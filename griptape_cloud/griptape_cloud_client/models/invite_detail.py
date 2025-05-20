import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.invite_status import InviteStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="InviteDetail")


@_attrs_define
class InviteDetail:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        email (str):
        expires_at (datetime.datetime):
        invite_id (str):
        organization_id (str):
        status (InviteStatus):
        responded_at (Union[Unset, datetime.datetime]):
    """

    created_at: datetime.datetime
    created_by: str
    email: str
    expires_at: datetime.datetime
    invite_id: str
    organization_id: str
    status: InviteStatus
    responded_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        email = self.email

        expires_at = self.expires_at.isoformat()

        invite_id = self.invite_id

        organization_id = self.organization_id

        status = self.status.value

        responded_at: Union[Unset, str] = UNSET
        if not isinstance(self.responded_at, Unset):
            responded_at = self.responded_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "email": email,
                "expires_at": expires_at,
                "invite_id": invite_id,
                "organization_id": organization_id,
                "status": status,
            }
        )
        if responded_at is not UNSET:
            field_dict["responded_at"] = responded_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        email = d.pop("email")

        expires_at = isoparse(d.pop("expires_at"))

        invite_id = d.pop("invite_id")

        organization_id = d.pop("organization_id")

        status = InviteStatus(d.pop("status"))

        _responded_at = d.pop("responded_at", UNSET)
        responded_at: Union[Unset, datetime.datetime]
        if isinstance(_responded_at, Unset):
            responded_at = UNSET
        else:
            responded_at = isoparse(_responded_at)

        invite_detail = cls(
            created_at=created_at,
            created_by=created_by,
            email=email,
            expires_at=expires_at,
            invite_id=invite_id,
            organization_id=organization_id,
            status=status,
            responded_at=responded_at,
        )

        invite_detail.additional_properties = d
        return invite_detail

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
