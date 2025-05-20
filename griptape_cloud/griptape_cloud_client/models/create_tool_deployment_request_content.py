from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_source_input_type_0 import CodeSourceInputType0


T = TypeVar("T", bound="CreateToolDeploymentRequestContent")


@_attrs_define
class CreateToolDeploymentRequestContent:
    """
    Attributes:
        code_source (Union['CodeSourceInputType0', Unset]):
        force (Union[Unset, bool]):
    """

    code_source: Union["CodeSourceInputType0", Unset] = UNSET
    force: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code_source: Union[Unset, dict[str, Any]]
        if isinstance(self.code_source, Unset):
            code_source = UNSET
        else:
            code_source = self.code_source.to_dict()

        force = self.force

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code_source is not UNSET:
            field_dict["code_source"] = code_source
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_source_input_type_0 import CodeSourceInputType0

        d = dict(src_dict)

        def _parse_code_source(data: object) -> Union["CodeSourceInputType0", Unset]:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_code_source_input_type_0 = CodeSourceInputType0.from_dict(data)

            return componentsschemas_code_source_input_type_0

        code_source = _parse_code_source(d.pop("code_source", UNSET))

        force = d.pop("force", UNSET)

        create_tool_deployment_request_content = cls(
            code_source=code_source,
            force=force,
        )

        create_tool_deployment_request_content.additional_properties = d
        return create_tool_deployment_request_content

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
