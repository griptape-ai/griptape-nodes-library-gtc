from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.json_schema import JsonSchema


T = TypeVar("T", bound="ChatMessageToolActivity")


@_attrs_define
class ChatMessageToolActivity:
    """
    Attributes:
        description (str):
        json_schema (JsonSchema):
        name (str):
    """

    description: str
    json_schema: "JsonSchema"
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        json_schema = self.json_schema.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "json_schema": json_schema,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_schema import JsonSchema

        d = dict(src_dict)
        description = d.pop("description")

        json_schema = JsonSchema.from_dict(d.pop("json_schema"))

        name = d.pop("name")

        chat_message_tool_activity = cls(
            description=description,
            json_schema=json_schema,
            name=name,
        )

        chat_message_tool_activity.additional_properties = d
        return chat_message_tool_activity

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
