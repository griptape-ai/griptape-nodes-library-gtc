from __future__ import annotations

import importlib.metadata
import json
import logging
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from urllib.parse import urljoin

from dotenv import set_key
from dotenv.main import DotEnv
from griptape_cloud_client.api.assets.create_asset import sync as create_asset
from griptape_cloud_client.api.assets.create_asset_url import sync as create_asset_url
from griptape_cloud_client.api.structures.create_structure import sync as create_structure
from griptape_cloud_client.api.structures.update_structure import sync as update_structure
from griptape_cloud_client.client import AuthenticatedClient
from griptape_cloud_client.models.assert_url_operation import AssertUrlOperation
from griptape_cloud_client.models.create_asset_request_content import CreateAssetRequestContent
from griptape_cloud_client.models.create_asset_response_content import (
    CreateAssetResponseContent,
)
from griptape_cloud_client.models.create_asset_url_request_content import CreateAssetUrlRequestContent
from griptape_cloud_client.models.create_asset_url_response_content import CreateAssetUrlResponseContent
from griptape_cloud_client.models.create_structure_request_content import CreateStructureRequestContent
from griptape_cloud_client.models.create_structure_response_content import (
    CreateStructureResponseContent,
)
from griptape_cloud_client.models.data_lake_structure_code import DataLakeStructureCode
from griptape_cloud_client.models.structure_code_type_1 import StructureCodeType1
from griptape_cloud_client.models.update_structure_request_content import UpdateStructureRequestContent
from griptape_cloud_client.models.update_structure_response_content import UpdateStructureResponseContent
from griptape_nodes.node_library.library_registry import LibraryNameAndVersion, LibraryRegistry
from griptape_nodes.node_library.workflow_registry import Workflow, WorkflowRegistry
from griptape_nodes.retained_mode.events.app_events import (
    GetEngineVersionRequest,
    GetEngineVersionResultSuccess,
)
from griptape_nodes.retained_mode.events.secrets_events import (
    GetAllSecretValuesRequest,
    GetAllSecretValuesResultSuccess,
)
from griptape_nodes.retained_mode.events.workflow_events import (
    PublishWorkflowResultFailure,
    PublishWorkflowResultSuccess,
)
from griptape_nodes.retained_mode.griptape_nodes import (
    GriptapeNodes,
)
from httpx import Client
from publish_workflow.workflow_builder import WorkflowBuilder

if TYPE_CHECKING:
    from griptape_nodes.retained_mode.events.base_events import ResultPayload
    from griptape_nodes.retained_mode.managers.library_manager import LibraryManager


T = TypeVar("T")


logger = logging.getLogger("griptape_cloud_publisher")

GRIPTAPE_SERVICE = "Griptape"


