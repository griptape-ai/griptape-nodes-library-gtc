from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHubAppInput")


@_attrs_define
class GitHubAppInput:
    """
    Attributes:
        app_id (Union[Unset, str]):
        private_key_secret_ref (Union[Unset, str]):
        webhook_secret_ref (Union[Unset, str]):
    """

    app_id: Union[Unset, str] = UNSET
    private_key_secret_ref: Union[Unset, str] = UNSET
    webhook_secret_ref: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        private_key_secret_ref = self.private_key_secret_ref

        webhook_secret_ref = self.webhook_secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if private_key_secret_ref is not UNSET:
            field_dict["private_key_secret_ref"] = private_key_secret_ref
        if webhook_secret_ref is not UNSET:
            field_dict["webhook_secret_ref"] = webhook_secret_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        private_key_secret_ref = d.pop("private_key_secret_ref", UNSET)

        webhook_secret_ref = d.pop("webhook_secret_ref", UNSET)

        git_hub_app_input = cls(
            app_id=app_id,
            private_key_secret_ref=private_key_secret_ref,
            webhook_secret_ref=webhook_secret_ref,
        )

        git_hub_app_input.additional_properties = d
        return git_hub_app_input

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
