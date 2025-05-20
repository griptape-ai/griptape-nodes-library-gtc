import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="KnowledgeBaseSearchDetail")


@_attrs_define
class KnowledgeBaseSearchDetail:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        knowledge_base_id (str):
        knowledge_base_search_id (str):
        query (str):
        result (str):
    """

    created_at: datetime.datetime
    created_by: str
    knowledge_base_id: str
    knowledge_base_search_id: str
    query: str
    result: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        knowledge_base_id = self.knowledge_base_id

        knowledge_base_search_id = self.knowledge_base_search_id

        query = self.query

        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "knowledge_base_id": knowledge_base_id,
                "knowledge_base_search_id": knowledge_base_search_id,
                "query": query,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        knowledge_base_id = d.pop("knowledge_base_id")

        knowledge_base_search_id = d.pop("knowledge_base_search_id")

        query = d.pop("query")

        result = d.pop("result")

        knowledge_base_search_detail = cls(
            created_at=created_at,
            created_by=created_by,
            knowledge_base_id=knowledge_base_id,
            knowledge_base_search_id=knowledge_base_search_id,
            query=query,
            result=result,
        )

        knowledge_base_search_detail.additional_properties = d
        return knowledge_base_search_detail

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
