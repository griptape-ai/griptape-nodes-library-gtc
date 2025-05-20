from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_connector_config_input_union_type_0 import DataConnectorConfigInputUnionType0
    from ..models.data_connector_config_input_union_type_1 import DataConnectorConfigInputUnionType1
    from ..models.data_connector_config_input_union_type_2 import DataConnectorConfigInputUnionType2
    from ..models.data_connector_config_input_union_type_3 import DataConnectorConfigInputUnionType3
    from ..models.data_connector_config_input_union_type_4 import DataConnectorConfigInputUnionType4
    from ..models.data_connector_config_input_union_type_5 import DataConnectorConfigInputUnionType5


T = TypeVar("T", bound="UpdateDataConnectorRequestContent")


@_attrs_define
class UpdateDataConnectorRequestContent:
    """
    Attributes:
        config (Union['DataConnectorConfigInputUnionType0', 'DataConnectorConfigInputUnionType1',
            'DataConnectorConfigInputUnionType2', 'DataConnectorConfigInputUnionType3',
            'DataConnectorConfigInputUnionType4', 'DataConnectorConfigInputUnionType5', Unset]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        schedule_expression (Union[Unset, str]):
    """

    config: Union[
        "DataConnectorConfigInputUnionType0",
        "DataConnectorConfigInputUnionType1",
        "DataConnectorConfigInputUnionType2",
        "DataConnectorConfigInputUnionType3",
        "DataConnectorConfigInputUnionType4",
        "DataConnectorConfigInputUnionType5",
        Unset,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    schedule_expression: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.data_connector_config_input_union_type_0 import DataConnectorConfigInputUnionType0
        from ..models.data_connector_config_input_union_type_1 import DataConnectorConfigInputUnionType1
        from ..models.data_connector_config_input_union_type_2 import DataConnectorConfigInputUnionType2
        from ..models.data_connector_config_input_union_type_3 import DataConnectorConfigInputUnionType3
        from ..models.data_connector_config_input_union_type_4 import DataConnectorConfigInputUnionType4

        config: Union[Unset, dict[str, Any]]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, DataConnectorConfigInputUnionType0):
            config = self.config.to_dict()
        elif isinstance(self.config, DataConnectorConfigInputUnionType1):
            config = self.config.to_dict()
        elif isinstance(self.config, DataConnectorConfigInputUnionType2):
            config = self.config.to_dict()
        elif isinstance(self.config, DataConnectorConfigInputUnionType3):
            config = self.config.to_dict()
        elif isinstance(self.config, DataConnectorConfigInputUnionType4):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        description = self.description

        name = self.name

        schedule_expression = self.schedule_expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if schedule_expression is not UNSET:
            field_dict["schedule_expression"] = schedule_expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_connector_config_input_union_type_0 import DataConnectorConfigInputUnionType0
        from ..models.data_connector_config_input_union_type_1 import DataConnectorConfigInputUnionType1
        from ..models.data_connector_config_input_union_type_2 import DataConnectorConfigInputUnionType2
        from ..models.data_connector_config_input_union_type_3 import DataConnectorConfigInputUnionType3
        from ..models.data_connector_config_input_union_type_4 import DataConnectorConfigInputUnionType4
        from ..models.data_connector_config_input_union_type_5 import DataConnectorConfigInputUnionType5

        d = dict(src_dict)

        def _parse_config(
            data: object,
        ) -> Union[
            "DataConnectorConfigInputUnionType0",
            "DataConnectorConfigInputUnionType1",
            "DataConnectorConfigInputUnionType2",
            "DataConnectorConfigInputUnionType3",
            "DataConnectorConfigInputUnionType4",
            "DataConnectorConfigInputUnionType5",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_input_union_type_0 = (
                    DataConnectorConfigInputUnionType0.from_dict(data)
                )

                return componentsschemas_data_connector_config_input_union_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_input_union_type_1 = (
                    DataConnectorConfigInputUnionType1.from_dict(data)
                )

                return componentsschemas_data_connector_config_input_union_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_input_union_type_2 = (
                    DataConnectorConfigInputUnionType2.from_dict(data)
                )

                return componentsschemas_data_connector_config_input_union_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_input_union_type_3 = (
                    DataConnectorConfigInputUnionType3.from_dict(data)
                )

                return componentsschemas_data_connector_config_input_union_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_input_union_type_4 = (
                    DataConnectorConfigInputUnionType4.from_dict(data)
                )

                return componentsschemas_data_connector_config_input_union_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_data_connector_config_input_union_type_5 = DataConnectorConfigInputUnionType5.from_dict(
                data
            )

            return componentsschemas_data_connector_config_input_union_type_5

        config = _parse_config(d.pop("config", UNSET))

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        schedule_expression = d.pop("schedule_expression", UNSET)

        update_data_connector_request_content = cls(
            config=config,
            description=description,
            name=name,
            schedule_expression=schedule_expression,
        )

        update_data_connector_request_content.additional_properties = d
        return update_data_connector_request_content

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
