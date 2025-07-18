from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfluenceInput")


@_attrs_define
class ConfluenceInput:
    """
    Attributes:
        atlassian_api_token (str):
        atlassian_email (str):
        domain (str):
    """

    atlassian_api_token: str
    atlassian_email: str
    domain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        atlassian_api_token = self.atlassian_api_token

        atlassian_email = self.atlassian_email

        domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "atlassian_api_token": atlassian_api_token,
                "atlassian_email": atlassian_email,
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        atlassian_api_token = d.pop("atlassian_api_token")

        atlassian_email = d.pop("atlassian_email")

        domain = d.pop("domain")

        confluence_input = cls(
            atlassian_api_token=atlassian_api_token,
            atlassian_email=atlassian_email,
            domain=domain,
        )

        confluence_input.additional_properties = d
        return confluence_input

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
