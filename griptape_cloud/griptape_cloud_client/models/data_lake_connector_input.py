from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataLakeConnectorInput")


@_attrs_define
class DataLakeConnectorInput:
    """
    Attributes:
        bucket_id (str):
        asset_paths (Union[Unset, list[str]]):
    """

    bucket_id: str
    asset_paths: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_id = self.bucket_id

        asset_paths: Union[Unset, list[str]] = UNSET
        if not isinstance(self.asset_paths, Unset):
            asset_paths = self.asset_paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_id": bucket_id,
            }
        )
        if asset_paths is not UNSET:
            field_dict["asset_paths"] = asset_paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_id = d.pop("bucket_id")

        asset_paths = cast(list[str], d.pop("asset_paths", UNSET))

        data_lake_connector_input = cls(
            bucket_id=bucket_id,
            asset_paths=asset_paths,
        )

        data_lake_connector_input.additional_properties = d
        return data_lake_connector_input

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
