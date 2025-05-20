from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_base_search_detail import KnowledgeBaseSearchDetail


T = TypeVar("T", bound="ListKnowledgeBaseSearchesResponseContent")


@_attrs_define
class ListKnowledgeBaseSearchesResponseContent:
    """
    Attributes:
        knowledge_base_searches (Union[Unset, list['KnowledgeBaseSearchDetail']]):
    """

    knowledge_base_searches: Union[Unset, list["KnowledgeBaseSearchDetail"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_base_searches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.knowledge_base_searches, Unset):
            knowledge_base_searches = []
            for knowledge_base_searches_item_data in self.knowledge_base_searches:
                knowledge_base_searches_item = knowledge_base_searches_item_data.to_dict()
                knowledge_base_searches.append(knowledge_base_searches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if knowledge_base_searches is not UNSET:
            field_dict["knowledge_base_searches"] = knowledge_base_searches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knowledge_base_search_detail import KnowledgeBaseSearchDetail

        d = dict(src_dict)
        knowledge_base_searches = []
        _knowledge_base_searches = d.pop("knowledge_base_searches", UNSET)
        for knowledge_base_searches_item_data in _knowledge_base_searches or []:
            knowledge_base_searches_item = KnowledgeBaseSearchDetail.from_dict(knowledge_base_searches_item_data)

            knowledge_base_searches.append(knowledge_base_searches_item)

        list_knowledge_base_searches_response_content = cls(
            knowledge_base_searches=knowledge_base_searches,
        )

        list_knowledge_base_searches_response_content.additional_properties = d
        return list_knowledge_base_searches_response_content

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
