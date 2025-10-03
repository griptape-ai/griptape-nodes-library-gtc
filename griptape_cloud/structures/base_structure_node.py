import logging

from base.base_griptape_cloud_node import BaseGriptapeCloudNode
from griptape_cloud_client.models.structure_detail import StructureDetail

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseStructureNode(BaseGriptapeCloudNode):
    @classmethod
    def _structure_to_name_and_id(cls, structure: StructureDetail) -> str:
        return f"{structure.name} ({structure.structure_id})"
