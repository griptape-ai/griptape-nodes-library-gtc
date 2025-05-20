from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.default_structure_code import DefaultStructureCode


T = TypeVar("T", bound="StructureCodeType2")


@_attrs_define
class StructureCodeType2:
    """
    Attributes:
        default (DefaultStructureCode):
    """

    default: "DefaultStructureCode"
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
        from ..models.default_structure_code import DefaultStructureCode

        d = dict(src_dict)
        default = DefaultStructureCode.from_dict(d.pop("default"))

        structure_code_type_2 = cls(
            default=default,
        )

        structure_code_type_2.additional_properties = d
        return structure_code_type_2

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
