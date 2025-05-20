from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookDetail")


@_attrs_define
class WebhookDetail:
    """
    Attributes:
        disable_api_key_param (bool):
        integration_endpoint (str):
    """

    disable_api_key_param: bool
    integration_endpoint: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable_api_key_param = self.disable_api_key_param

        integration_endpoint = self.integration_endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disable_api_key_param": disable_api_key_param,
                "integration_endpoint": integration_endpoint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disable_api_key_param = d.pop("disable_api_key_param")

        integration_endpoint = d.pop("integration_endpoint")

        webhook_detail = cls(
            disable_api_key_param=disable_api_key_param,
            integration_endpoint=integration_endpoint,
        )

        webhook_detail.additional_properties = d
        return webhook_detail

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
