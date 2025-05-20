from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        page_number (float):
        page_size (float):
        total_count (float):
        total_pages (float):
        next_page (Union[Unset, float]):
        previous_page (Union[Unset, float]):
    """

    page_number: float
    page_size: float
    total_count: float
    total_pages: float
    next_page: Union[Unset, float] = UNSET
    previous_page: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_number = self.page_number

        page_size = self.page_size

        total_count = self.total_count

        total_pages = self.total_pages

        next_page = self.next_page

        previous_page = self.previous_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_number": page_number,
                "page_size": page_size,
                "total_count": total_count,
                "total_pages": total_pages,
            }
        )
        if next_page is not UNSET:
            field_dict["next_page"] = next_page
        if previous_page is not UNSET:
            field_dict["previous_page"] = previous_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_number = d.pop("page_number")

        page_size = d.pop("page_size")

        total_count = d.pop("total_count")

        total_pages = d.pop("total_pages")

        next_page = d.pop("next_page", UNSET)

        previous_page = d.pop("previous_page", UNSET)

        pagination = cls(
            page_number=page_number,
            page_size=page_size,
            total_count=total_count,
            total_pages=total_pages,
            next_page=next_page,
            previous_page=previous_page,
        )

        pagination.additional_properties = d
        return pagination

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
