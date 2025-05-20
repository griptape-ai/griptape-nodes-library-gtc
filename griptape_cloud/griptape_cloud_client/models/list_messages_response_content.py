from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.message_detail import MessageDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListMessagesResponseContent")


@_attrs_define
class ListMessagesResponseContent:
    """
    Attributes:
        messages (list['MessageDetail']):
        pagination (Pagination):
    """

    messages: list["MessageDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_detail import MessageDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = MessageDetail.from_dict(messages_item_data)

            messages.append(messages_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_messages_response_content = cls(
            messages=messages,
            pagination=pagination,
        )

        list_messages_response_content.additional_properties = d
        return list_messages_response_content

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
