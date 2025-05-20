import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.entry import Entry


T = TypeVar("T", bound="KnowledgeBaseQueryDetail")


@_attrs_define
class KnowledgeBaseQueryDetail:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        entries (list['Entry']):
        knowledge_base_id (str):
        knowledge_base_query_id (str):
        query (str):
    """

    created_at: datetime.datetime
    created_by: str
    entries: list["Entry"]
    knowledge_base_id: str
    knowledge_base_query_id: str
    query: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        knowledge_base_id = self.knowledge_base_id

        knowledge_base_query_id = self.knowledge_base_query_id

        query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "entries": entries,
                "knowledge_base_id": knowledge_base_id,
                "knowledge_base_query_id": knowledge_base_query_id,
                "query": query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entry import Entry

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = Entry.from_dict(entries_item_data)

            entries.append(entries_item)

        knowledge_base_id = d.pop("knowledge_base_id")

        knowledge_base_query_id = d.pop("knowledge_base_query_id")

        query = d.pop("query")

        knowledge_base_query_detail = cls(
            created_at=created_at,
            created_by=created_by,
            entries=entries,
            knowledge_base_id=knowledge_base_id,
            knowledge_base_query_id=knowledge_base_query_id,
            query=query,
        )

        knowledge_base_query_detail.additional_properties = d
        return knowledge_base_query_detail

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
