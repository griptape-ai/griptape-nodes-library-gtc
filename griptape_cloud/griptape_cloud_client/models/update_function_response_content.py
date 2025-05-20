import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env_var import EnvVar
    from ..models.function_code_type_0 import FunctionCodeType0
    from ..models.function_code_type_1 import FunctionCodeType1
    from ..models.function_code_type_2 import FunctionCodeType2


T = TypeVar("T", bound="UpdateFunctionResponseContent")


@_attrs_define
class UpdateFunctionResponseContent:
    """
    Attributes:
        code (Union['FunctionCodeType0', 'FunctionCodeType1', 'FunctionCodeType2']):
        created_at (datetime.datetime):
        created_by (str):
        description (str):
        env_vars (list['EnvVar']):
        function_id (str):
        latest_deployment_id (str):
        name (str):
        organization_id (str):
        updated_at (datetime.datetime):
        function_config_file (Union[Unset, str]):
    """

    code: Union["FunctionCodeType0", "FunctionCodeType1", "FunctionCodeType2"]
    created_at: datetime.datetime
    created_by: str
    description: str
    env_vars: list["EnvVar"]
    function_id: str
    latest_deployment_id: str
    name: str
    organization_id: str
    updated_at: datetime.datetime
    function_config_file: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.function_code_type_0 import FunctionCodeType0
        from ..models.function_code_type_1 import FunctionCodeType1

        code: dict[str, Any]
        if isinstance(self.code, FunctionCodeType0):
            code = self.code.to_dict()
        elif isinstance(self.code, FunctionCodeType1):
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

        function_id = self.function_id

        latest_deployment_id = self.latest_deployment_id

        name = self.name

        organization_id = self.organization_id

        updated_at = self.updated_at.isoformat()

        function_config_file = self.function_config_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "env_vars": env_vars,
                "function_id": function_id,
                "latest_deployment_id": latest_deployment_id,
                "name": name,
                "organization_id": organization_id,
                "updated_at": updated_at,
            }
        )
        if function_config_file is not UNSET:
            field_dict["function_config_file"] = function_config_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.env_var import EnvVar
        from ..models.function_code_type_0 import FunctionCodeType0
        from ..models.function_code_type_1 import FunctionCodeType1
        from ..models.function_code_type_2 import FunctionCodeType2

        d = dict(src_dict)

        def _parse_code(data: object) -> Union["FunctionCodeType0", "FunctionCodeType1", "FunctionCodeType2"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_function_code_type_0 = FunctionCodeType0.from_dict(data)

                return componentsschemas_function_code_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_function_code_type_1 = FunctionCodeType1.from_dict(data)

                return componentsschemas_function_code_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_function_code_type_2 = FunctionCodeType2.from_dict(data)

            return componentsschemas_function_code_type_2

        code = _parse_code(d.pop("code"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        description = d.pop("description")

        env_vars = []
        _env_vars = d.pop("env_vars")
        for env_vars_item_data in _env_vars:
            env_vars_item = EnvVar.from_dict(env_vars_item_data)

            env_vars.append(env_vars_item)

        function_id = d.pop("function_id")

        latest_deployment_id = d.pop("latest_deployment_id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        updated_at = isoparse(d.pop("updated_at"))

        function_config_file = d.pop("function_config_file", UNSET)

        update_function_response_content = cls(
            code=code,
            created_at=created_at,
            created_by=created_by,
            description=description,
            env_vars=env_vars,
            function_id=function_id,
            latest_deployment_id=latest_deployment_id,
            name=name,
            organization_id=organization_id,
            updated_at=updated_at,
            function_config_file=function_config_file,
        )

        update_function_response_content.additional_properties = d
        return update_function_response_content

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
