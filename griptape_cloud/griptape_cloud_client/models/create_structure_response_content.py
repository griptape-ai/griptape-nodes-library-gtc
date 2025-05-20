import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env_var import EnvVar
    from ..models.structure_code_type_0 import StructureCodeType0
    from ..models.structure_code_type_1 import StructureCodeType1
    from ..models.structure_code_type_2 import StructureCodeType2


T = TypeVar("T", bound="CreateStructureResponseContent")


@_attrs_define
class CreateStructureResponseContent:
    """
    Attributes:
        code (Union['StructureCodeType0', 'StructureCodeType1', 'StructureCodeType2']):
        created_at (datetime.datetime):
        created_by (str):
        description (str):
        env_vars (list['EnvVar']):
        latest_deployment_id (str):
        name (str):
        organization_id (str):
        structure_id (str):
        updated_at (datetime.datetime):
        webhook_enabled (bool):
        structure_config_file (Union[Unset, str]):
    """

    code: Union["StructureCodeType0", "StructureCodeType1", "StructureCodeType2"]
    created_at: datetime.datetime
    created_by: str
    description: str
    env_vars: list["EnvVar"]
    latest_deployment_id: str
    name: str
    organization_id: str
    structure_id: str
    updated_at: datetime.datetime
    webhook_enabled: bool
    structure_config_file: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.structure_code_type_0 import StructureCodeType0
        from ..models.structure_code_type_1 import StructureCodeType1

        code: dict[str, Any]
        if isinstance(self.code, StructureCodeType0):
            code = self.code.to_dict()
        elif isinstance(self.code, StructureCodeType1):
            code = self.code.to_dict()
        else:
            code = self.code.to_dict()

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        description = self.description

        env_vars = []
        for env_vars_item_data in self.env_vars:
            env_vars_item = env_vars_item_data.to_dict()
            env_vars.append(env_vars_item)

        latest_deployment_id = self.latest_deployment_id

        name = self.name

        organization_id = self.organization_id

        structure_id = self.structure_id

        updated_at = self.updated_at.isoformat()

        webhook_enabled = self.webhook_enabled

        structure_config_file = self.structure_config_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "env_vars": env_vars,
                "latest_deployment_id": latest_deployment_id,
                "name": name,
                "organization_id": organization_id,
                "structure_id": structure_id,
                "updated_at": updated_at,
                "webhook_enabled": webhook_enabled,
            }
        )
        if structure_config_file is not UNSET:
            field_dict["structure_config_file"] = structure_config_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.env_var import EnvVar
        from ..models.structure_code_type_0 import StructureCodeType0
        from ..models.structure_code_type_1 import StructureCodeType1
        from ..models.structure_code_type_2 import StructureCodeType2

        d = dict(src_dict)

        def _parse_code(data: object) -> Union["StructureCodeType0", "StructureCodeType1", "StructureCodeType2"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_structure_code_type_0 = StructureCodeType0.from_dict(data)

                return componentsschemas_structure_code_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_structure_code_type_1 = StructureCodeType1.from_dict(data)

                return componentsschemas_structure_code_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_structure_code_type_2 = StructureCodeType2.from_dict(data)

            return componentsschemas_structure_code_type_2

        code = _parse_code(d.pop("code"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        description = d.pop("description")

        env_vars = []
        _env_vars = d.pop("env_vars")
        for env_vars_item_data in _env_vars:
            env_vars_item = EnvVar.from_dict(env_vars_item_data)

            env_vars.append(env_vars_item)

        latest_deployment_id = d.pop("latest_deployment_id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        structure_id = d.pop("structure_id")

        updated_at = isoparse(d.pop("updated_at"))

        webhook_enabled = d.pop("webhook_enabled")

        structure_config_file = d.pop("structure_config_file", UNSET)

        create_structure_response_content = cls(
            code=code,
            created_at=created_at,
            created_by=created_by,
            description=description,
            env_vars=env_vars,
            latest_deployment_id=latest_deployment_id,
            name=name,
            organization_id=organization_id,
            structure_id=structure_id,
            updated_at=updated_at,
            webhook_enabled=webhook_enabled,
            structure_config_file=structure_config_file,
        )

        create_structure_response_content.additional_properties = d
        return create_structure_response_content

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
