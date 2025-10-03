import logging
import os
from urllib.parse import urljoin

from griptape_cloud_client.client import AuthenticatedClient
from griptape_nodes.exe_types.node_types import BaseNode
from mixins.griptape_cloud_api_mixin import GriptapeCloudApiMixin

DEFAULT_GRIPTAPE_CLOUD_ENDPOINT = urljoin(base=os.getenv("GT_CLOUD_BASE_URL", "https://cloud.griptape.ai"), url="/api/")
API_KEY_ENV_VAR = "GT_CLOUD_API_KEY"
SERVICE = "Griptape"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseGriptapeCloudNode(BaseNode, GriptapeCloudApiMixin):
    def __init__(self, name: str | None = None, **kwargs) -> None:
        # Handle name as either positional or keyword argument
        if name is not None:
            kwargs["name"] = name
        super().__init__(**kwargs)
        self.base_url = DEFAULT_GRIPTAPE_CLOUD_ENDPOINT
        self.gtc_client = AuthenticatedClient(
            base_url=self.base_url,
            token=self.get_config_value(service=SERVICE, value=API_KEY_ENV_VAR),
            verify_ssl=False,
        )

    def validate_before_workflow_run(self) -> list[Exception] | None:
        exceptions = []

        try:
            api_key = self.get_config_value(service=SERVICE, value=API_KEY_ENV_VAR)

            if not api_key:
                msg = f"{API_KEY_ENV_VAR} is not defined"
                exceptions.append(KeyError(msg))

        except Exception as e:
            exceptions.append(e)

        return exceptions if exceptions else None
