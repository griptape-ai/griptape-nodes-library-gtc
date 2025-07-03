from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceErrorResponseContent")


@_attrs_define
class ServiceErrorResponseContent:
    """
    Attributes:
        errors (Union[Unset, list[Any]]):
        type_ (Union[Unset, str]):
    """

    errors: Union[Unset, list[Any]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        errors = cast(list[Any], d.pop("errors", UNSET))

        type_ = d.pop("type", UNSET)

        service_error_response_content = cls(
            errors=errors,
            type_=type_,
        )

        service_error_response_content.additional_properties = d
        return service_error_response_content

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
