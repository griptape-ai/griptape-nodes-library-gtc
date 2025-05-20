from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.library_detail import LibraryDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListLibrariesResponseContent")


@_attrs_define
class ListLibrariesResponseContent:
    """
    Attributes:
        libraries (list['LibraryDetail']):
        pagination (Pagination):
    """

    libraries: list["LibraryDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        libraries = []
        for libraries_item_data in self.libraries:
            libraries_item = libraries_item_data.to_dict()
            libraries.append(libraries_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "libraries": libraries,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_detail import LibraryDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        libraries = []
        _libraries = d.pop("libraries")
        for libraries_item_data in _libraries:
            libraries_item = LibraryDetail.from_dict(libraries_item_data)

            libraries.append(libraries_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_libraries_response_content = cls(
            libraries=libraries,
            pagination=pagination,
        )

        list_libraries_response_content.additional_properties = d
        return list_libraries_response_content

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
