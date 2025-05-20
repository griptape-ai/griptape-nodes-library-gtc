from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_schema_property import JsonSchemaProperty


T = TypeVar("T", bound="JsonSchemaProperties")


@_attrs_define
class JsonSchemaProperties:
    """
    Attributes:
        member (Union[Unset, JsonSchemaProperty]):
    """

    member: Union[Unset, "JsonSchemaProperty"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.member, Unset):
            member = self.member.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member is not UNSET:
            field_dict["member"] = member

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_schema_property import JsonSchemaProperty

        d = dict(src_dict)
        _member = d.pop("member", UNSET)
        member: Union[Unset, JsonSchemaProperty]
        if isinstance(_member, Unset):
            member = UNSET
        else:
            member = JsonSchemaProperty.from_dict(_member)

        json_schema_properties = cls(
            member=member,
        )

        json_schema_properties.additional_properties = d
        return json_schema_properties

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
