import argparse
import json
import logging
from pathlib import Path

from dotenv import load_dotenv

LIBRARIES = ["REPLACE_LIBRARIES"]


logging.basicConfig(
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def _set_libraries(libraries: list[str]) -> None:
    from griptape_nodes.retained_mode.managers.config_manager import ConfigManager

    config_manager = ConfigManager()
    config_manager.set_config_value(
        key="app_events.on_app_initialization_complete.libraries_to_register",
        value=libraries,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        default=None,
        help="The input to the flow",
    )

    args = parser.parse_args()
    flow_input = args.input

    try:
        flow_input = json.loads(flow_input) if flow_input else {}
    except Exception as e:
        msg = f"Error decoding JSON input: {e}"
        logger.info(msg)
        raise

    load_dotenv()
    _set_libraries(LIBRARIES)

    from structure_workflow_executor import StructureWorkflowExecutor
    from workflow import execute_workflow  # type: ignore[attr-defined]

    workflow_file_path = Path(__file__).parent / "workflow.py"
    workflow_runner = StructureWorkflowExecutor()
    execute_workflow(
        input=flow_input,
        storage_backend="gtc",
        workflow_executor=workflow_runner,
    )
