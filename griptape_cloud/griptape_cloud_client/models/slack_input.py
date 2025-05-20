from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlackInput")


@_attrs_define
class SlackInput:
    """
    Attributes:
        app_description (str):
        app_display_name (str):
        app_name (str):
        bot_token_secret_ref (Union[Unset, str]):
        signing_secret_secret_ref (Union[Unset, str]):
    """

    app_description: str
    app_display_name: str
    app_name: str
    bot_token_secret_ref: Union[Unset, str] = UNSET
    signing_secret_secret_ref: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_description = self.app_description

        app_display_name = self.app_display_name

        app_name = self.app_name

        bot_token_secret_ref = self.bot_token_secret_ref

        signing_secret_secret_ref = self.signing_secret_secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_description": app_description,
                "app_display_name": app_display_name,
                "app_name": app_name,
            }
        )
        if bot_token_secret_ref is not UNSET:
            field_dict["bot_token_secret_ref"] = bot_token_secret_ref
        if signing_secret_secret_ref is not UNSET:
            field_dict["signing_secret_secret_ref"] = signing_secret_secret_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_description = d.pop("app_description")

        app_display_name = d.pop("app_display_name")

        app_name = d.pop("app_name")

        bot_token_secret_ref = d.pop("bot_token_secret_ref", UNSET)

        signing_secret_secret_ref = d.pop("signing_secret_secret_ref", UNSET)

        slack_input = cls(
            app_description=app_description,
            app_display_name=app_display_name,
            app_name=app_name,
            bot_token_secret_ref=bot_token_secret_ref,
            signing_secret_secret_ref=signing_secret_secret_ref,
        )

        slack_input.additional_properties = d
        return slack_input

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
