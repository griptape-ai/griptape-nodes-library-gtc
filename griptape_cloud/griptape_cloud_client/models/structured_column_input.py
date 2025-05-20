from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StructuredColumnInput")


@_attrs_define
class StructuredColumnInput:
    """
    Attributes:
        column_name (str):
        description (str):
        sql_type (str):
    """

    column_name: str
    description: str
    sql_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column_name = self.column_name

        description = self.description

        sql_type = self.sql_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column_name": column_name,
                "description": description,
                "sql_type": sql_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column_name = d.pop("column_name")

        description = d.pop("description")

        sql_type = d.pop("sql_type")

        structured_column_input = cls(
            column_name=column_name,
            description=description,
            sql_type=sql_type,
        )

        structured_column_input.additional_properties = d
        return structured_column_input

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
