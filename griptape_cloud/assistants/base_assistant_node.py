import logging

from base.base_griptape_cloud_node import BaseGriptapeCloudNode
from griptape_cloud_client.models.assistant_detail import AssistantDetail
from griptape_nodes.exe_types.node_types import DataNode

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseAssistantNode(BaseGriptapeCloudNode, DataNode):
    @classmethod
    def _assistant_to_name_and_id(cls, assistant: AssistantDetail) -> str:
        return f"{assistant.name} ({assistant.assistant_id})"
