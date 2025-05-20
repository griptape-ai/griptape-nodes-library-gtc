import logging
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from griptape_cloud_client.models.structure_detail import StructureDetail
from griptape_nodes.exe_types.core_types import Parameter
from griptape_nodes.traits.options import Options

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@dataclass(eq=False)
class StructureOptions(Options):
    choices_value_lookup: dict[str, StructureDetail] = field(kw_only=True)

    def converters_for_trait(self) -> list[Callable]:
        def converter(value: Any) -> Any:
            if value not in self.choices:
                msg = f"Selection '{value}' is not in choices. Defaulting to first choice: '{self.choices[0]}'."
                logger.warning(msg)
                value = self.choices[0]
            value = self.choices_value_lookup.get(value, self.choices[0]).structure_id
            msg = f"Converted choice into value: {value}"
            logger.warning(msg)
            return value

        return [converter]

    def validators_for_trait(self) -> list[Callable[[Parameter, Any], Any]]:
        def validator(param: Parameter, value: Any) -> None:
            if value not in [x.structure_id for x in self.choices_value_lookup.values()]:
                msg = f"Attempted to set Parameter '{param.name}' to value '{value}', but that was not one of the available choices."

                def raise_error() -> None:
                    raise ValueError(msg)

                raise_error()

        return [validator]
