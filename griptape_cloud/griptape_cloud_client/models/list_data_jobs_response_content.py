from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_job_detail import DataJobDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListDataJobsResponseContent")


@_attrs_define
class ListDataJobsResponseContent:
    """
    Attributes:
        data_jobs (list['DataJobDetail']):
        pagination (Pagination):
    """

    data_jobs: list["DataJobDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_jobs = []
        for data_jobs_item_data in self.data_jobs:
            data_jobs_item = data_jobs_item_data.to_dict()
            data_jobs.append(data_jobs_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_jobs": data_jobs,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_job_detail import DataJobDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        data_jobs = []
        _data_jobs = d.pop("data_jobs")
        for data_jobs_item_data in _data_jobs:
            data_jobs_item = DataJobDetail.from_dict(data_jobs_item_data)

            data_jobs.append(data_jobs_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_data_jobs_response_content = cls(
            data_jobs=data_jobs,
            pagination=pagination,
        )

        list_data_jobs_response_content.additional_properties = d
        return list_data_jobs_response_content

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
