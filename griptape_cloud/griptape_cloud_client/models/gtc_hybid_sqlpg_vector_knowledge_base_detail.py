from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.structured_column_detail import StructuredColumnDetail
    from ..models.unstructured_column_detail import UnstructuredColumnDetail


T = TypeVar("T", bound="GTCHybidSQLPGVectorKnowledgeBaseDetail")


@_attrs_define
class GTCHybidSQLPGVectorKnowledgeBaseDetail:
    """
    Attributes:
        embedding_model (str):
        query_schema (Any):
        structured_columns (list['StructuredColumnDetail']):
        unstructured_columns (list['UnstructuredColumnDetail']):
        use_default_embedding_model (bool):
    """

    embedding_model: str
    query_schema: Any
    structured_columns: list["StructuredColumnDetail"]
    unstructured_columns: list["UnstructuredColumnDetail"]
    use_default_embedding_model: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedding_model = self.embedding_model

        query_schema = self.query_schema

        structured_columns = []
        for structured_columns_item_data in self.structured_columns:
            structured_columns_item = structured_columns_item_data.to_dict()
            structured_columns.append(structured_columns_item)

        unstructured_columns = []
        for unstructured_columns_item_data in self.unstructured_columns:
            unstructured_columns_item = unstructured_columns_item_data.to_dict()
            unstructured_columns.append(unstructured_columns_item)

        use_default_embedding_model = self.use_default_embedding_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embedding_model": embedding_model,
                "query_schema": query_schema,
                "structured_columns": structured_columns,
                "unstructured_columns": unstructured_columns,
                "use_default_embedding_model": use_default_embedding_model,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_column_detail import StructuredColumnDetail
        from ..models.unstructured_column_detail import UnstructuredColumnDetail

        d = dict(src_dict)
        embedding_model = d.pop("embedding_model")

        query_schema = d.pop("query_schema")

        structured_columns = []
        _structured_columns = d.pop("structured_columns")
        for structured_columns_item_data in _structured_columns:
            structured_columns_item = StructuredColumnDetail.from_dict(structured_columns_item_data)

            structured_columns.append(structured_columns_item)

        unstructured_columns = []
        _unstructured_columns = d.pop("unstructured_columns")
        for unstructured_columns_item_data in _unstructured_columns:
            unstructured_columns_item = UnstructuredColumnDetail.from_dict(unstructured_columns_item_data)

            unstructured_columns.append(unstructured_columns_item)

        use_default_embedding_model = d.pop("use_default_embedding_model")

        gtc_hybid_sqlpg_vector_knowledge_base_detail = cls(
            embedding_model=embedding_model,
            query_schema=query_schema,
            structured_columns=structured_columns,
            unstructured_columns=unstructured_columns,
            use_default_embedding_model=use_default_embedding_model,
        )

        gtc_hybid_sqlpg_vector_knowledge_base_detail.additional_properties = d
        return gtc_hybid_sqlpg_vector_knowledge_base_detail

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
