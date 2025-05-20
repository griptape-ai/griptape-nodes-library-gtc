from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.retriever_component_detail import RetrieverComponentDetail


T = TypeVar("T", bound="ListRetrieverComponentsResponseContent")


@_attrs_define
class ListRetrieverComponentsResponseContent:
    """
    Attributes:
        pagination (Pagination):
        retriever_components (list['RetrieverComponentDetail']):
    """

    pagination: "Pagination"
    retriever_components: list["RetrieverComponentDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        retriever_components = []
        for retriever_components_item_data in self.retriever_components:
            retriever_components_item = retriever_components_item_data.to_dict()
            retriever_components.append(retriever_components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "retriever_components": retriever_components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.retriever_component_detail import RetrieverComponentDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        retriever_components = []
        _retriever_components = d.pop("retriever_components")
        for retriever_components_item_data in _retriever_components:
            retriever_components_item = RetrieverComponentDetail.from_dict(retriever_components_item_data)

            retriever_components.append(retriever_components_item)

        list_retriever_components_response_content = cls(
            pagination=pagination,
            retriever_components=retriever_components,
        )

        list_retriever_components_response_content.additional_properties = d
        return list_retriever_components_response_content

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
