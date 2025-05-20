from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_message_usage import ChatMessageUsage
    from ..models.message_content import MessageContent


T = TypeVar("T", bound="ChatMessageMessage")


@_attrs_define
class ChatMessageMessage:
    """
    Attributes:
        content (list['MessageContent']):
        role (str):
        usage (ChatMessageUsage):
    """

    content: list["MessageContent"]
    role: str
    usage: "ChatMessageUsage"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            content.append(content_item)

        role = self.role

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "role": role,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_message_usage import ChatMessageUsage
        from ..models.message_content import MessageContent

        d = dict(src_dict)
        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = MessageContent.from_dict(content_item_data)

            content.append(content_item)

        role = d.pop("role")

        usage = ChatMessageUsage.from_dict(d.pop("usage"))

        chat_message_message = cls(
            content=content,
            role=role,
            usage=usage,
        )

        chat_message_message.additional_properties = d
        return chat_message_message

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
