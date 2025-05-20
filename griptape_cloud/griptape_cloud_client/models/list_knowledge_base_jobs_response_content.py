from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.knowledge_base_job_detail import KnowledgeBaseJobDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListKnowledgeBaseJobsResponseContent")


@_attrs_define
class ListKnowledgeBaseJobsResponseContent:
    """
    Attributes:
        knowledge_base_jobs (list['KnowledgeBaseJobDetail']):
        pagination (Pagination):
    """

    knowledge_base_jobs: list["KnowledgeBaseJobDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        knowledge_base_jobs = []
        for knowledge_base_jobs_item_data in self.knowledge_base_jobs:
            knowledge_base_jobs_item = knowledge_base_jobs_item_data.to_dict()
            knowledge_base_jobs.append(knowledge_base_jobs_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "knowledge_base_jobs": knowledge_base_jobs,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knowledge_base_job_detail import KnowledgeBaseJobDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        knowledge_base_jobs = []
        _knowledge_base_jobs = d.pop("knowledge_base_jobs")
        for knowledge_base_jobs_item_data in _knowledge_base_jobs:
            knowledge_base_jobs_item = KnowledgeBaseJobDetail.from_dict(knowledge_base_jobs_item_data)

            knowledge_base_jobs.append(knowledge_base_jobs_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_knowledge_base_jobs_response_content = cls(
            knowledge_base_jobs=knowledge_base_jobs,
            pagination=pagination,
        )

        list_knowledge_base_jobs_response_content.additional_properties = d
        return list_knowledge_base_jobs_response_content

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
