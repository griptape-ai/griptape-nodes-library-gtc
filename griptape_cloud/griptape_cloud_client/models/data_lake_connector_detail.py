from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataLakeConnectorDetail")


@_attrs_define
class DataLakeConnectorDetail:
    """
    Attributes:
        asset_paths (list[str]):
        bucket_id (str):
    """

    asset_paths: list[str]
    bucket_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_paths = self.asset_paths

        bucket_id = self.bucket_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_paths": asset_paths,
                "bucket_id": bucket_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_paths = cast(list[str], d.pop("asset_paths"))

        bucket_id = d.pop("bucket_id")

        data_lake_connector_detail = cls(
            asset_paths=asset_paths,
            bucket_id=bucket_id,
        )

        data_lake_connector_detail.additional_properties = d
        return data_lake_connector_detail

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
