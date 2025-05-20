from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookInput")


@_attrs_define
class WebhookInput:
    """
    Attributes:
        disable_api_key_param (Union[Unset, bool]):
    """

    disable_api_key_param: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable_api_key_param = self.disable_api_key_param

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable_api_key_param is not UNSET:
            field_dict["disable_api_key_param"] = disable_api_key_param

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disable_api_key_param = d.pop("disable_api_key_param", UNSET)

        webhook_input = cls(
            disable_api_key_param=disable_api_key_param,
        )

        webhook_input.additional_properties = d
        return webhook_input

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
