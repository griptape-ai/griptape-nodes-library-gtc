from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.json_schema_properties import JsonSchemaProperties


T = TypeVar("T", bound="JsonSchema")


@_attrs_define
class JsonSchema:
    """
    Attributes:
        additional_properties (bool):
        description (str):
        id (str):
        properties (JsonSchemaProperties):
        required (list[str]):
        schema (str):
        title (str):
        type_ (str):
    """

    additional_properties: bool
    description: str
    id: str
    properties: "JsonSchemaProperties"
    required: list[str]
    schema: str
    title: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_properties = self.additional_properties

        description = self.description

        id = self.id

        properties = self.properties.to_dict()

        required = self.required

        schema = self.schema

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "additionalProperties": additional_properties,
                "description": description,
                "id": id,
                "properties": properties,
                "required": required,
                "schema": schema,
                "title": title,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_schema_properties import JsonSchemaProperties

        d = dict(src_dict)
        additional_properties = d.pop("additionalProperties")

        description = d.pop("description")

        id = d.pop("id")

        properties = JsonSchemaProperties.from_dict(d.pop("properties"))

        required = cast(list[str], d.pop("required"))

        schema = d.pop("schema")

        title = d.pop("title")

        type_ = d.pop("type")

        json_schema = cls(
            additional_properties=additional_properties,
            description=description,
            id=id,
            properties=properties,
            required=required,
            schema=schema,
            title=title,
            type_=type_,
        )

        json_schema.additional_properties = d
        return json_schema

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
