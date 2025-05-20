import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetUsageResponseContent")


@_attrs_define
class GetUsageResponseContent:
    """
    Attributes:
        bytes_ingested (float):
        bytes_ingested_limit (float):
        rag_queries (float):
        rag_queries_limit (float):
        runtime_seconds (float):
        runtime_seconds_limit (float):
        usage_period_end (datetime.datetime):
        usage_period_start (datetime.datetime):
    """

    bytes_ingested: float
    bytes_ingested_limit: float
    rag_queries: float
    rag_queries_limit: float
    runtime_seconds: float
    runtime_seconds_limit: float
    usage_period_end: datetime.datetime
    usage_period_start: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_ingested = self.bytes_ingested

        bytes_ingested_limit = self.bytes_ingested_limit

        rag_queries = self.rag_queries

        rag_queries_limit = self.rag_queries_limit

        runtime_seconds = self.runtime_seconds

        runtime_seconds_limit = self.runtime_seconds_limit

        usage_period_end = self.usage_period_end.isoformat()

        usage_period_start = self.usage_period_start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bytes_ingested": bytes_ingested,
                "bytes_ingested_limit": bytes_ingested_limit,
                "rag_queries": rag_queries,
                "rag_queries_limit": rag_queries_limit,
                "runtime_seconds": runtime_seconds,
                "runtime_seconds_limit": runtime_seconds_limit,
                "usage_period_end": usage_period_end,
                "usage_period_start": usage_period_start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_ingested = d.pop("bytes_ingested")

        bytes_ingested_limit = d.pop("bytes_ingested_limit")

        rag_queries = d.pop("rag_queries")

        rag_queries_limit = d.pop("rag_queries_limit")

        runtime_seconds = d.pop("runtime_seconds")

        runtime_seconds_limit = d.pop("runtime_seconds_limit")

        usage_period_end = isoparse(d.pop("usage_period_end"))

        usage_period_start = isoparse(d.pop("usage_period_start"))

        get_usage_response_content = cls(
            bytes_ingested=bytes_ingested,
            bytes_ingested_limit=bytes_ingested_limit,
            rag_queries=rag_queries,
            rag_queries_limit=rag_queries_limit,
            runtime_seconds=runtime_seconds,
            runtime_seconds_limit=runtime_seconds_limit,
            usage_period_end=usage_period_end,
            usage_period_start=usage_period_start,
        )

        get_usage_response_content.additional_properties = d
        return get_usage_response_content

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
