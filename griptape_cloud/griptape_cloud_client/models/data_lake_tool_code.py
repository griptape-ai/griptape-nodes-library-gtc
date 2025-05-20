from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataLakeToolCode")


@_attrs_define
class DataLakeToolCode:
    """
    Attributes:
        asset_path (str):
        bucket_id (str):
    """

    asset_path: str
    bucket_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_path = self.asset_path

        bucket_id = self.bucket_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_path": asset_path,
                "bucket_id": bucket_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_path = d.pop("asset_path")

        bucket_id = d.pop("bucket_id")

        data_lake_tool_code = cls(
            asset_path=asset_path,
            bucket_id=bucket_id,
        )

        data_lake_tool_code.additional_properties = d
        return data_lake_tool_code

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
