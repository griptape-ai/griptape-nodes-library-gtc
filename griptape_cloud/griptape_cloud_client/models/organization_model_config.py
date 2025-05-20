from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationModelConfig")


@_attrs_define
class OrganizationModelConfig:
    """
    Attributes:
        default_chat_model (Union[Unset, str]):
        default_embedding_model (Union[Unset, str]):
        default_image_generation_model (Union[Unset, str]):
        default_rerank_model (Union[Unset, str]):
    """

    default_chat_model: Union[Unset, str] = UNSET
    default_embedding_model: Union[Unset, str] = UNSET
    default_image_generation_model: Union[Unset, str] = UNSET
    default_rerank_model: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_chat_model = self.default_chat_model

        default_embedding_model = self.default_embedding_model

        default_image_generation_model = self.default_image_generation_model

        default_rerank_model = self.default_rerank_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_chat_model is not UNSET:
            field_dict["default_chat_model"] = default_chat_model
        if default_embedding_model is not UNSET:
            field_dict["default_embedding_model"] = default_embedding_model
        if default_image_generation_model is not UNSET:
            field_dict["default_image_generation_model"] = default_image_generation_model
        if default_rerank_model is not UNSET:
            field_dict["default_rerank_model"] = default_rerank_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_chat_model = d.pop("default_chat_model", UNSET)

        default_embedding_model = d.pop("default_embedding_model", UNSET)

        default_image_generation_model = d.pop("default_image_generation_model", UNSET)

        default_rerank_model = d.pop("default_rerank_model", UNSET)

        organization_model_config = cls(
            default_chat_model=default_chat_model,
            default_embedding_model=default_embedding_model,
            default_image_generation_model=default_image_generation_model,
            default_rerank_model=default_rerank_model,
        )

        organization_model_config.additional_properties = d
        return organization_model_config

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
