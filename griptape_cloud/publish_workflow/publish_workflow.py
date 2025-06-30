import logging

from base.base_griptape_cloud_node import BaseGriptapeCloudNode
from griptape.events import BaseEvent, EventBus, EventListener
from griptape_nodes.retained_mode.events.base_events import (
    EventResultSuccess,
    GriptapeNodeEvent,
    GriptapeNodeRequest,
)
from griptape_nodes.retained_mode.events.workflow_events import PublishWorkflowResultSuccess

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def _on_publish_workflow_request(event: BaseEvent) -> None:
    """Handle publish workflow request events."""
    logger.info("Workflow publish started!!!!!!!!!: %s", event)
    logger.info(type(event))
    # wrapped_event = GriptapeNodeEvent(
    #     wrapped_event=EventResultSuccess(result=PublishWorkflowResultSuccess(workflow_id="abc"), request=event)
    # )
    # EventBus.publish_event(event=wrapped_event)


def _register_event_handlers() -> None:
    """Register event handlers with the EventBus."""
    try:
        EventBus.add_event_listener(EventListener(on_event=_on_publish_workflow_request))

        logger.info("Successfully registered workflow publication event handlers")
        logger.info(type(GriptapeNodeRequest))

    except Exception as e:
        logger.warning("Failed to register event handlers: %s", e)


_register_event_handlers()


class PublishWorkflow(BaseGriptapeCloudNode):
    """Node for publishing entire workflows to Griptape Cloud.

    This Node can take a workflow and publish it to a Griptape Cloud Structure.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
