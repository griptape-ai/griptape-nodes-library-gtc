from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GTCPGVectorKnowledgeBaseDetail")


@_attrs_define
class GTCPGVectorKnowledgeBaseDetail:
    """
    Attributes:
        embedding_model (str):
        query_schema (Any):
        use_default_embedding_model (bool):
    """

    embedding_model: str
    query_schema: Any
    use_default_embedding_model: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedding_model = self.embedding_model

        query_schema = self.query_schema

        use_default_embedding_model = self.use_default_embedding_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embedding_model": embedding_model,
                "query_schema": query_schema,
                "use_default_embedding_model": use_default_embedding_model,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        embedding_model = d.pop("embedding_model")

        query_schema = d.pop("query_schema")

        use_default_embedding_model = d.pop("use_default_embedding_model")

        gtcpg_vector_knowledge_base_detail = cls(
            embedding_model=embedding_model,
            query_schema=query_schema,
            use_default_embedding_model=use_default_embedding_model,
        )

        gtcpg_vector_knowledge_base_detail.additional_properties = d
        return gtcpg_vector_knowledge_base_detail

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
