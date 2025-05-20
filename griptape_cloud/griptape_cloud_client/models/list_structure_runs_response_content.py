from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.structure_run_detail import StructureRunDetail


T = TypeVar("T", bound="ListStructureRunsResponseContent")


@_attrs_define
class ListStructureRunsResponseContent:
    """
    Attributes:
        pagination (Pagination):
        structure_runs (list['StructureRunDetail']):
    """

    pagination: "Pagination"
    structure_runs: list["StructureRunDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        structure_runs = []
        for structure_runs_item_data in self.structure_runs:
            structure_runs_item = structure_runs_item_data.to_dict()
            structure_runs.append(structure_runs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "structure_runs": structure_runs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.structure_run_detail import StructureRunDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        structure_runs = []
        _structure_runs = d.pop("structure_runs")
        for structure_runs_item_data in _structure_runs:
            structure_runs_item = StructureRunDetail.from_dict(structure_runs_item_data)

            structure_runs.append(structure_runs_item)

        list_structure_runs_response_content = cls(
            pagination=pagination,
            structure_runs=structure_runs,
        )

        list_structure_runs_response_content.additional_properties = d
        return list_structure_runs_response_content

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
