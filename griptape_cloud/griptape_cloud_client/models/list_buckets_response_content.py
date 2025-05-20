from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bucket_detail import BucketDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListBucketsResponseContent")


@_attrs_define
class ListBucketsResponseContent:
    """
    Attributes:
        buckets (list['BucketDetail']):
        pagination (Pagination):
    """

    buckets: list["BucketDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buckets = []
        for buckets_item_data in self.buckets:
            buckets_item = buckets_item_data.to_dict()
            buckets.append(buckets_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buckets": buckets,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_detail import BucketDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        buckets = []
        _buckets = d.pop("buckets")
        for buckets_item_data in _buckets:
            buckets_item = BucketDetail.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_buckets_response_content = cls(
            buckets=buckets,
            pagination=pagination,
        )

        list_buckets_response_content.additional_properties = d
        return list_buckets_response_content

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
