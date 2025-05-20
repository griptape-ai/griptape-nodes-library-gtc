from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organization_user_detail import OrganizationUserDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListOrganizationUsersResponseContent")


@_attrs_define
class ListOrganizationUsersResponseContent:
    """
    Attributes:
        pagination (Pagination):
        users (list['OrganizationUserDetail']):
    """

    pagination: "Pagination"
    users: list["OrganizationUserDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_user_detail import OrganizationUserDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = OrganizationUserDetail.from_dict(users_item_data)

            users.append(users_item)

        list_organization_users_response_content = cls(
            pagination=pagination,
            users=users,
        )

        list_organization_users_response_content.additional_properties = d
        return list_organization_users_response_content

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
