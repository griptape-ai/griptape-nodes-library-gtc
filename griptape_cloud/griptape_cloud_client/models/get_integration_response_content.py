import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.integration_type import IntegrationType

if TYPE_CHECKING:
    from ..models.integration_config_union_type_0 import IntegrationConfigUnionType0
    from ..models.integration_config_union_type_1 import IntegrationConfigUnionType1
    from ..models.integration_config_union_type_2 import IntegrationConfigUnionType2


T = TypeVar("T", bound="GetIntegrationResponseContent")


@_attrs_define
class GetIntegrationResponseContent:
    """
    Attributes:
        assistant_ids (list[str]):
        config (Union['IntegrationConfigUnionType0', 'IntegrationConfigUnionType1', 'IntegrationConfigUnionType2']):
        created_at (datetime.datetime):
        created_by (str):
        description (str):
        integration_id (str):
        name (str):
        organization_id (str):
        structure_ids (list[str]):
        type_ (IntegrationType):
        updated_at (datetime.datetime):
    """

    assistant_ids: list[str]
    config: Union["IntegrationConfigUnionType0", "IntegrationConfigUnionType1", "IntegrationConfigUnionType2"]
    created_at: datetime.datetime
    created_by: str
    description: str
    integration_id: str
    name: str
    organization_id: str
    structure_ids: list[str]
    type_: IntegrationType
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.integration_config_union_type_0 import IntegrationConfigUnionType0
        from ..models.integration_config_union_type_1 import IntegrationConfigUnionType1

        assistant_ids = self.assistant_ids

        config: dict[str, Any]
        if isinstance(self.config, IntegrationConfigUnionType0):
            config = self.config.to_dict()
        elif isinstance(self.config, IntegrationConfigUnionType1):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        description = self.description

        integration_id = self.integration_id

        name = self.name

        organization_id = self.organization_id

        structure_ids = self.structure_ids

        type_ = self.type_.value

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistant_ids": assistant_ids,
                "config": config,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "integration_id": integration_id,
                "name": name,
                "organization_id": organization_id,
                "structure_ids": structure_ids,
                "type": type_,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_config_union_type_0 import IntegrationConfigUnionType0
        from ..models.integration_config_union_type_1 import IntegrationConfigUnionType1
        from ..models.integration_config_union_type_2 import IntegrationConfigUnionType2

        d = dict(src_dict)
        assistant_ids = cast(list[str], d.pop("assistant_ids"))

        def _parse_config(
            data: object,
        ) -> Union["IntegrationConfigUnionType0", "IntegrationConfigUnionType1", "IntegrationConfigUnionType2"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_integration_config_union_type_0 = IntegrationConfigUnionType0.from_dict(data)

                return componentsschemas_integration_config_union_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_integration_config_union_type_1 = IntegrationConfigUnionType1.from_dict(data)

                return componentsschemas_integration_config_union_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_integration_config_union_type_2 = IntegrationConfigUnionType2.from_dict(data)

            return componentsschemas_integration_config_union_type_2

        config = _parse_config(d.pop("config"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        description = d.pop("description")

        integration_id = d.pop("integration_id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        structure_ids = cast(list[str], d.pop("structure_ids"))

        type_ = IntegrationType(d.pop("type"))

        updated_at = isoparse(d.pop("updated_at"))

        get_integration_response_content = cls(
            assistant_ids=assistant_ids,
            config=config,
            created_at=created_at,
            created_by=created_by,
            description=description,
            integration_id=integration_id,
            name=name,
            organization_id=organization_id,
            structure_ids=structure_ids,
            type_=type_,
            updated_at=updated_at,
        )

        get_integration_response_content.additional_properties = d
        return get_integration_response_content

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
