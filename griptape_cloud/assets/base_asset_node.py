import logging

from base.base_griptape_cloud_node import BaseGriptapeCloudNode
from griptape_cloud_client.models.bucket_detail import BucketDetail
from griptape_nodes.exe_types.node_types import DataNode

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseAssetNode(BaseGriptapeCloudNode, DataNode):
    @classmethod
    def _bucket_to_name_and_id(cls, bucket: BucketDetail) -> str:
        return f"{bucket.name} ({bucket.bucket_id})"
