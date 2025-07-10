import logging

from base.base_griptape_cloud_node import BaseGriptapeCloudNode
from griptape_cloud_client.api.buckets.create_bucket import sync as create_bucket
from griptape_cloud_client.api.buckets.delete_bucket import sync as delete_bucket
from griptape_cloud_client.api.buckets.get_bucket import sync as get_bucket
from griptape_cloud_client.api.buckets.list_buckets import sync as list_buckets
from griptape_cloud_client.api.buckets.update_bucket import sync as update_bucket
from griptape_cloud_client.models.bucket_detail import BucketDetail
from griptape_cloud_client.models.create_bucket_request_content import CreateBucketRequestContent
from griptape_cloud_client.models.create_bucket_response_content import CreateBucketResponseContent
from griptape_cloud_client.models.get_bucket_response_content import GetBucketResponseContent
from griptape_cloud_client.models.list_buckets_response_content import ListBucketsResponseContent
from griptape_cloud_client.models.update_bucket_request_content import UpdateBucketRequestContent
from griptape_cloud_client.models.update_bucket_response_content import UpdateBucketResponseContent
from griptape_nodes.exe_types.node_types import DataNode

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseBucketNode(BaseGriptapeCloudNode, DataNode):
    @classmethod
    def _bucket_to_name_and_id(cls, bucket: BucketDetail) -> str:
        return f"{bucket.name} ({bucket.bucket_id})"

    def _list_buckets(self) -> ListBucketsResponseContent:
        try:
            response = list_buckets(
                client=self.client,
                page=1,
                page_size=100,
            )
            if isinstance(response, ListBucketsResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error listing buckets: %s", e)
            raise

    def _get_bucket(self, bucket_id: str) -> GetBucketResponseContent:
        try:
            response = get_bucket(bucket_id=bucket_id, client=self.client)
            if isinstance(response, GetBucketResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error getting bucket: %s", e)
            raise

    def _create_bucket(self, name: str) -> CreateBucketResponseContent:
        try:
            response = create_bucket(
                body=CreateBucketRequestContent(name=name),
                client=self.client,
            )
            if isinstance(response, CreateBucketResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error creating bucket: %s", e)
            raise

    def _update_bucket(self, bucket_id: str, name: str) -> UpdateBucketResponseContent:
        try:
            response = update_bucket(
                bucket_id=bucket_id,
                body=UpdateBucketRequestContent(name=name),
                client=self.client,
            )
            if isinstance(response, UpdateBucketResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error updating bucket: %s", e)
            raise

    def _delete_bucket(self, bucket_id: str) -> None:
        try:
            delete_bucket(bucket_id=bucket_id, client=self.client)
        except Exception as e:
            logger.error("Error deleting bucket: %s", e)
            raise
