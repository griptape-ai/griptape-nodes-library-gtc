from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.thread_detail import ThreadDetail


T = TypeVar("T", bound="ListThreadsResponseContent")


@_attrs_define
class ListThreadsResponseContent:
    """
    Attributes:
        pagination (Pagination):
        threads (list['ThreadDetail']):
    """

    pagination: "Pagination"
    threads: list["ThreadDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        threads = []
        for threads_item_data in self.threads:
            threads_item = threads_item_data.to_dict()
            threads.append(threads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "threads": threads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.thread_detail import ThreadDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        threads = []
        _threads = d.pop("threads")
        for threads_item_data in _threads:
            threads_item = ThreadDetail.from_dict(threads_item_data)

            threads.append(threads_item)

        list_threads_response_content = cls(
            pagination=pagination,
            threads=threads,
        )

        list_threads_response_content.additional_properties = d
        return list_threads_response_content

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
