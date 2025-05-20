from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.integration_detail import IntegrationDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListIntegrationsResponseContent")


@_attrs_define
class ListIntegrationsResponseContent:
    """
    Attributes:
        integrations (list['IntegrationDetail']):
        pagination (Pagination):
    """

    integrations: list["IntegrationDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integrations = []
        for integrations_item_data in self.integrations:
            integrations_item = integrations_item_data.to_dict()
            integrations.append(integrations_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integrations": integrations,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_detail import IntegrationDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        integrations = []
        _integrations = d.pop("integrations")
        for integrations_item_data in _integrations:
            integrations_item = IntegrationDetail.from_dict(integrations_item_data)

            integrations.append(integrations_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_integrations_response_content = cls(
            integrations=integrations,
            pagination=pagination,
        )

        list_integrations_response_content.additional_properties = d
        return list_integrations_response_content

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
