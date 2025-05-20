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


T = TypeVar("T", bound="UpdateIntegrationRequestContent")


@_attrs_define
class UpdateIntegrationRequestContent:
    """
    Attributes:
        assistant_ids (Union[Unset, list[str]]):
        config (Union['IntegrationConfigInputUnionType0', 'IntegrationConfigInputUnionType1',
            'IntegrationConfigInputUnionType2', Unset]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        structure_ids (Union[Unset, list[str]]):
        type_ (Union[Unset, IntegrationType]):
    """

    assistant_ids: Union[Unset, list[str]] = UNSET
    config: Union[
        "IntegrationConfigInputUnionType0",
        "IntegrationConfigInputUnionType1",
        "IntegrationConfigInputUnionType2",
        Unset,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    structure_ids: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, IntegrationType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.integration_config_input_union_type_0 import IntegrationConfigInputUnionType0
        from ..models.integration_config_input_union_type_1 import IntegrationConfigInputUnionType1

        assistant_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assistant_ids, Unset):
            assistant_ids = self.assistant_ids

        config: Union[Unset, dict[str, Any]]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, IntegrationConfigInputUnionType0):
            config = self.config.to_dict()
        elif isinstance(self.config, IntegrationConfigInputUnionType1):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        description = self.description

        name = self.name

        structure_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.structure_ids, Unset):
            structure_ids = self.structure_ids

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assistant_ids is not UNSET:
            field_dict["assistant_ids"] = assistant_ids
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if structure_ids is not UNSET:
            field_dict["structure_ids"] = structure_ids
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_config_input_union_type_0 import IntegrationConfigInputUnionType0
        from ..models.integration_config_input_union_type_1 import IntegrationConfigInputUnionType1
        from ..models.integration_config_input_union_type_2 import IntegrationConfigInputUnionType2

        d = dict(src_dict)
        assistant_ids = cast(list[str], d.pop("assistant_ids", UNSET))

        def _parse_config(
            data: object,
        ) -> Union[
            "IntegrationConfigInputUnionType0",
            "IntegrationConfigInputUnionType1",
            "IntegrationConfigInputUnionType2",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
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

        config = _parse_config(d.pop("config", UNSET))

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        structure_ids = cast(list[str], d.pop("structure_ids", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, IntegrationType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IntegrationType(_type_)

        update_integration_request_content = cls(
            assistant_ids=assistant_ids,
            config=config,
            description=description,
            name=name,
            structure_ids=structure_ids,
            type_=type_,
        )

        update_integration_request_content.additional_properties = d
        return update_integration_request_content

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
