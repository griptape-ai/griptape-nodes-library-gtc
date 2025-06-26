from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_detail import UserDetail


T = TypeVar("T", bound="ListUsersResponseContent")


@_attrs_define
class ListUsersResponseContent:
    """
    Attributes:
        users (Union[Unset, list['UserDetail']]):
    """

    users: Union[Unset, list["UserDetail"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_detail import UserDetail

        d = dict(src_dict)
        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = UserDetail.from_dict(users_item_data)

            users.append(users_item)

        list_users_response_content = cls(
            users=users,
        )

        list_users_response_content.additional_properties = d
        return list_users_response_content

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
