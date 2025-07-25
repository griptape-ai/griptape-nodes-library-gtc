import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetSecretResponseContent")


@_attrs_define
class GetSecretResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        last_used (datetime.datetime):
        name (str):
        organization_id (str):
        secret_id (str):
        updated_at (datetime.datetime):
    """

    created_at: datetime.datetime
    last_used: datetime.datetime
    name: str
    organization_id: str
    secret_id: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        last_used = self.last_used.isoformat()

        name = self.name

        organization_id = self.organization_id

        secret_id = self.secret_id

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "last_used": last_used,
                "name": name,
                "organization_id": organization_id,
                "secret_id": secret_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        last_used = isoparse(d.pop("last_used"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        secret_id = d.pop("secret_id")

        updated_at = isoparse(d.pop("updated_at"))

        get_secret_response_content = cls(
            created_at=created_at,
            last_used=last_used,
            name=name,
            organization_id=organization_id,
            secret_id=secret_id,
            updated_at=updated_at,
        )

        get_secret_response_content.additional_properties = d
        return get_secret_response_content

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
