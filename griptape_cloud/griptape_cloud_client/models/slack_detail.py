from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SlackDetail")


@_attrs_define
class SlackDetail:
    """
    Attributes:
        app_description (str):
        app_display_name (str):
        app_manifest (Any):
        app_name (str):
        bot_token_secret_ref (str):
        signing_secret_secret_ref (str):
    """

    app_description: str
    app_display_name: str
    app_manifest: Any
    app_name: str
    bot_token_secret_ref: str
    signing_secret_secret_ref: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_description = self.app_description

        app_display_name = self.app_display_name

        app_manifest = self.app_manifest

        app_name = self.app_name

        bot_token_secret_ref = self.bot_token_secret_ref

        signing_secret_secret_ref = self.signing_secret_secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_description": app_description,
                "app_display_name": app_display_name,
                "app_manifest": app_manifest,
                "app_name": app_name,
                "bot_token_secret_ref": bot_token_secret_ref,
                "signing_secret_secret_ref": signing_secret_secret_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_description = d.pop("app_description")

        app_display_name = d.pop("app_display_name")

        app_manifest = d.pop("app_manifest")

        app_name = d.pop("app_name")

        bot_token_secret_ref = d.pop("bot_token_secret_ref")

        signing_secret_secret_ref = d.pop("signing_secret_secret_ref")

        slack_detail = cls(
            app_description=app_description,
            app_display_name=app_display_name,
            app_manifest=app_manifest,
            app_name=app_name,
            bot_token_secret_ref=bot_token_secret_ref,
            signing_secret_secret_ref=signing_secret_secret_ref,
        )

        slack_detail.additional_properties = d
        return slack_detail

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
