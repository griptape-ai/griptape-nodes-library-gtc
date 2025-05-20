from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_type import ModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelDetail")


@_attrs_define
class ModelDetail:
    """
    Attributes:
        default (bool):
        model_name (str):
        model_type (ModelType):
        description (Union[Unset, str]):
    """

    default: bool
    model_name: str
    model_type: ModelType
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        model_name = self.model_name

        model_type = self.model_type.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
                "model_name": model_name,
                "model_type": model_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default = d.pop("default")

        model_name = d.pop("model_name")

        model_type = ModelType(d.pop("model_type"))

        description = d.pop("description", UNSET)

        model_detail = cls(
            default=default,
            model_name=model_name,
            model_type=model_type,
            description=description,
        )

        model_detail.additional_properties = d
        return model_detail

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
