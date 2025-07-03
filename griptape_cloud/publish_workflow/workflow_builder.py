"""WorkflowBuilder for generating a Griptape Nodes workflow that can invoke a published workflow in the form of a Griptape Cloud structure.

This module provides simple script generation for creating workflows that follow the pattern:
StartNode -> PublishedWorkflow -> EndNode

The generated workflows can execute published structures in Griptape Cloud using the
PublishedWorkflow node which handles parameter mapping automatically.
"""

import logging
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any

from griptape_nodes.retained_mode.griptape_nodes import GriptapeNodes

logger = logging.getLogger(__name__)


class WorkflowBuilder:
    """Builder class for generating executor workflows using simple script generation."""

    def __init__(self, workflow_name: str, executor_workflow_name: str, libraries: list[str] | None = None) -> None:
        """Initialize the WorkflowBuilder.

        Args:
            workflow_name: Name of the original workflow that was published
            executor_workflow_name: Name of the executor workflow to be created
            libraries: List of libraries needed for the workflow
        """
        self.workflow_name = workflow_name
        self.executor_workflow_name = executor_workflow_name
        self.libraries = libraries or []

    def generate_executor_workflow(self, structure_id: str, workflow_shape: dict[str, Any]) -> Path:
        """Generate an executor workflow that can invoke the published structure.

        Args:
            structure_id: The ID of the published structure in Griptape Cloud
            workflow_shape: The input/output shape of the original workflow
        """
        # Generate a simple workflow creation script using PublishedWorkflow node
        workflow_script = self._build_simple_workflow_script(structure_id, workflow_shape, self.libraries)

        # Execute the script in a subprocess to create the workflow
        self._execute_workflow_script(workflow_script)

        # Verify the workflow was created successfully
        executor_workflow_path = GriptapeNodes.ConfigManager().workspace_path / (self.executor_workflow_name + ".py")
        if not executor_workflow_path.exists():
            error_msg = f"Executor workflow {self.executor_workflow_name} was not created successfully."
            logger.error(error_msg)
            raise RuntimeError(error_msg)
        return executor_workflow_path

    def _build_library_registration_script(self, libraries: list[str]) -> str:
        """Build a script to register libraries for the workflow.

        Args:
            libraries: List of library paths to register

        Returns:
            Complete Python script as string
        """
        if not libraries:
            return ""

        # Build the library registration script
        script = ""

        for i, lib in enumerate(libraries):
            if lib.endswith(".json"):
                script += f"""
    request_{str(i)} = GriptapeNodes.handle_request(RegisterLibraryFromFileRequest(file_path="{lib}"))
"""
            else:
                script += f"""
    request_{str(i)} = GriptapeNodes.handle_request(RegisterLibraryFromRequirementSpecifierRequest(requirement_specifier="{lib}"))
"""
        return script

    def _build_simple_workflow_script(
        self, structure_id: str, workflow_shape: dict[str, Any], libraries: list[str]
    ) -> str:
        """Build a simple workflow creation script using PublishedWorkflow node.

        Args:
            structure_id: The Griptape Cloud structure ID
            workflow_shape: Input/output parameter structure
            libraries: List of libraries needed for the workflow

        Returns:
            Complete Python script as string
        """
        # Get parameter information directly from workflow_shape
        input_params = []
        if "input" in workflow_shape:
            for node_params in workflow_shape["input"].values():
                if isinstance(node_params, dict):
                    input_params.extend(node_params.values())

        output_params = []
        if "output" in workflow_shape:
            for node_params in workflow_shape["output"].values():
                if isinstance(node_params, dict):
                    output_params.extend(node_params.values())

        # Build the workflow generation script
        script = f'''
"""
Generated executor workflow for invoking published Griptape Cloud structure.
This workflow was automatically created to execute structure: {structure_id}
"""

from griptape_nodes.retained_mode.griptape_nodes import GriptapeNodes
from griptape_nodes.retained_mode.events.flow_events import CreateFlowRequest
from griptape_nodes.retained_mode.events.node_events import CreateNodeRequest
from griptape_nodes.retained_mode.events.library_events import (
    RegisterLibraryFromFileRequest,
    RegisterLibraryFromRequirementSpecifierRequest,
)
from griptape_nodes.retained_mode.events.parameter_events import AddParameterToNodeRequest
from griptape_nodes.retained_mode.events.connection_events import CreateConnectionRequest
from griptape_nodes.retained_mode.events.workflow_events import SaveWorkflowRequest

def main():
    {self._build_library_registration_script(libraries)}

    context_manager = GriptapeNodes.ContextManager()
    if not context_manager.has_current_workflow():
        context_manager.push_workflow(workflow_name="{self.executor_workflow_name}")

    # Create the main flow
    flow_response = GriptapeNodes.handle_request(CreateFlowRequest(parent_flow_name=None))
    flow_name = flow_response.flow_name

    with GriptapeNodes.ContextManager().flow(flow_name):
        # Create StartNode
        start_node_response = GriptapeNodes.handle_request(CreateNodeRequest(
            node_type="StartFlow",
            specific_library_name="Griptape Nodes Library",
            node_name="Start Flow",
            initial_setup=True
        ))
        start_node_name = start_node_response.node_name

        # Create GriptapeCloudPublishedWorkflow node
        published_wf_response = GriptapeNodes.handle_request(CreateNodeRequest(
            node_type="GriptapeCloudPublishedWorkflow",
            specific_library_name="Griptape Cloud Library",
            node_name="Published Workflow",
            metadata={{
                "workflow_shape": {workflow_shape!r},
                "structure_id": "{structure_id}",
                "structure_name": "{self.workflow_name}"
            }},
            initial_setup=True
        ))
        published_wf_name = published_wf_response.node_name

        # Create EndNode
        end_node_response = GriptapeNodes.handle_request(CreateNodeRequest(
            node_type="EndFlow",
            specific_library_name="Griptape Nodes Library",
            node_name="End Flow",
            initial_setup=True
        ))
        end_node_name = end_node_response.node_name

        # Configure StartNode parameters
        with GriptapeNodes.ContextManager().node(start_node_name):'''

        # Add parameter configuration for StartNode
        for param in input_params:
            # Create a copy and remap 'name' to 'parameter_name'
            param_config = dict(param)
            param_config["parameter_name"] = param_config.pop("name")
            script += f"""
            GriptapeNodes.handle_request(AddParameterToNodeRequest(
                **{param_config},
                mode_allowed_input=False,
                mode_allowed_property=True,
                mode_allowed_output=True,
                initial_setup=True
            ))"""

        script += """

        # Configure GriptapeCloudPublishedWorkflow parameters
        with GriptapeNodes.ContextManager().node(published_wf_name):"""

        # Add input parameter configuration for GriptapeCloudPublishedWorkflow
        for param in input_params:
            # Create a copy and remap 'name' to 'parameter_name'
            param_config = dict(param)
            param_config["parameter_name"] = param_config.pop("name")
            script += f"""
            GriptapeNodes.handle_request(AddParameterToNodeRequest(
                **{param_config},
                mode_allowed_input=True,
                mode_allowed_property=True,
                mode_allowed_output=False,
                initial_setup=True
            ))"""

        # Add output parameter configuration for GriptapeCloudPublishedWorkflow
        for param in output_params:
            # Create a copy and remap 'name' to 'parameter_name'
            param_config = dict(param)
            param_config["parameter_name"] = param_config.pop("name")
            script += f"""
            GriptapeNodes.handle_request(AddParameterToNodeRequest(
                **{param_config},
                mode_allowed_input=False,
                mode_allowed_property=True,
                mode_allowed_output=True,
                initial_setup=True
            ))"""

        script += """

        # Configure EndNode parameters
        with GriptapeNodes.ContextManager().node(end_node_name):"""

        # Add parameter configuration for EndNode
        for param in output_params:
            # Create a copy and remap 'name' to 'parameter_name'
            param_config = dict(param)
            param_config["parameter_name"] = param_config.pop("name")
            script += f"""
            GriptapeNodes.handle_request(AddParameterToNodeRequest(
                **{param_config},
                mode_allowed_input=True,
                mode_allowed_property=True,
                mode_allowed_output=False,
                initial_setup=True
            ))"""

        script += """

    # Create connections between StartNode and GriptapeCloudPublishedWorkflow"""

        # Add connections for each input parameter
        for param in input_params:
            script += f"""
    GriptapeNodes.handle_request(CreateConnectionRequest(
        source_node_name=start_node_name,
        source_parameter_name="{param["name"]}",
        target_node_name=published_wf_name,
        target_parameter_name="{param["name"]}",
        initial_setup=True
    ))"""

        script += """

    # Create connections between GriptapeCloudPublishedWorkflow and EndNode"""

        # Add connections for each output parameter
        for param in output_params:
            script += f"""
    GriptapeNodes.handle_request(CreateConnectionRequest(
        source_node_name=published_wf_name,
        source_parameter_name="{param["name"]}",
        target_node_name=end_node_name,
        target_parameter_name="{param["name"]}",
        initial_setup=True
    ))"""

        script += f"""

    # Save the workflow
    save_response = GriptapeNodes.handle_request(SaveWorkflowRequest(
        file_name="{self.executor_workflow_name}"))

    if save_response.succeeded():
        print(f"Successfully created executor workflow: {self.executor_workflow_name}")
    else:
        print(f"Failed to create executor workflow")
        exit(1)

if __name__ == "__main__":
    main()
"""

        return script

    def _execute_workflow_script(self, script: str) -> None:
        """Execute the workflow creation script in a subprocess."""
        temp_script_path = Path(__file__).parent / f"temp_executor_{uuid.uuid4().hex}.py"

        try:
            with temp_script_path.open("w", encoding="utf-8") as f:
                f.write(script)

            # Execute the script in a subprocess to isolate the GriptapeNodes state
            result = subprocess.run(  # noqa: S603
                [sys.executable, str(temp_script_path)],
                capture_output=True,
                text=True,
                cwd=temp_script_path.parent,
                timeout=30,
                check=False,
            )

            # Print subprocess output
            if result.stdout:
                logger.debug(result.stdout)
            if result.stderr:
                logger.debug(result.stderr)

            if result.returncode != 0:
                error_msg = f"Executor workflow generation failed: {result.stderr}"
                logger.error("Failed to generate executor workflow: %s", result.stderr)
                raise RuntimeError(error_msg)

            logger.info("Successfully generated executor workflow: %s", self.executor_workflow_name)

        finally:
            # Clean up temporary script
            if temp_script_path.exists():
                temp_script_path.unlink()
