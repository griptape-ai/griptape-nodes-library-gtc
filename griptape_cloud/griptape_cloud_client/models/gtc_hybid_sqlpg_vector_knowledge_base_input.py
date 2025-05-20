from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_column_input import StructuredColumnInput
    from ..models.unstructured_column_input import UnstructuredColumnInput


T = TypeVar("T", bound="GTCHybidSQLPGVectorKnowledgeBaseInput")


@_attrs_define
class GTCHybidSQLPGVectorKnowledgeBaseInput:
    """
    Attributes:
        structured_columns (list['StructuredColumnInput']):
        unstructured_columns (list['UnstructuredColumnInput']):
        embedding_model (Union[Unset, str]):
        use_default_embedding_model (Union[Unset, bool]):
    """

    structured_columns: list["StructuredColumnInput"]
    unstructured_columns: list["UnstructuredColumnInput"]
    embedding_model: Union[Unset, str] = UNSET
    use_default_embedding_model: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        structured_columns = []
        for structured_columns_item_data in self.structured_columns:
            structured_columns_item = structured_columns_item_data.to_dict()
            structured_columns.append(structured_columns_item)

        unstructured_columns = []
        for unstructured_columns_item_data in self.unstructured_columns:
            unstructured_columns_item = unstructured_columns_item_data.to_dict()
            unstructured_columns.append(unstructured_columns_item)

        embedding_model = self.embedding_model

        use_default_embedding_model = self.use_default_embedding_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "structured_columns": structured_columns,
                "unstructured_columns": unstructured_columns,
            }
        )
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if use_default_embedding_model is not UNSET:
            field_dict["use_default_embedding_model"] = use_default_embedding_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_column_input import StructuredColumnInput
        from ..models.unstructured_column_input import UnstructuredColumnInput

        d = dict(src_dict)
        structured_columns = []
        _structured_columns = d.pop("structured_columns")
        for structured_columns_item_data in _structured_columns:
            structured_columns_item = StructuredColumnInput.from_dict(structured_columns_item_data)

            structured_columns.append(structured_columns_item)

        unstructured_columns = []
        _unstructured_columns = d.pop("unstructured_columns")
        for unstructured_columns_item_data in _unstructured_columns:
            unstructured_columns_item = UnstructuredColumnInput.from_dict(unstructured_columns_item_data)

            unstructured_columns.append(unstructured_columns_item)

        embedding_model = d.pop("embedding_model", UNSET)

        use_default_embedding_model = d.pop("use_default_embedding_model", UNSET)

        gtc_hybid_sqlpg_vector_knowledge_base_input = cls(
            structured_columns=structured_columns,
            unstructured_columns=unstructured_columns,
            embedding_model=embedding_model,
            use_default_embedding_model=use_default_embedding_model,
        )

        gtc_hybid_sqlpg_vector_knowledge_base_input.additional_properties = d
        return gtc_hybid_sqlpg_vector_knowledge_base_input

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
