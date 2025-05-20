import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ConnectionDetail")


@_attrs_define
class ConnectionDetail:
    """
    Attributes:
        connection_id (str):
        created_at (datetime.datetime):
        created_by (str):
        name (str):
        type_ (str):
        updated_at (datetime.datetime):
    """

    connection_id: str
    created_at: datetime.datetime
    created_by: str
    name: str
    type_: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        name = self.name

        type_ = self.type_

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
                "created_at": created_at,
                "created_by": created_by,
                "name": name,
                "type": type_,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        name = d.pop("name")

        type_ = d.pop("type")

        updated_at = isoparse(d.pop("updated_at"))

        connection_detail = cls(
            connection_id=connection_id,
            created_at=created_at,
            created_by=created_by,
            name=name,
            type_=type_,
            updated_at=updated_at,
        )

        connection_detail.additional_properties = d
        return connection_detail

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
