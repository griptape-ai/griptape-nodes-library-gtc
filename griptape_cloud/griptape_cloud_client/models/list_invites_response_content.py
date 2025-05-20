from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.invite_detail import InviteDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListInvitesResponseContent")


@_attrs_define
class ListInvitesResponseContent:
    """
    Attributes:
        invites (list['InviteDetail']):
        pagination (Pagination):
    """

    invites: list["InviteDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invites = []
        for invites_item_data in self.invites:
            invites_item = invites_item_data.to_dict()
            invites.append(invites_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invites": invites,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invite_detail import InviteDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        invites = []
        _invites = d.pop("invites")
        for invites_item_data in _invites:
            invites_item = InviteDetail.from_dict(invites_item_data)

            invites.append(invites_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_invites_response_content = cls(
            invites=invites,
            pagination=pagination,
        )

        list_invites_response_content.additional_properties = d
        return list_invites_response_content

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
