import logging

from base.base_griptape_cloud_node import BaseGriptapeCloudNode
from griptape_cloud_client.api.assets.create_asset import sync as create_asset
from griptape_cloud_client.api.assets.create_asset_url import sync as create_asset_url
from griptape_cloud_client.api.buckets.list_buckets import sync as list_buckets
from griptape_cloud_client.models.assert_url_operation import AssertUrlOperation
from griptape_cloud_client.models.bucket_detail import BucketDetail
from griptape_cloud_client.models.create_asset_request_content import CreateAssetRequestContent
from griptape_cloud_client.models.create_asset_response_content import (
    CreateAssetResponseContent,
)
from griptape_cloud_client.models.create_asset_url_request_content import CreateAssetUrlRequestContent
from griptape_cloud_client.models.create_asset_url_response_content import CreateAssetUrlResponseContent
from griptape_cloud_client.models.list_buckets_response_content import ListBucketsResponseContent
from griptape_nodes.exe_types.node_types import DataNode

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseAssetNode(BaseGriptapeCloudNode, DataNode):
    @classmethod
    def _bucket_to_name_and_id(cls, bucket: BucketDetail) -> str:
        return f"{bucket.name} ({bucket.bucket_id})"

    def _create_asset(
        self,
        asset_name: str,
        bucket_id: str,
    ) -> CreateAssetResponseContent:
        try:
            response = create_asset(
                bucket_id=bucket_id,
                client=self.client,
                body=CreateAssetRequestContent(
                    name=asset_name,
                ),
            )
            if isinstance(response, CreateAssetResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error creating asset: %s", e)
            raise

    def _create_asset_url(
        self, asset_name: str, bucket_id: str, operation: AssertUrlOperation = AssertUrlOperation.GET
    ) -> CreateAssetUrlResponseContent:
        try:
            response = create_asset_url(
                bucket_id=bucket_id,
                name=asset_name,
                client=self.client,
                body=CreateAssetUrlRequestContent(
                    operation=operation,
                ),
            )
            if isinstance(response, CreateAssetUrlResponseContent):
                return response
            msg = f"Unexpected response type: {type(response)}"
            logger.error(msg)
            raise TypeError(msg)  # noqa: TRY301
        except Exception as e:
            logger.error("Error creating asset URL: %s", e)
            raise

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
