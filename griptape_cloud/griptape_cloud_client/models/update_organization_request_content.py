from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_model_config import OrganizationModelConfig


T = TypeVar("T", bound="UpdateOrganizationRequestContent")


@_attrs_define
class UpdateOrganizationRequestContent:
    """
    Attributes:
        model_config (Union[Unset, OrganizationModelConfig]):
        name (Union[Unset, str]):
    """

    model_config: Union[Unset, "OrganizationModelConfig"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.model_config, Unset):
            model_config = self.model_config.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_config is not UNSET:
            field_dict["model_config"] = model_config
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_model_config import OrganizationModelConfig

        d = dict(src_dict)
        _model_config = d.pop("model_config", UNSET)
        model_config: Union[Unset, OrganizationModelConfig]
        if isinstance(_model_config, Unset):
            model_config = UNSET
        else:
            model_config = OrganizationModelConfig.from_dict(_model_config)

        name = d.pop("name", UNSET)

        update_organization_request_content = cls(
            model_config=model_config,
            name=name,
        )

        update_organization_request_content.additional_properties = d
        return update_organization_request_content

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
