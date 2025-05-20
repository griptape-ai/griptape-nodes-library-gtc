from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pg_vector_knowledge_base_detail import PGVectorKnowledgeBaseDetail


T = TypeVar("T", bound="KnowledgeBaseConfigUnionType0")


@_attrs_define
class KnowledgeBaseConfigUnionType0:
    """
    Attributes:
        pg_vector (PGVectorKnowledgeBaseDetail):
    """

    pg_vector: "PGVectorKnowledgeBaseDetail"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pg_vector = self.pg_vector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pg_vector": pg_vector,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pg_vector_knowledge_base_detail import PGVectorKnowledgeBaseDetail

        d = dict(src_dict)
        pg_vector = PGVectorKnowledgeBaseDetail.from_dict(d.pop("pg_vector"))

        knowledge_base_config_union_type_0 = cls(
            pg_vector=pg_vector,
        )

        knowledge_base_config_union_type_0.additional_properties = d
        return knowledge_base_config_union_type_0

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
