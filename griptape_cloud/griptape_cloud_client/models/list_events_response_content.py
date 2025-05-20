from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_detail import EventDetail


T = TypeVar("T", bound="ListEventsResponseContent")


@_attrs_define
class ListEventsResponseContent:
    """
    Attributes:
        count (float):
        events (list['EventDetail']):
        limit (float):
        next_offset (float):
        offset (float):
        total_count (float):
    """

    count: float
    events: list["EventDetail"]
    limit: float
    next_offset: float
    offset: float
    total_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        limit = self.limit

        next_offset = self.next_offset

        offset = self.offset

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "events": events,
                "limit": limit,
                "next_offset": next_offset,
                "offset": offset,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_detail import EventDetail

        d = dict(src_dict)
        count = d.pop("count")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = EventDetail.from_dict(events_item_data)

            events.append(events_item)

        limit = d.pop("limit")

        next_offset = d.pop("next_offset")

        offset = d.pop("offset")

        total_count = d.pop("total_count")

        list_events_response_content = cls(
            count=count,
            events=events,
            limit=limit,
            next_offset=next_offset,
            offset=offset,
            total_count=total_count,
        )

        list_events_response_content.additional_properties = d
        return list_events_response_content

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
