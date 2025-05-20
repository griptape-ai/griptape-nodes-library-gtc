from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_message_driver_configuration import ChatMessageDriverConfiguration
    from ..models.chat_message_message import ChatMessageMessage
    from ..models.chat_message_tool import ChatMessageTool
    from ..models.json_schema import JsonSchema


T = TypeVar("T", bound="CreateChatMessageRequestContent")


@_attrs_define
class CreateChatMessageRequestContent:
    """
    Attributes:
        driver_configuration (ChatMessageDriverConfiguration):
        messages (list['ChatMessageMessage']):
        output_schema (JsonSchema):
        tools (list['ChatMessageTool']):
    """

    driver_configuration: "ChatMessageDriverConfiguration"
    messages: list["ChatMessageMessage"]
    output_schema: "JsonSchema"
    tools: list["ChatMessageTool"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        driver_configuration = self.driver_configuration.to_dict()

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        output_schema = self.output_schema.to_dict()

        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "driver_configuration": driver_configuration,
                "messages": messages,
                "output_schema": output_schema,
                "tools": tools,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_message_driver_configuration import ChatMessageDriverConfiguration
        from ..models.chat_message_message import ChatMessageMessage
        from ..models.chat_message_tool import ChatMessageTool
        from ..models.json_schema import JsonSchema

        d = dict(src_dict)
        driver_configuration = ChatMessageDriverConfiguration.from_dict(d.pop("driver_configuration"))

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = ChatMessageMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        output_schema = JsonSchema.from_dict(d.pop("output_schema"))

        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = ChatMessageTool.from_dict(tools_item_data)

            tools.append(tools_item)

        create_chat_message_request_content = cls(
            driver_configuration=driver_configuration,
            messages=messages,
            output_schema=output_schema,
            tools=tools,
        )

        create_chat_message_request_content.additional_properties = d
        return create_chat_message_request_content

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
