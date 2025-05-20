from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.retriever_detail import RetrieverDetail


T = TypeVar("T", bound="ListRetrieversResponseContent")


@_attrs_define
class ListRetrieversResponseContent:
    """
    Attributes:
        pagination (Pagination):
        retrievers (list['RetrieverDetail']):
    """

    pagination: "Pagination"
    retrievers: list["RetrieverDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        retrievers = []
        for retrievers_item_data in self.retrievers:
            retrievers_item = retrievers_item_data.to_dict()
            retrievers.append(retrievers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "retrievers": retrievers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.retriever_detail import RetrieverDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        retrievers = []
        _retrievers = d.pop("retrievers")
        for retrievers_item_data in _retrievers:
            retrievers_item = RetrieverDetail.from_dict(retrievers_item_data)

            retrievers.append(retrievers_item)

        list_retrievers_response_content = cls(
            pagination=pagination,
            retrievers=retrievers,
        )

        list_retrievers_response_content.additional_properties = d
        return list_retrievers_response_content

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
