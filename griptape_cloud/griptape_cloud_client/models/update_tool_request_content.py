from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env_var import EnvVar
    from ..models.tool_code_type_0 import ToolCodeType0
    from ..models.tool_code_type_1 import ToolCodeType1
    from ..models.tool_code_type_2 import ToolCodeType2


T = TypeVar("T", bound="UpdateToolRequestContent")


@_attrs_define
class UpdateToolRequestContent:
    """
    Attributes:
        code (Union['ToolCodeType0', 'ToolCodeType1', 'ToolCodeType2', Unset]):
        description (Union[Unset, str]):
        env_vars (Union[Unset, list['EnvVar']]):
        name (Union[Unset, str]):
        tool_config_file (Union[Unset, str]):
    """

    code: Union["ToolCodeType0", "ToolCodeType1", "ToolCodeType2", Unset] = UNSET
    description: Union[Unset, str] = UNSET
    env_vars: Union[Unset, list["EnvVar"]] = UNSET
    name: Union[Unset, str] = UNSET
    tool_config_file: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_code_type_0 import ToolCodeType0
        from ..models.tool_code_type_1 import ToolCodeType1

        code: Union[Unset, dict[str, Any]]
        if isinstance(self.code, Unset):
            code = UNSET
        elif isinstance(self.code, ToolCodeType0):
            code = self.code.to_dict()
        elif isinstance(self.code, ToolCodeType1):
            code = self.code.to_dict()
        else:
            code = self.code.to_dict()

        description = self.description

        env_vars: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = []
            for env_vars_item_data in self.env_vars:
                env_vars_item = env_vars_item_data.to_dict()
                env_vars.append(env_vars_item)

        name = self.name

        tool_config_file = self.tool_config_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if name is not UNSET:
            field_dict["name"] = name
        if tool_config_file is not UNSET:
            field_dict["tool_config_file"] = tool_config_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.env_var import EnvVar
        from ..models.tool_code_type_0 import ToolCodeType0
        from ..models.tool_code_type_1 import ToolCodeType1
        from ..models.tool_code_type_2 import ToolCodeType2

        d = dict(src_dict)

        def _parse_code(data: object) -> Union["ToolCodeType0", "ToolCodeType1", "ToolCodeType2", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tool_code_type_0 = ToolCodeType0.from_dict(data)

                return componentsschemas_tool_code_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tool_code_type_1 = ToolCodeType1.from_dict(data)

                return componentsschemas_tool_code_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_tool_code_type_2 = ToolCodeType2.from_dict(data)

            return componentsschemas_tool_code_type_2

        code = _parse_code(d.pop("code", UNSET))

        description = d.pop("description", UNSET)

        env_vars = []
        _env_vars = d.pop("env_vars", UNSET)
        for env_vars_item_data in _env_vars or []:
            env_vars_item = EnvVar.from_dict(env_vars_item_data)

            env_vars.append(env_vars_item)

        name = d.pop("name", UNSET)

        tool_config_file = d.pop("tool_config_file", UNSET)

        update_tool_request_content = cls(
            code=code,
            description=description,
            env_vars=env_vars,
            name=name,
            tool_config_file=tool_config_file,
        )

        update_tool_request_content.additional_properties = d
        return update_tool_request_content

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
