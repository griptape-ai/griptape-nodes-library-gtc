import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ApiKeyDetail")


@_attrs_define
class ApiKeyDetail:
    """
    Attributes:
        active (bool):
        api_key_id (str):
        created_at (datetime.datetime):
        created_by (str):
        last_used (datetime.datetime):
        name (str):
        organization_id (str):
        updated_at (datetime.datetime):
    """

    active: bool
    api_key_id: str
    created_at: datetime.datetime
    created_by: str
    last_used: datetime.datetime
    name: str
    organization_id: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        api_key_id = self.api_key_id

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        last_used = self.last_used.isoformat()

        name = self.name

        organization_id = self.organization_id

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "api_key_id": api_key_id,
                "created_at": created_at,
                "created_by": created_by,
                "last_used": last_used,
                "name": name,
                "organization_id": organization_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        api_key_id = d.pop("api_key_id")

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        last_used = isoparse(d.pop("last_used"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        updated_at = isoparse(d.pop("updated_at"))

        api_key_detail = cls(
            active=active,
            api_key_id=api_key_id,
            created_at=created_at,
            created_by=created_by,
            last_used=last_used,
            name=name,
            organization_id=organization_id,
            updated_at=updated_at,
        )

        api_key_detail.additional_properties = d
        return api_key_detail

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
