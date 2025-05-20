from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.assistant_run_detail import AssistantRunDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListAssistantRunsResponseContent")


@_attrs_define
class ListAssistantRunsResponseContent:
    """
    Attributes:
        assistant_runs (list['AssistantRunDetail']):
        pagination (Pagination):
    """

    assistant_runs: list["AssistantRunDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistant_runs = []
        for assistant_runs_item_data in self.assistant_runs:
            assistant_runs_item = assistant_runs_item_data.to_dict()
            assistant_runs.append(assistant_runs_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistant_runs": assistant_runs,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assistant_run_detail import AssistantRunDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        assistant_runs = []
        _assistant_runs = d.pop("assistant_runs")
        for assistant_runs_item_data in _assistant_runs:
            assistant_runs_item = AssistantRunDetail.from_dict(assistant_runs_item_data)

            assistant_runs.append(assistant_runs_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_assistant_runs_response_content = cls(
            assistant_runs=assistant_runs,
            pagination=pagination,
        )

        list_assistant_runs_response_content.additional_properties = d
        return list_assistant_runs_response_content

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
