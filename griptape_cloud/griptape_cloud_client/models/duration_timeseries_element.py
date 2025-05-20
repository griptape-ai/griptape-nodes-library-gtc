import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DurationTimeseriesElement")


@_attrs_define
class DurationTimeseriesElement:
    """
    Attributes:
        seconds_p0 (Union[Unset, float]):
        seconds_p100 (Union[Unset, float]):
        seconds_p50 (Union[Unset, float]):
        time (Union[Unset, datetime.datetime]):
    """

    seconds_p0: Union[Unset, float] = UNSET
    seconds_p100: Union[Unset, float] = UNSET
    seconds_p50: Union[Unset, float] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seconds_p0 = self.seconds_p0

        seconds_p100 = self.seconds_p100

        seconds_p50 = self.seconds_p50

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seconds_p0 is not UNSET:
            field_dict["seconds_p0"] = seconds_p0
        if seconds_p100 is not UNSET:
            field_dict["seconds_p100"] = seconds_p100
        if seconds_p50 is not UNSET:
            field_dict["seconds_p50"] = seconds_p50
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seconds_p0 = d.pop("seconds_p0", UNSET)

        seconds_p100 = d.pop("seconds_p100", UNSET)

        seconds_p50 = d.pop("seconds_p50", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        duration_timeseries_element = cls(
            seconds_p0=seconds_p0,
            seconds_p100=seconds_p100,
            seconds_p50=seconds_p50,
            time=time,
        )

        duration_timeseries_element.additional_properties = d
        return duration_timeseries_element

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
