from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structure_connector_detail import StructureConnectorDetail


T = TypeVar("T", bound="TransformDetail")


@_attrs_define
class TransformDetail:
    """
    Attributes:
        structure (Union[Unset, StructureConnectorDetail]):
    """

    structure: Union[Unset, "StructureConnectorDetail"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        structure: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.structure, Unset):
            structure = self.structure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if structure is not UNSET:
            field_dict["structure"] = structure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structure_connector_detail import StructureConnectorDetail

        d = dict(src_dict)
        _structure = d.pop("structure", UNSET)
        structure: Union[Unset, StructureConnectorDetail]
        if isinstance(_structure, Unset):
            structure = UNSET
        else:
            structure = StructureConnectorDetail.from_dict(_structure)

        transform_detail = cls(
            structure=structure,
        )

        transform_detail.additional_properties = d
        return transform_detail

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
