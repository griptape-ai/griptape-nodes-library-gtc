from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.function_run_detail import FunctionRunDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListFunctionRunsResponseContent")


@_attrs_define
class ListFunctionRunsResponseContent:
    """
    Attributes:
        function_runs (list['FunctionRunDetail']):
        pagination (Pagination):
    """

    function_runs: list["FunctionRunDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function_runs = []
        for function_runs_item_data in self.function_runs:
            function_runs_item = function_runs_item_data.to_dict()
            function_runs.append(function_runs_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function_runs": function_runs,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_run_detail import FunctionRunDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        function_runs = []
        _function_runs = d.pop("function_runs")
        for function_runs_item_data in _function_runs:
            function_runs_item = FunctionRunDetail.from_dict(function_runs_item_data)

            function_runs.append(function_runs_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_function_runs_response_content = cls(
            function_runs=function_runs,
            pagination=pagination,
        )

        list_function_runs_response_content.additional_properties = d
        return list_function_runs_response_content

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
