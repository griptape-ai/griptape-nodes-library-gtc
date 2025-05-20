from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gtc_hybid_sqlpg_vector_knowledge_base_detail import GTCHybidSQLPGVectorKnowledgeBaseDetail


T = TypeVar("T", bound="KnowledgeBaseConfigUnionType2")


@_attrs_define
class KnowledgeBaseConfigUnionType2:
    """
    Attributes:
        gtc_hybrid_sql_pg_vector (GTCHybidSQLPGVectorKnowledgeBaseDetail):
    """

    gtc_hybrid_sql_pg_vector: "GTCHybidSQLPGVectorKnowledgeBaseDetail"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gtc_hybrid_sql_pg_vector = self.gtc_hybrid_sql_pg_vector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gtc_hybrid_sql_pg_vector": gtc_hybrid_sql_pg_vector,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gtc_hybid_sqlpg_vector_knowledge_base_detail import GTCHybidSQLPGVectorKnowledgeBaseDetail

        d = dict(src_dict)
        gtc_hybrid_sql_pg_vector = GTCHybidSQLPGVectorKnowledgeBaseDetail.from_dict(d.pop("gtc_hybrid_sql_pg_vector"))

        knowledge_base_config_union_type_2 = cls(
            gtc_hybrid_sql_pg_vector=gtc_hybrid_sql_pg_vector,
        )

        knowledge_base_config_union_type_2.additional_properties = d
        return knowledge_base_config_union_type_2

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
