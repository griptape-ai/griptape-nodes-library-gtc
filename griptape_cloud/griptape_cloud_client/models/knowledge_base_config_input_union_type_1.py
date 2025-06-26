from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gtcpg_vector_knowledge_base_input import GTCPGVectorKnowledgeBaseInput


T = TypeVar("T", bound="KnowledgeBaseConfigInputUnionType1")


@_attrs_define
class KnowledgeBaseConfigInputUnionType1:
    """
    Attributes:
        gtc_pg_vector (GTCPGVectorKnowledgeBaseInput):
    """

    gtc_pg_vector: "GTCPGVectorKnowledgeBaseInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gtc_pg_vector = self.gtc_pg_vector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gtc_pg_vector": gtc_pg_vector,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gtcpg_vector_knowledge_base_input import GTCPGVectorKnowledgeBaseInput

        d = dict(src_dict)
        gtc_pg_vector = GTCPGVectorKnowledgeBaseInput.from_dict(d.pop("gtc_pg_vector"))

        knowledge_base_config_input_union_type_1 = cls(
            gtc_pg_vector=gtc_pg_vector,
        )

        knowledge_base_config_input_union_type_1.additional_properties = d
        return knowledge_base_config_input_union_type_1

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
