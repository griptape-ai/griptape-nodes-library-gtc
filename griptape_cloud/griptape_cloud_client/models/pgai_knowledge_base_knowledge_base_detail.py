from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PGAIKnowledgeBaseKnowledgeBaseDetail")


@_attrs_define
class PGAIKnowledgeBaseKnowledgeBaseDetail:
    """
    Attributes:
        knowledge_base_name (str):
        query_schema (Any):
    """

    knowledge_base_name: str
    query_schema: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_base_name = self.knowledge_base_name

        query_schema = self.query_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_base_name": knowledge_base_name,
                "query_schema": query_schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        knowledge_base_name = d.pop("knowledge_base_name")

        query_schema = d.pop("query_schema")

        pgai_knowledge_base_knowledge_base_detail = cls(
            knowledge_base_name=knowledge_base_name,
            query_schema=query_schema,
        )

        pgai_knowledge_base_knowledge_base_detail.additional_properties = d
        return pgai_knowledge_base_knowledge_base_detail

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
