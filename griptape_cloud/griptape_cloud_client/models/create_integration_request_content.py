from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_type import IntegrationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_config_input_union_type_0 import IntegrationConfigInputUnionType0
    from ..models.integration_config_input_union_type_1 import IntegrationConfigInputUnionType1
    from ..models.integration_config_input_union_type_2 import IntegrationConfigInputUnionType2


T = TypeVar("T", bound="CreateIntegrationRequestContent")


@_attrs_define
class CreateIntegrationRequestContent:
    """
    Attributes:
        config (Union['IntegrationConfigInputUnionType0', 'IntegrationConfigInputUnionType1',
            'IntegrationConfigInputUnionType2']):
        name (str):
        type_ (IntegrationType):
        assistant_ids (Union[Unset, list[str]]):
        description (Union[Unset, str]):
        structure_ids (Union[Unset, list[str]]):
    """

    config: Union[
        "IntegrationConfigInputUnionType0", "IntegrationConfigInputUnionType1", "IntegrationConfigInputUnionType2"
    ]
    name: str
    type_: IntegrationType
    assistant_ids: Union[Unset, list[str]] = UNSET
    description: Union[Unset, str] = UNSET
    structure_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.integration_config_input_union_type_0 import IntegrationConfigInputUnionType0
        from ..models.integration_config_input_union_type_1 import IntegrationConfigInputUnionType1

        config: dict[str, Any]
        if isinstance(self.config, IntegrationConfigInputUnionType0):
            config = self.config.to_dict()
        elif isinstance(self.config, IntegrationConfigInputUnionType1):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        name = self.name

        type_ = self.type_.value

        assistant_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assistant_ids, Unset):
            assistant_ids = self.assistant_ids

        description = self.description

        structure_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.structure_ids, Unset):
            structure_ids = self.structure_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "name": name,
                "type": type_,
            }
        )
        if assistant_ids is not UNSET:
            field_dict["assistant_ids"] = assistant_ids
        if description is not UNSET:
            field_dict["description"] = description
        if structure_ids is not UNSET:
            field_dict["structure_ids"] = structure_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_config_input_union_type_0 import IntegrationConfigInputUnionType0
        from ..models.integration_config_input_union_type_1 import IntegrationConfigInputUnionType1
        from ..models.integration_config_input_union_type_2 import IntegrationConfigInputUnionType2

        d = dict(src_dict)

        def _parse_config(
            data: object,
        ) -> Union[
            "IntegrationConfigInputUnionType0", "IntegrationConfigInputUnionType1", "IntegrationConfigInputUnionType2"
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_integration_config_input_union_type_0 = IntegrationConfigInputUnionType0.from_dict(
                    data
                )

                return componentsschemas_integration_config_input_union_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_integration_config_input_union_type_1 = IntegrationConfigInputUnionType1.from_dict(
                    data
                )

                return componentsschemas_integration_config_input_union_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_integration_config_input_union_type_2 = IntegrationConfigInputUnionType2.from_dict(data)

            return componentsschemas_integration_config_input_union_type_2

        config = _parse_config(d.pop("config"))

        name = d.pop("name")

        type_ = IntegrationType(d.pop("type"))

        assistant_ids = cast(list[str], d.pop("assistant_ids", UNSET))

        description = d.pop("description", UNSET)

        structure_ids = cast(list[str], d.pop("structure_ids", UNSET))

        create_integration_request_content = cls(
            config=config,
            name=name,
            type_=type_,
            assistant_ids=assistant_ids,
            description=description,
            structure_ids=structure_ids,
        )

        create_integration_request_content.additional_properties = d
        return create_integration_request_content

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
