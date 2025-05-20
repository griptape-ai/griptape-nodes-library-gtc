import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetEventResponseContent")


@_attrs_define
class GetEventResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        event_id (str):
        origin (str):
        payload (Any):
        structure_run_id (str):
        timestamp (float):
        type_ (str):
    """

    created_at: datetime.datetime
    event_id: str
    origin: str
    payload: Any
    structure_run_id: str
    timestamp: float
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        event_id = self.event_id

        origin = self.origin

        payload = self.payload

        structure_run_id = self.structure_run_id

        timestamp = self.timestamp

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "event_id": event_id,
                "origin": origin,
                "payload": payload,
                "structure_run_id": structure_run_id,
                "timestamp": timestamp,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        event_id = d.pop("event_id")

        origin = d.pop("origin")

        payload = d.pop("payload")

        structure_run_id = d.pop("structure_run_id")

        timestamp = d.pop("timestamp")

        type_ = d.pop("type")

        get_event_response_content = cls(
            created_at=created_at,
            event_id=event_id,
            origin=origin,
            payload=payload,
            structure_run_id=structure_run_id,
            timestamp=timestamp,
            type_=type_,
        )

        get_event_response_content.additional_properties = d
        return get_event_response_content

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
