from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GitHubAppDetail")


@_attrs_define
class GitHubAppDetail:
    """
    Attributes:
        app_id (str):
        integration_endpoint (str):
        private_key_secret_ref (str):
        webhook_secret_ref (str):
    """

    app_id: str
    integration_endpoint: str
    private_key_secret_ref: str
    webhook_secret_ref: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        integration_endpoint = self.integration_endpoint

        private_key_secret_ref = self.private_key_secret_ref

        webhook_secret_ref = self.webhook_secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "integration_endpoint": integration_endpoint,
                "private_key_secret_ref": private_key_secret_ref,
                "webhook_secret_ref": webhook_secret_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("app_id")

        integration_endpoint = d.pop("integration_endpoint")

        private_key_secret_ref = d.pop("private_key_secret_ref")

        webhook_secret_ref = d.pop("webhook_secret_ref")

        git_hub_app_detail = cls(
            app_id=app_id,
            integration_endpoint=integration_endpoint,
            private_key_secret_ref=private_key_secret_ref,
            webhook_secret_ref=webhook_secret_ref,
        )

        git_hub_app_detail.additional_properties = d
        return git_hub_app_detail

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
