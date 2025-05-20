from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_type_count import ErrorTypeCount


T = TypeVar("T", bound="ErrorRateGauge")


@_attrs_define
class ErrorRateGauge:
    """
    Attributes:
        error_type_counts (Union[Unset, list['ErrorTypeCount']]):
        rate (Union[Unset, float]):
    """

    error_type_counts: Union[Unset, list["ErrorTypeCount"]] = UNSET
    rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_type_counts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.error_type_counts, Unset):
            error_type_counts = []
            for error_type_counts_item_data in self.error_type_counts:
                error_type_counts_item = error_type_counts_item_data.to_dict()
                error_type_counts.append(error_type_counts_item)

        rate = self.rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_type_counts is not UNSET:
            field_dict["error_type_counts"] = error_type_counts
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_type_count import ErrorTypeCount

        d = dict(src_dict)
        error_type_counts = []
        _error_type_counts = d.pop("error_type_counts", UNSET)
        for error_type_counts_item_data in _error_type_counts or []:
            error_type_counts_item = ErrorTypeCount.from_dict(error_type_counts_item_data)

            error_type_counts.append(error_type_counts_item)

        rate = d.pop("rate", UNSET)

        error_rate_gauge = cls(
            error_type_counts=error_type_counts,
            rate=rate,
        )

        error_rate_gauge.additional_properties = d
        return error_rate_gauge

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
