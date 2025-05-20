from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.default_function_code import DefaultFunctionCode


T = TypeVar("T", bound="FunctionCodeType2")


@_attrs_define
class FunctionCodeType2:
    """
    Attributes:
        default (DefaultFunctionCode):
    """

    default: "DefaultFunctionCode"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.default_function_code import DefaultFunctionCode

        d = dict(src_dict)
        default = DefaultFunctionCode.from_dict(d.pop("default"))

        function_code_type_2 = cls(
            default=default,
        )

        function_code_type_2.additional_properties = d
        return function_code_type_2

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