class GriptapeCloudPublisher:
    def __init__(self, workflow_name: str) -> None:
        self._workflow_name = workflow_name
        self._client = Client()
        self._gtc_client = AuthenticatedClient(
            base_url=self._get_base_url(),
            token=self._get_secret("GT_CLOUD_API_KEY"),
            verify_ssl=False,
        )
        self._gt_cloud_bucket_id = self._get_secret("GT_CLOUD_BUCKET_ID")

    def publish_workflow(self) -> ResultPayload:
        try:
            # Get the workflow shape
            workflow_shape = GriptapeNodes.WorkflowManager().extract_workflow_shape(self._workflow_name)
            logger.info("Workflow shape: %s", workflow_shape)

            # Package the workflow
            package_path = self._package_workflow(self._workflow_name)
            logger.info("Workflow packaged to path: %s", package_path)

            # Deploy the workflow to Griptape Cloud
            structure = self._deploy_workflow_to_cloud(package_path)
            logger.info(
                "Workflow '%s' published successfully to Structure: %s", self._workflow_name, structure.structure_id
            )

            # Generate an executor workflow that can invoke the published structure
            executor_workflow_path = self._generate_executor_workflow(structure.structure_id, workflow_shape)

            return PublishWorkflowResultSuccess(
                published_workflow_file_path=str(executor_workflow_path),
            )
        except Exception as e:
            details = f"Failed to publish workflow '{self._workflow_name}'. Error: {e}"
            logger.error(details)
            return PublishWorkflowResultFailure()

    @classmethod
    def _get_base_url(cls) -> str:
        """Retrieves the base URL for the Griptape Cloud service."""
        base_url = os.environ.get("GT_CLOUD_BASE_URL") or "https://cloud.griptape.ai"
        if not base_url.endswith("/api"):
            base_url = urljoin(base_url, "/api")
        return base_url

    @classmethod
    def _get_config_value(cls, service: str, value: str) -> str:
        """Retrieves a configuration value from the ConfigManager."""
        config_value = GriptapeNodes.ConfigManager().get_config_value(f"nodes.{service}.{value}")
        if not config_value:
            details = f"Failed to get configuration value '{value}' for service '{service}'."
            logger.error(details)
            raise ValueError(details)
        return config_value

    @classmethod
    def _get_secret(cls, secret: str) -> str:
        """Retrieves a secret value from the SecretsManager."""
        secret_value = GriptapeNodes.SecretsManager().get_secret(secret)
        if not secret_value:
            details = f"Failed to get secret:'{secret}'."
            logger.error(details)
            raise ValueError(details)
        return secret_value

    def _upload_file_to_data_lake(self, name: str, value: bytes) -> None:
        create_asset_response = create_asset(
            client=self._gtc_client,
            bucket_id=self._gt_cloud_bucket_id,
            body=CreateAssetRequestContent(
                name=name,
            ),
        )
        if not isinstance(create_asset_response, CreateAssetResponseContent):
            msg = f"Unexpected response type when creating asset: {type(create_asset_response)}"
            logger.error(msg)
            raise TypeError(msg)

        create_asset_url_response = create_asset_url(
            client=self._gtc_client,
            bucket_id=self._gt_cloud_bucket_id,
            name=name,
            body=CreateAssetUrlRequestContent(operation=AssertUrlOperation.PUT),
        )
        if not isinstance(create_asset_url_response, CreateAssetUrlResponseContent):
            msg = f"Unexpected response type when creating asset URL: {type(create_asset_url_response)}"
            logger.error(msg)
            raise TypeError(msg)
        url = create_asset_url_response.url
        headers = create_asset_url_response.headers
        try:
            response = self._client.put(
                url=url,
                headers=headers.to_dict(),
                data=value,
            )
            response.raise_for_status()
        except Exception as e:
            logger.exception(f"Failed to upload file to data lake: {e}")
            raise

    def _deploy_workflow_to_cloud(self, package_path: str) -> UpdateStructureResponseContent:
        create_structure_response = create_structure(
            client=self._gtc_client,
            body=CreateStructureRequestContent(
                name=self._workflow_name,
                description=f"Published Griptape Nodes workflow '{self._workflow_name}'",
                structure_config_file="structure_config.yaml",
            ),
        )
        if not isinstance(create_structure_response, CreateStructureResponseContent):
            msg = f"Unexpected response type when creating structure: {type(create_structure_response)}"
            logger.error(msg)
            raise TypeError(msg)

        with Path(package_path).open("rb") as file:
            file_contents = file.read()
            file_name = Path(package_path).name

        asset_name = f"{create_structure_response.structure_id}/{file_name}"
        self._upload_file_to_data_lake(name=asset_name, value=file_contents)

        update_structure_response = update_structure(
            client=self._gtc_client,
            structure_id=create_structure_response.structure_id,
            body=UpdateStructureRequestContent(
                structure_config_file="structure_config.yaml",
                code=StructureCodeType1(
                    data_lake=DataLakeStructureCode(
                        bucket_id=self._gt_cloud_bucket_id,
                        asset_path=asset_name,
                    ),
                ),
            ),
        )
        if not isinstance(update_structure_response, UpdateStructureResponseContent):
            msg = f"Unexpected response type when updating structure: {type(update_structure_response)}"
            logger.error(msg)
            raise TypeError(msg)

        return update_structure_response

    def _copy_libraries_to_path_for_workflow(
        self,
        node_libraries: list[LibraryNameAndVersion],
        destination_path: Path,
        runtime_env_path: Path,
        workflow: Workflow,
    ) -> list[str]:
        """Copies the libraries to the specified path for the workflow, returning the list of library paths.

        This is used to package the workflow for publishing.
        """
        library_paths: list[str] = []

        for library_ref in node_libraries:
            library = GriptapeNodes.LibraryManager().get_library_info_by_library_name(library_ref.library_name)

            if library is None:
                details = f"Attempted to publish workflow '{workflow.metadata.name}', but failed gathering library info for library '{library_ref.library_name}'."
                logger.error(details)
                raise ValueError(details)

            library_data = LibraryRegistry.get_library(library_ref.library_name).get_library_data()

            if library.library_path.endswith(".json"):
                library_path = Path(library.library_path)
                absolute_library_path = library_path.resolve()
                abs_paths = [absolute_library_path]
                for node in library_data.nodes:
                    p = (library_path.parent / Path(node.file_path)).resolve()
                    abs_paths.append(p)
                common_root = Path(os.path.commonpath([str(p) for p in abs_paths]))
                dest = destination_path / common_root.name
                shutil.copytree(
                    common_root, dest, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".venv", "__pycache__")
                )
                library_path_relative_to_common_root = absolute_library_path.relative_to(common_root)
                library_paths.append(str(runtime_env_path / common_root.name / library_path_relative_to_common_root))
            else:
                library_paths.append(library.library_path)

        return library_paths

    def __get_install_source(self) -> tuple[Literal["git", "file", "pypi"], str | None]:
        """Determines the install source of the Griptape Nodes package.

        Returns:
            tuple: A tuple containing the install source and commit ID (if applicable).
        """
        dist = importlib.metadata.distribution("griptape_nodes")
        direct_url_text = dist.read_text("direct_url.json")
        # installing from pypi doesn't have a direct_url.json file
        if direct_url_text is None:
            logger.debug("No direct_url.json file found, assuming pypi install")
            return "pypi", None

        direct_url_info = json.loads(direct_url_text)
        url = direct_url_info.get("url")
        if url.startswith("file://"):
            try:
                pkg_dir = Path(str(dist.locate_file(""))).resolve()
                git_root = next(p for p in (pkg_dir, *pkg_dir.parents) if (p / ".git").is_dir())
                commit = (
                    subprocess.check_output(
                        ["git", "rev-parse", "--short", "HEAD"],  # noqa: S607
                        cwd=git_root,
                        stderr=subprocess.DEVNULL,
                    )
                    .decode()
                    .strip()
                )
            except (StopIteration, subprocess.CalledProcessError):
                logger.debug("File URL but no git repo → file")
                return "file", None
            else:
                logger.debug("Detected git repo at %s (commit %s)", git_root, commit)
                return "git", commit
        if "vcs_info" in direct_url_info:
            logger.debug("Detected git repo at %s", url)
            return "git", direct_url_info["vcs_info"].get("commit_id")[:7]
        # Fall back to pypi if no other source is found
        logger.debug("Failed to detect install source, assuming pypi")
        return "pypi", None

    def _get_merged_env_file_mapping(self, workspace_env_file_path: Path) -> dict[str, Any]:
        """Merges the secrets from the workspace env file with the secrets from the GriptapeNodes SecretsManager.

        This is used to create a single .env file for the workflow. We can gather all secrets explicitly defined in the .env file
        and by the settings/SecretsManager, but we will not gather all secrets from the OS env for the purpose of publishing.
        """
        env_file_dict = {}
        if workspace_env_file_path.exists():
            env_file = DotEnv(workspace_env_file_path)
            env_file_dict = env_file.dict()

        get_all_secrets_request = GetAllSecretValuesRequest()
        get_all_secrets_result = GriptapeNodes.handle_request(request=get_all_secrets_request)
        if not isinstance(get_all_secrets_result, GetAllSecretValuesResultSuccess):
            details = "Failed to get all secret values."
            logger.error(details)
            raise TypeError(details)

        secret_values = get_all_secrets_result.values
        for secret_name, secret_value in secret_values.items():
            if secret_name not in env_file_dict:
                env_file_dict[secret_name] = secret_value

        return env_file_dict

    def _write_env_file(self, env_file_path: Path, env_file_dict: dict[str, Any]) -> None:
        env_file_path.touch(exist_ok=True)
        for key, val in env_file_dict.items():
            set_key(env_file_path, key, str(val))

    def _package_workflow(self, workflow_name: str) -> str:  # noqa: PLR0915
        config_manager = GriptapeNodes.get_instance()._config_manager
        secrets_manager = GriptapeNodes.get_instance()._secrets_manager
        workflow = WorkflowRegistry.get_workflow_by_name(workflow_name)

        engine_version: str = ""
        engine_version_request = GetEngineVersionRequest()
        engine_version_result = GriptapeNodes.handle_request(request=engine_version_request)
        if not engine_version_result.succeeded():
            details = (
                f"Attempted to publish workflow '{workflow.metadata.name}', but failed getting the engine version."
            )
            logger.error(details)
            raise ValueError(details)
        engine_version_success = cast("GetEngineVersionResultSuccess", engine_version_result)
        engine_version = (
            f"v{engine_version_success.major}.{engine_version_success.minor}.{engine_version_success.patch}"
        )

        # This is the path where the full workflow will be packaged to in the runtime environment.
        packaged_top_level_dir = "/structure"

        # Gather the paths to the files we need to copy.
        # Files are now located in the publish_workflow directory
        publish_workflow_path = Path(__file__).parent
        structure_file_path = publish_workflow_path / "structure.py"
        structure_workflow_executor_file_path = publish_workflow_path / "structure_workflow_executor.py"
        structure_config_file_path = publish_workflow_path / "structure_config.yaml"
        pre_build_install_script_path = publish_workflow_path / "pre_build_install_script.sh"
        post_build_install_script_path = publish_workflow_path / "post_build_install_script.sh"
        # Note: register_libraries_script.py might need to be created if it doesn't exist
        register_libraries_script_path = publish_workflow_path / "register_libraries_script.py"
        full_workflow_file_path = WorkflowRegistry.get_complete_file_path(workflow.file_path)

        env_file_mapping = self._get_merged_env_file_mapping(secrets_manager.workspace_env_path)

        config = config_manager.user_config
        config["workspace_directory"] = packaged_top_level_dir

        # Create a temporary directory to perform the packaging
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_dir_path = Path(tmp_dir)
            temp_workflow_file_path = tmp_dir_path / "workflow.py"
            temp_structure_path = tmp_dir_path / "structure.py"
            temp_structure_workflow_executor_path = tmp_dir_path / "structure_workflow_executor.py"
            temp_pre_build_install_script_path = tmp_dir_path / "pre_build_install_script.sh"
            temp_post_build_install_script_path = tmp_dir_path / "post_build_install_script.sh"
            temp_register_libraries_script_path = tmp_dir_path / "register_libraries_script.py"
            config_file_path = tmp_dir_path / "GriptapeNodes" / "griptape_nodes_config.json"
            init_file_path = tmp_dir_path / "__init__.py"

            try:
                # Copy the workflow file, libraries, and structure files to the temporary directory
                shutil.copyfile(full_workflow_file_path, temp_workflow_file_path)
                shutil.copyfile(structure_workflow_executor_file_path, temp_structure_workflow_executor_path)
                shutil.copyfile(pre_build_install_script_path, temp_pre_build_install_script_path)
                shutil.copyfile(post_build_install_script_path, temp_post_build_install_script_path)
                shutil.copyfile(structure_config_file_path, tmp_dir_path / "structure_config.yaml")

                # Write the environment variables to the .env file
                self._write_env_file(tmp_dir_path / ".env", env_file_mapping)

                # Get the library paths
                library_paths: list[str] = self._copy_libraries_to_path_for_workflow(
                    node_libraries=workflow.metadata.node_libraries_referenced,
                    destination_path=tmp_dir_path / "libraries",
                    runtime_env_path=Path(packaged_top_level_dir) / "libraries",
                    workflow=workflow,
                )
                config["app_events"] = {
                    "on_app_initialization_complete": {
                        "workflows_to_register": [],
                        "libraries_to_register": library_paths,
                    }
                }
                library_paths_formatted = [f'"{library_path}"' for library_path in library_paths]

                with register_libraries_script_path.open("r", encoding="utf-8") as register_libraries_script_file:
                    register_libraries_script_contents = register_libraries_script_file.read()
                    register_libraries_script_contents = register_libraries_script_contents.replace(
                        '["REPLACE_LIBRARY_PATHS"]',
                        f"[{', '.join(library_paths_formatted)}]",
                    )
                with temp_register_libraries_script_path.open("w", encoding="utf-8") as register_libraries_script_file:
                    register_libraries_script_file.write(register_libraries_script_contents)

                with structure_file_path.open("r", encoding="utf-8") as structure_file:
                    structure_file_contents = structure_file.read()
                    structure_file_contents = structure_file_contents.replace(
                        '["REPLACE_LIBRARIES"]',
                        f"[{', '.join(library_paths_formatted)}]",
                    )
                with temp_structure_path.open("w", encoding="utf-8") as structure_file:
                    structure_file.write(structure_file_contents)

                config_file_path.parent.mkdir(parents=True, exist_ok=True)
                with config_file_path.open("w", encoding="utf-8") as config_file:
                    config_file.write(json.dumps(config, indent=4))

                init_file_path.parent.mkdir(parents=True, exist_ok=True)
                with init_file_path.open("w", encoding="utf-8") as init_file:
                    init_file.write('"""This is a temporary __init__.py file for the structure."""\n')

                shutil.copyfile(config_file_path, tmp_dir_path / "griptape_nodes_config.json")

            except Exception as e:
                details = f"Failed to copy files to temporary directory. Error: {e}"
                logger.exception(details)
                raise

            # Create the requirements.txt file using the correct engine version
            source, commit_id = self.__get_install_source()
            if source == "git" and commit_id is not None:
                engine_version = commit_id
            requirements_file_path = tmp_dir_path / "requirements.txt"
            with requirements_file_path.open("w", encoding="utf-8") as requirements_file:
                requirements_file.write(
                    f"griptape-nodes @ git+https://github.com/griptape-ai/griptape-nodes.git@{engine_version}\n"
                )

            archive_base_name = config_manager.workspace_path / workflow_name
            shutil.make_archive(str(archive_base_name), "zip", tmp_dir)
            return str(archive_base_name) + ".zip"

    def _generate_executor_workflow(self, structure_id: str, workflow_shape: dict[str, Any]) -> Path:
        """Generate a new workflow file that can execute the published structure.

        This creates a simple workflow with StartNode -> PublishedWorkflow -> EndNode
        that can invoke the published workflow in Griptape Cloud.

        Args:
            structure_id: The ID of the published structure in Griptape Cloud
            workflow_shape: The input/output shape of the original workflow
        """
        # Use WorkflowBuilder to generate the executor workflow
        libraries: list[LibraryManager.LibraryInfo] = []
        if nodes_library := GriptapeNodes.LibraryManager().get_library_info_by_library_name("Griptape Nodes Library"):
            libraries.append(nodes_library)
        else:
            details = "Griptape Nodes Library is not available. Cannot generate executor workflow."
            logger.error(details)
            raise ValueError(details)
        if cloud_library := GriptapeNodes.LibraryManager().get_library_info_by_library_name("Griptape Cloud Library"):
            libraries.append(cloud_library)
        else:
            details = "Griptape Cloud Library is not available. Cannot generate executor workflow."
            logger.error(details)
            raise ValueError(details)
        library_paths = [library.library_path for library in libraries if library.library_path is not None]
        builder = WorkflowBuilder(
            workflow_name=self._workflow_name,
            executor_workflow_name=f"{self._workflow_name}_gtc_executor_{structure_id}",
            libraries=library_paths,
        )
        return builder.generate_executor_workflow(structure_id, workflow_shape)
