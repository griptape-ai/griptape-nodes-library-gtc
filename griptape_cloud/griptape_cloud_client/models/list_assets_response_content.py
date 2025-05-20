from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_detail import AssetDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListAssetsResponseContent")


@_attrs_define
class ListAssetsResponseContent:
    """
    Attributes:
        assets (list['AssetDetail']):
        pagination (Pagination):
        postfix (Union[Unset, str]):
        prefix (Union[Unset, str]):
    """

    assets: list["AssetDetail"]
    pagination: "Pagination"
    postfix: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        pagination = self.pagination.to_dict()

        postfix = self.postfix

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assets": assets,
                "pagination": pagination,
            }
        )
        if postfix is not UNSET:
            field_dict["postfix"] = postfix
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_detail import AssetDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = AssetDetail.from_dict(assets_item_data)

            assets.append(assets_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        postfix = d.pop("postfix", UNSET)

        prefix = d.pop("prefix", UNSET)

        list_assets_response_content = cls(
            assets=assets,
            pagination=pagination,
            postfix=postfix,
            prefix=prefix,
        )

        list_assets_response_content.additional_properties = d
        return list_assets_response_content

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
