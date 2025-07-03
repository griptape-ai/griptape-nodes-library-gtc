import logging
import time
from collections.abc import Generator

from base.base_griptape_cloud_node import BaseGriptapeCloudNode
from griptape_cloud_client.api.deployments.get_deployment import sync as get_deployment
from griptape_cloud_client.api.deployments.list_structure_deployments import sync as list_structure_deployments
from griptape_cloud_client.api.events.list_events import sync as list_events
from griptape_cloud_client.api.structure_runs.create_structure_run import sync as create_structure_run
from griptape_cloud_client.api.structure_runs.get_structure_run import sync as get_structure_run
from griptape_cloud_client.api.structures.list_structures import sync as list_structures
from griptape_cloud_client.models.create_structure_run_request_content import (
    CreateStructureRunRequestContent,
)
from griptape_cloud_client.models.create_structure_run_response_content import (
    CreateStructureRunResponseContent,
)
from griptape_cloud_client.models.deployment_status import DeploymentStatus
from griptape_cloud_client.models.event_detail import EventDetail
from griptape_cloud_client.models.get_deployment_response_content import GetDeploymentResponseContent
from griptape_cloud_client.models.get_structure_run_response_content import (
    GetStructureRunResponseContent,
)
from griptape_cloud_client.models.list_events_response_content import ListEventsResponseContent
from griptape_cloud_client.models.list_structure_deployments_response_content import (
    ListStructureDeploymentsResponseContent,
)
from griptape_cloud_client.models.list_structures_response_content import ListStructuresResponseContent
from griptape_cloud_client.models.structure_detail import StructureDetail
from griptape_cloud_client.types import UNSET
from griptape_nodes.exe_types.node_types import DataNode

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseStructureNode(BaseGriptapeCloudNode, DataNode):
    @classmethod
    def _structure_to_name_and_id(cls, structure: StructureDetail) -> str:
        return f"{structure.name} ({structure.structure_id})"

    def _list_structures(self) -> ListStructuresResponseContent:
        try:
            response = list_structures(
                client=self.client,
                page=1,
                page_size=100,
            )
            if isinstance(response, ListStructuresResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error listing structures: %s", e)
            raise

    def _get_deployment(self, deployment_id: str) -> GetDeploymentResponseContent:
        try:
            response = get_deployment(
                deployment_id=deployment_id,
                client=self.client,
            )
            if isinstance(response, GetDeploymentResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error getting deployment: %s", e)
            raise

    def _list_structure_deployments(
        self, structure_id: str, status: list[DeploymentStatus] | None = None
    ) -> ListStructureDeploymentsResponseContent:
        try:
            status_query = status or UNSET
            response = list_structure_deployments(structure_id=structure_id, client=self.client, status=status_query)
            if isinstance(response, ListStructureDeploymentsResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error getting deployment: %s", e)
            raise

    def _get_structure_run(self, structure_run_id: str) -> GetStructureRunResponseContent:
        try:
            response = get_structure_run(structure_run_id=structure_run_id, client=self.client)
            if isinstance(response, GetStructureRunResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error getting structure run: %s", e)
            raise

    def _create_structure_run(self, structure_id: str, args: list[str]) -> CreateStructureRunResponseContent:
        try:
            response = create_structure_run(
                structure_id=structure_id,
                body=CreateStructureRunRequestContent(
                    args=args,
                ),
                client=self.client,
            )
            if isinstance(response, CreateStructureRunResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error creating structure run: %s", e)
            raise

    def _list_structure_run_events(
        self, structure_run_id: str, offset: float | None = None
    ) -> ListEventsResponseContent:
        try:
            response = list_events(
                structure_run_id=structure_run_id,
                offset=str(offset) if offset is not None else None,
                client=self.client,
            )
            if isinstance(response, ListEventsResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error listing events: %s", e)
            raise

    def _poll_structure_run_events(self, structure_run_id: str) -> Generator[list[EventDetail], None, None]:
        run_completed = False
        offset: float | None = None

        while not run_completed:
            list_events_response = self._list_structure_run_events(structure_run_id=structure_run_id, offset=offset)
            offset = list_events_response.next_offset
            for event in list_events_response.events:
                if event.type_ == "StructureRunCompleted" and event.origin == "SYSTEM":
                    run_completed = True
            yield list_events_response.events
            time.sleep(0.5)

    def _is_deployment_ready(self, deployment: GetDeploymentResponseContent) -> bool:
        return deployment.status in [
            DeploymentStatus.SUCCEEDED,
        ]
