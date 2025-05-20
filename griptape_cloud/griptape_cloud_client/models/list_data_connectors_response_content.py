from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_connector_detail import DataConnectorDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListDataConnectorsResponseContent")


@_attrs_define
class ListDataConnectorsResponseContent:
    """
    Attributes:
        data_connectors (list['DataConnectorDetail']):
        pagination (Pagination):
    """

    data_connectors: list["DataConnectorDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_connectors = []
        for data_connectors_item_data in self.data_connectors:
            data_connectors_item = data_connectors_item_data.to_dict()
            data_connectors.append(data_connectors_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_connectors": data_connectors,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_connector_detail import DataConnectorDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        data_connectors = []
        _data_connectors = d.pop("data_connectors")
        for data_connectors_item_data in _data_connectors:
            data_connectors_item = DataConnectorDetail.from_dict(data_connectors_item_data)

            data_connectors.append(data_connectors_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_data_connectors_response_content = cls(
            data_connectors=data_connectors,
            pagination=pagination,
        )

        list_data_connectors_response_content.additional_properties = d
        return list_data_connectors_response_content

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
