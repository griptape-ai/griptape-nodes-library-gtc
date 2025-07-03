import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDetail")


@_attrs_define
class UserDetail:
    """
    Attributes:
        created_at (datetime.datetime):
        email (str):
        organizations (list[str]):
        updated_at (datetime.datetime):
        user_id (str):
        name (Union[Unset, str]):
    """

    created_at: datetime.datetime
    email: str
    organizations: list[str]
    updated_at: datetime.datetime
    user_id: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        email = self.email

        organizations = self.organizations

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "email": email,
                "organizations": organizations,
                "updated_at": updated_at,
                "user_id": user_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        email = d.pop("email")

        organizations = cast(list[str], d.pop("organizations"))

        updated_at = isoparse(d.pop("updated_at"))

        user_id = d.pop("user_id")

        name = d.pop("name", UNSET)

        user_detail = cls(
            created_at=created_at,
            email=email,
            organizations=organizations,
            updated_at=updated_at,
            user_id=user_id,
            name=name,
        )

        user_detail.additional_properties = d
        return user_detail

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
