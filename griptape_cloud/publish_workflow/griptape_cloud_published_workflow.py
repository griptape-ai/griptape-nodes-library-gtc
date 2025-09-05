import contextlib
import json
import logging
from typing import Any

from griptape_cloud_client.models.deployment_status import DeploymentStatus
from griptape_cloud_client.types import Unset
from griptape_nodes.exe_types.core_types import Parameter, ParameterGroup, ParameterMode
from griptape_nodes.exe_types.node_types import AsyncResult, ControlNode
from structures.base_structure_node import BaseStructureNode

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class GriptapeCloudPublishedWorkflow(BaseStructureNode, ControlNode):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        metadata = kwargs.get("metadata", {})

        # Store workflow shape and structure info
        self.workflow_shape = metadata.get("workflow_shape", {})
        self.structure_id = metadata.get("structure_id")
        self.structure_name = metadata.get("structure_name", "Published Workflow")

        # Add basic structure information parameters
        with ParameterGroup(name="Griptape Cloud Structure Details") as structure_details_group:
            Parameter(
                name="name",
                input_types=["str"],
                type="str",
                output_type="str",
                default_value=self.structure_name,
                tooltip="The name of the published workflow structure",
                allowed_modes={ParameterMode.OUTPUT},
            )

            Parameter(
                name="structure_id",
                input_types=["str"],
                type="str",
                output_type="str",
                default_value=self.structure_id,
                tooltip="The structure ID of the published workflow",
                allowed_modes={ParameterMode.OUTPUT},
            )

            Parameter(
                name="structure_run_id",
                input_types=["str"],
                output_type="str",
                type="str",
                default_value=None,
                tooltip="The ID of the structure run",
                allowed_modes={ParameterMode.OUTPUT},
            )

        structure_details_group.ui_options = {"hide": False, "collapsed": True}
        self.add_node_element(structure_details_group)

        # Add events group
        with ParameterGroup(name="Events") as events_group:
            Parameter(name="include_events", type="bool", default_value=False, tooltip="Include events details.")

            Parameter(
                name="events",
                type="str",
                tooltip="Displays processing events if enabled.",
                ui_options={"multiline": True, "placeholder_text": "Events"},
                allowed_modes={ParameterMode.OUTPUT},
            )
        events_group.ui_options = {"hide": False, "collapsed": True}
        self.add_node_element(events_group)

    def validate_before_workflow_run(self) -> list[Exception] | None:
        exceptions = super().validate_before_workflow_run() or []

        try:
            if not self.get_parameter_value("structure_id"):
                msg = "Structure ID is not set. Configure the Node with a valid Griptape Cloud Structure ID before running."
                exceptions.append(ValueError(msg))

            structure_id = self.get_parameter_value("structure_id")

            list_structure_deployments_response = self._list_structure_deployments(
                structure_id=structure_id, status=[DeploymentStatus.SUCCEEDED]
            )
            if not any(
                self._is_deployment_ready(deployment) for deployment in list_structure_deployments_response.deployments
            ):
                msg = f"Structure '{structure_id}' is not ready to run! Ensure it has a successful deployment."
                exceptions.append(ValueError(msg))

        except Exception as e:
            # Add any exceptions to your list to return
            exceptions.append(e)

        # if there are exceptions, they will display when the user tries to run the flow with the node.
        return exceptions if exceptions else None

    def _process(self) -> None:
        include_events = self.get_parameter_value("include_events")

        # Collect input parameters and construct JSON for structure run
        input_json = self._collect_input_parameters()

        # Create args list with -i flag and JSON string
        args = ["-i", json.dumps(input_json)]

        # Create and run the structure
        structure_run = self._create_structure_run(structure_id=self.structure_id, args=args)

        # Poll for events if requested
        for events in self._poll_structure_run_events(structure_run_id=structure_run.structure_run_id):
            if include_events:
                self.append_value_to_parameter("events", "\n".join(str(event.payload) for event in events))

        # Get the final structure run result
        structure_run = self._get_structure_run(structure_run_id=structure_run.structure_run_id)
        output = structure_run.output if not isinstance(structure_run.output, Unset) else None

        if isinstance(output, dict) and "value" in output:
            with contextlib.suppress(json.JSONDecodeError):
                # Attempt to parse the output value as JSON
                output = json.loads(output["value"])

        # Set the structure run ID output parameter
        self.parameter_output_values["structure_run_id"] = structure_run.structure_run_id

        # Map output to output parameters
        self._map_output_parameters(output)

    def _collect_input_parameters(self) -> dict[str, dict[str, Any]]:
        """Collect input parameters and structure them for the published workflow."""
        input_json = {}

        if "input" not in self.workflow_shape:
            return input_json

        for node_name, node_params in self.workflow_shape["input"].items():
            if isinstance(node_params, dict):
                node_inputs = {}
                for param_name in node_params:
                    param_value = self.get_parameter_value(param_name)

                    if param_value is not None:
                        node_inputs[param_name] = param_value

                if node_inputs:
                    input_json[node_name] = node_inputs

        return input_json

    def _map_output_parameters(self, structure_output: dict[str, Any] | None) -> None:
        """Map structure output to output parameters."""
        if not structure_output or "output" not in self.workflow_shape:
            return

        logger.warning(
            "Mapping output parameters for structure '%s' with output: %s", self.structure_id, structure_output
        )

        for node_name, node_params in self.workflow_shape["output"].items():
            logger.warning("Processing node '%s' with parameters: %s", node_name, node_params)
            if isinstance(node_params, dict) and node_name in structure_output:
                node_outputs = structure_output[node_name]
                logger.warning("Node '%s' outputs: %s", node_name, node_outputs)
                if isinstance(node_outputs, dict):
                    for param_name in node_params:
                        logger.warning("Checking parameter '%s' in node '%s'", param_name, node_name)
                        # Check if this parameter exists in the output
                        if param_name in node_outputs:
                            param_value = node_outputs[param_name]
                            logger.warning("Found output parameter '%s' with value: %s", param_name, param_value)

                            # Set the output parameter value
                            self.set_parameter_value(
                                param_name=param_name,
                                value=param_value,
                            )
                            self.parameter_output_values[param_name] = param_value
                            logger.info("Set output parameter %s = %s", param_name, param_value)

    def process(
        self,
    ) -> AsyncResult[None]:
        yield lambda: self._process()
