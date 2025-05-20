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
    from ..models.transform_input import TransformInput


T = TypeVar("T", bound="CreateDataConnectorRequestContent")


@_attrs_define
class CreateDataConnectorRequestContent:
    """
    Attributes:
        config (Union['DataConnectorConfigInputUnionType0', 'DataConnectorConfigInputUnionType1',
            'DataConnectorConfigInputUnionType2', 'DataConnectorConfigInputUnionType3',
            'DataConnectorConfigInputUnionType4', 'DataConnectorConfigInputUnionType5']):
        name (str):
        type_ (str):
        description (Union[Unset, str]):
        schedule_expression (Union[Unset, str]):
        transforms (Union[Unset, list['TransformInput']]):
    """

    config: Union[
        "DataConnectorConfigInputUnionType0",
        "DataConnectorConfigInputUnionType1",
        "DataConnectorConfigInputUnionType2",
        "DataConnectorConfigInputUnionType3",
        "DataConnectorConfigInputUnionType4",
        "DataConnectorConfigInputUnionType5",
    ]
    name: str
    type_: str
    description: Union[Unset, str] = UNSET
    schedule_expression: Union[Unset, str] = UNSET
    transforms: Union[Unset, list["TransformInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.data_connector_config_input_union_type_0 import DataConnectorConfigInputUnionType0
        from ..models.data_connector_config_input_union_type_1 import DataConnectorConfigInputUnionType1
        from ..models.data_connector_config_input_union_type_2 import DataConnectorConfigInputUnionType2
        from ..models.data_connector_config_input_union_type_3 import DataConnectorConfigInputUnionType3
        from ..models.data_connector_config_input_union_type_4 import DataConnectorConfigInputUnionType4

        config: dict[str, Any]
        if isinstance(self.config, DataConnectorConfigInputUnionType0):
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

        name = self.name

        type_ = self.type_

        description = self.description

        schedule_expression = self.schedule_expression

        transforms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transforms, Unset):
            transforms = []
            for transforms_item_data in self.transforms:
                transforms_item = transforms_item_data.to_dict()
                transforms.append(transforms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "name": name,
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if schedule_expression is not UNSET:
            field_dict["schedule_expression"] = schedule_expression
        if transforms is not UNSET:
            field_dict["transforms"] = transforms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_connector_config_input_union_type_0 import DataConnectorConfigInputUnionType0
        from ..models.data_connector_config_input_union_type_1 import DataConnectorConfigInputUnionType1
        from ..models.data_connector_config_input_union_type_2 import DataConnectorConfigInputUnionType2
        from ..models.data_connector_config_input_union_type_3 import DataConnectorConfigInputUnionType3
        from ..models.data_connector_config_input_union_type_4 import DataConnectorConfigInputUnionType4
        from ..models.data_connector_config_input_union_type_5 import DataConnectorConfigInputUnionType5
        from ..models.transform_input import TransformInput

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
        ]:
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

        config = _parse_config(d.pop("config"))

        name = d.pop("name")

        type_ = d.pop("type")

        description = d.pop("description", UNSET)

        schedule_expression = d.pop("schedule_expression", UNSET)

        transforms = []
        _transforms = d.pop("transforms", UNSET)
        for transforms_item_data in _transforms or []:
            transforms_item = TransformInput.from_dict(transforms_item_data)

            transforms.append(transforms_item)

        create_data_connector_request_content = cls(
            config=config,
            name=name,
            type_=type_,
            description=description,
            schedule_expression=schedule_expression,
            transforms=transforms,
        )

        create_data_connector_request_content.additional_properties = d
        return create_data_connector_request_content

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
