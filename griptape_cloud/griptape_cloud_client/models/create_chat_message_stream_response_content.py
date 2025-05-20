from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_message_usage import ChatMessageUsage
    from ..models.stream_message_content import StreamMessageContent


T = TypeVar("T", bound="CreateChatMessageStreamResponseContent")


@_attrs_define
class CreateChatMessageStreamResponseContent:
    """
    Attributes:
        content (list['StreamMessageContent']):
        role (str):
        type_ (str):
        usage (Union[Unset, ChatMessageUsage]):
    """

    content: list["StreamMessageContent"]
    role: str
    type_: str
    usage: Union[Unset, "ChatMessageUsage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            content.append(content_item)

        role = self.role

        type_ = self.type_

        usage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "role": role,
                "type": type_,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_message_usage import ChatMessageUsage
        from ..models.stream_message_content import StreamMessageContent

        d = dict(src_dict)
        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = StreamMessageContent.from_dict(content_item_data)

            content.append(content_item)

        role = d.pop("role")

        type_ = d.pop("type")

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, ChatMessageUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = ChatMessageUsage.from_dict(_usage)

        create_chat_message_stream_response_content = cls(
            content=content,
            role=role,
            type_=type_,
            usage=usage,
        )

        create_chat_message_stream_response_content.additional_properties = d
        return create_chat_message_stream_response_content

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
