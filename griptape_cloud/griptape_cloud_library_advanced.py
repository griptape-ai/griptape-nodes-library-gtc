import logging

from griptape_nodes.node_library.advanced_node_library import AdvancedNodeLibrary
from griptape_nodes.node_library.library_registry import Library, LibrarySchema
from griptape_nodes.retained_mode.events.base_events import ResultPayload
from griptape_nodes.retained_mode.events.workflow_events import PublishWorkflowRequest
from griptape_nodes.retained_mode.griptape_nodes import GriptapeNodes
from publish_workflow.griptape_cloud_publisher import GriptapeCloudPublisher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _publish_workflow_request_handler(request: PublishWorkflowRequest) -> ResultPayload:
    publisher = GriptapeCloudPublisher(
        workflow_name=request.workflow_name,
    )
    return publisher.publish_workflow()


class GriptapeCloudLibraryAdvanced(AdvancedNodeLibrary):
    """Advanced library implementation for the default Griptape Cloud Library."""

    def before_library_nodes_loaded(self, library_data: LibrarySchema, library: Library):
        """Called before any nodes are loaded from the library."""
        print(f"🚀 Starting to load nodes for '{library_data.name}' library...")

    def after_library_nodes_loaded(self, library_data: LibrarySchema, library: Library):
        """Called after all nodes have been loaded from the library."""
        GriptapeNodes.LibraryManager().on_register_event_handler(
            request_type=PublishWorkflowRequest,
            handler=_publish_workflow_request_handler,
            library_data=library_data,
        )
