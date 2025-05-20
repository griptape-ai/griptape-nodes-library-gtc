from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_token_counts_map import ModelTokenCountsMap


T = TypeVar("T", bound="TokenCountGauge")


@_attrs_define
class TokenCountGauge:
    """
    Attributes:
        by_model (Union[Unset, ModelTokenCountsMap]):
        input_ (Union[Unset, float]):
        output (Union[Unset, float]):
    """

    by_model: Union[Unset, "ModelTokenCountsMap"] = UNSET
    input_: Union[Unset, float] = UNSET
    output: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.by_model, Unset):
            by_model = self.by_model.to_dict()

        input_ = self.input_

        output = self.output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_model is not UNSET:
            field_dict["by_model"] = by_model
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_token_counts_map import ModelTokenCountsMap

        d = dict(src_dict)
        _by_model = d.pop("by_model", UNSET)
        by_model: Union[Unset, ModelTokenCountsMap]
        if isinstance(_by_model, Unset):
            by_model = UNSET
        else:
            by_model = ModelTokenCountsMap.from_dict(_by_model)

        input_ = d.pop("input", UNSET)

        output = d.pop("output", UNSET)

        token_count_gauge = cls(
            by_model=by_model,
            input_=input_,
            output=output,
        )

        token_count_gauge.additional_properties = d
        return token_count_gauge

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
