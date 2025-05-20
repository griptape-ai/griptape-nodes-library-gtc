from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration_timeseries_element import DurationTimeseriesElement


T = TypeVar("T", bound="DurationPlot")


@_attrs_define
class DurationPlot:
    """
    Attributes:
        seconds_avg (Union[Unset, float]):
        seconds_p100 (Union[Unset, float]):
        seconds_p50 (Union[Unset, float]):
        timeseries (Union[Unset, list['DurationTimeseriesElement']]):
    """

    seconds_avg: Union[Unset, float] = UNSET
    seconds_p100: Union[Unset, float] = UNSET
    seconds_p50: Union[Unset, float] = UNSET
    timeseries: Union[Unset, list["DurationTimeseriesElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seconds_avg = self.seconds_avg

        seconds_p100 = self.seconds_p100

        seconds_p50 = self.seconds_p50

        timeseries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.timeseries, Unset):
            timeseries = []
            for timeseries_item_data in self.timeseries:
                timeseries_item = timeseries_item_data.to_dict()
                timeseries.append(timeseries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seconds_avg is not UNSET:
            field_dict["seconds_avg"] = seconds_avg
        if seconds_p100 is not UNSET:
            field_dict["seconds_p100"] = seconds_p100
        if seconds_p50 is not UNSET:
            field_dict["seconds_p50"] = seconds_p50
        if timeseries is not UNSET:
            field_dict["timeseries"] = timeseries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duration_timeseries_element import DurationTimeseriesElement

        d = dict(src_dict)
        seconds_avg = d.pop("seconds_avg", UNSET)

        seconds_p100 = d.pop("seconds_p100", UNSET)

        seconds_p50 = d.pop("seconds_p50", UNSET)

        timeseries = []
        _timeseries = d.pop("timeseries", UNSET)
        for timeseries_item_data in _timeseries or []:
            timeseries_item = DurationTimeseriesElement.from_dict(timeseries_item_data)

            timeseries.append(timeseries_item)

        duration_plot = cls(
            seconds_avg=seconds_avg,
            seconds_p100=seconds_p100,
            seconds_p50=seconds_p50,
            timeseries=timeseries,
        )

        duration_plot.additional_properties = d
        return duration_plot

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
