import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.span_status import SpanStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observability_event import ObservabilityEvent


T = TypeVar("T", bound="SpanDetail")


@_attrs_define
class SpanDetail:
    """
    Attributes:
        attributes (Any):
        end_time (datetime.datetime):
        events (ObservabilityEvent):
        name (str):
        span_id (str):
        start_time (datetime.datetime):
        status (SpanStatus):
        trace_id (str):
        parent_id (Union[Unset, str]):
    """

    attributes: Any
    end_time: datetime.datetime
    events: "ObservabilityEvent"
    name: str
    span_id: str
    start_time: datetime.datetime
    status: SpanStatus
    trace_id: str
    parent_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes

        end_time = self.end_time.isoformat()

        events = self.events.to_dict()

        name = self.name

        span_id = self.span_id

        start_time = self.start_time.isoformat()

        status = self.status.value

        trace_id = self.trace_id

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "end_time": end_time,
                "events": events,
                "name": name,
                "span_id": span_id,
                "start_time": start_time,
                "status": status,
                "trace_id": trace_id,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observability_event import ObservabilityEvent

        d = dict(src_dict)
        attributes = d.pop("attributes")

        end_time = isoparse(d.pop("end_time"))

        events = ObservabilityEvent.from_dict(d.pop("events"))

        name = d.pop("name")

        span_id = d.pop("span_id")

        start_time = isoparse(d.pop("start_time"))

        status = SpanStatus(d.pop("status"))

        trace_id = d.pop("trace_id")

        parent_id = d.pop("parent_id", UNSET)

        span_detail = cls(
            attributes=attributes,
            end_time=end_time,
            events=events,
            name=name,
            span_id=span_id,
            start_time=start_time,
            status=status,
            trace_id=trace_id,
            parent_id=parent_id,
        )

        span_detail.additional_properties = d
        return span_detail

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
