from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_duration import ActivityDuration


T = TypeVar("T", bound="RunDurationGauge")


@_attrs_define
class RunDurationGauge:
    """
    Attributes:
        activity_durations (Union[Unset, list['ActivityDuration']]):
        total_seconds (Union[Unset, float]):
    """

    activity_durations: Union[Unset, list["ActivityDuration"]] = UNSET
    total_seconds: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_durations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.activity_durations, Unset):
            activity_durations = []
            for activity_durations_item_data in self.activity_durations:
                activity_durations_item = activity_durations_item_data.to_dict()
                activity_durations.append(activity_durations_item)

        total_seconds = self.total_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_durations is not UNSET:
            field_dict["activity_durations"] = activity_durations
        if total_seconds is not UNSET:
            field_dict["total_seconds"] = total_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_duration import ActivityDuration

        d = dict(src_dict)
        activity_durations = []
        _activity_durations = d.pop("activity_durations", UNSET)
        for activity_durations_item_data in _activity_durations or []:
            activity_durations_item = ActivityDuration.from_dict(activity_durations_item_data)

            activity_durations.append(activity_durations_item)

        total_seconds = d.pop("total_seconds", UNSET)

        run_duration_gauge = cls(
            activity_durations=activity_durations,
            total_seconds=total_seconds,
        )

        run_duration_gauge.additional_properties = d
        return run_duration_gauge

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
