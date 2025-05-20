from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.structure_connector_detail import StructureConnectorDetail


T = TypeVar("T", bound="DataConnectorConfigUnionType3")


@_attrs_define
class DataConnectorConfigUnionType3:
    """
    Attributes:
        structure (StructureConnectorDetail):
    """

    structure: "StructureConnectorDetail"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        structure = self.structure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "structure": structure,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structure_connector_detail import StructureConnectorDetail

        d = dict(src_dict)
        structure = StructureConnectorDetail.from_dict(d.pop("structure"))

        data_connector_config_union_type_3 = cls(
            structure=structure,
        )

        data_connector_config_union_type_3.additional_properties = d
        return data_connector_config_union_type_3

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
