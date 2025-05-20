from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.tool_run_detail import ToolRunDetail


T = TypeVar("T", bound="ListToolRunsResponseContent")


@_attrs_define
class ListToolRunsResponseContent:
    """
    Attributes:
        pagination (Pagination):
        tool_runs (list['ToolRunDetail']):
    """

    pagination: "Pagination"
    tool_runs: list["ToolRunDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        tool_runs = []
        for tool_runs_item_data in self.tool_runs:
            tool_runs_item = tool_runs_item_data.to_dict()
            tool_runs.append(tool_runs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "tool_runs": tool_runs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.tool_run_detail import ToolRunDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        tool_runs = []
        _tool_runs = d.pop("tool_runs")
        for tool_runs_item_data in _tool_runs:
            tool_runs_item = ToolRunDetail.from_dict(tool_runs_item_data)

            tool_runs.append(tool_runs_item)

        list_tool_runs_response_content = cls(
            pagination=pagination,
            tool_runs=tool_runs,
        )

        list_tool_runs_response_content.additional_properties = d
        return list_tool_runs_response_content

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
