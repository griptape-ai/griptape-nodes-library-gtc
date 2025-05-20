from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_key_detail import ApiKeyDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListApiKeysResponseContent")


@_attrs_define
class ListApiKeysResponseContent:
    """
    Attributes:
        api_keys (list['ApiKeyDetail']):
        pagination (Pagination):
    """

    api_keys: list["ApiKeyDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_keys = []
        for api_keys_item_data in self.api_keys:
            api_keys_item = api_keys_item_data.to_dict()
            api_keys.append(api_keys_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_keys": api_keys,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_detail import ApiKeyDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        api_keys = []
        _api_keys = d.pop("api_keys")
        for api_keys_item_data in _api_keys:
            api_keys_item = ApiKeyDetail.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_api_keys_response_content = cls(
            api_keys=api_keys,
            pagination=pagination,
        )

        list_api_keys_response_content.additional_properties = d
        return list_api_keys_response_content

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
