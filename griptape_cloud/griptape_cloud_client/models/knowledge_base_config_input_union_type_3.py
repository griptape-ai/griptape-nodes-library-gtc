from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pgai_knowledge_base_knowledge_base_input import PGAIKnowledgeBaseKnowledgeBaseInput


T = TypeVar("T", bound="KnowledgeBaseConfigInputUnionType3")


@_attrs_define
class KnowledgeBaseConfigInputUnionType3:
    """
    Attributes:
        pgai_knowledge_base (PGAIKnowledgeBaseKnowledgeBaseInput):
    """

    pgai_knowledge_base: "PGAIKnowledgeBaseKnowledgeBaseInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pgai_knowledge_base = self.pgai_knowledge_base.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pgai_knowledge_base": pgai_knowledge_base,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pgai_knowledge_base_knowledge_base_input import PGAIKnowledgeBaseKnowledgeBaseInput

        d = dict(src_dict)
        pgai_knowledge_base = PGAIKnowledgeBaseKnowledgeBaseInput.from_dict(d.pop("pgai_knowledge_base"))

        knowledge_base_config_input_union_type_3 = cls(
            pgai_knowledge_base=pgai_knowledge_base,
        )

        knowledge_base_config_input_union_type_3.additional_properties = d
        return knowledge_base_config_input_union_type_3

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
