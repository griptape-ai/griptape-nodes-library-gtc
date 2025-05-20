import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetDetail")


@_attrs_define
class AssetDetail:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        name (str):
        organization_id (str):
        updated_at (datetime.datetime):
        bucket_id (Union[Unset, str]):
        contents (Union[Unset, Any]):
        size (Union[Unset, float]):
    """

    created_at: datetime.datetime
    created_by: str
    name: str
    organization_id: str
    updated_at: datetime.datetime
    bucket_id: Union[Unset, str] = UNSET
    contents: Union[Unset, Any] = UNSET
    size: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        name = self.name

        organization_id = self.organization_id

        updated_at = self.updated_at.isoformat()

        bucket_id = self.bucket_id

        contents = self.contents

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "name": name,
                "organization_id": organization_id,
                "updated_at": updated_at,
            }
        )
        if bucket_id is not UNSET:
            field_dict["bucket_id"] = bucket_id
        if contents is not UNSET:
            field_dict["contents"] = contents
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        updated_at = isoparse(d.pop("updated_at"))

        bucket_id = d.pop("bucket_id", UNSET)

        contents = d.pop("contents", UNSET)

        size = d.pop("size", UNSET)

        asset_detail = cls(
            created_at=created_at,
            created_by=created_by,
            name=name,
            organization_id=organization_id,
            updated_at=updated_at,
            bucket_id=bucket_id,
            contents=contents,
            size=size,
        )

        asset_detail.additional_properties = d
        return asset_detail

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
