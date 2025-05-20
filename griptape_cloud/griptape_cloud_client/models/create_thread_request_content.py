from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_input import MessageInput
    from ..models.metadata import Metadata


T = TypeVar("T", bound="CreateThreadRequestContent")


@_attrs_define
class CreateThreadRequestContent:
    """
    Attributes:
        name (str):
        alias (Union[Unset, str]):
        messages (Union[Unset, list['MessageInput']]):
        metadata (Union[Unset, Metadata]):
    """

    name: str
    alias: Union[Unset, str] = UNSET
    messages: Union[Unset, list["MessageInput"]] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alias = self.alias

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if messages is not UNSET:
            field_dict["messages"] = messages
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_input import MessageInput
        from ..models.metadata import Metadata

        d = dict(src_dict)
        name = d.pop("name")

        alias = d.pop("alias", UNSET)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = MessageInput.from_dict(messages_item_data)

            messages.append(messages_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        create_thread_request_content = cls(
            name=name,
            alias=alias,
            messages=messages,
            metadata=metadata,
        )

        create_thread_request_content.additional_properties = d
        return create_thread_request_content

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
