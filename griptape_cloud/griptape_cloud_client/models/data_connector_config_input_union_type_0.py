from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.confluence_input import ConfluenceInput


T = TypeVar("T", bound="DataConnectorConfigInputUnionType0")


@_attrs_define
class DataConnectorConfigInputUnionType0:
    """
    Attributes:
        confluence (ConfluenceInput):
    """

    confluence: "ConfluenceInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confluence = self.confluence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confluence": confluence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confluence_input import ConfluenceInput

        d = dict(src_dict)
        confluence = ConfluenceInput.from_dict(d.pop("confluence"))

        data_connector_config_input_union_type_0 = cls(
            confluence=confluence,
        )

        data_connector_config_input_union_type_0.additional_properties = d
        return data_connector_config_input_union_type_0

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
