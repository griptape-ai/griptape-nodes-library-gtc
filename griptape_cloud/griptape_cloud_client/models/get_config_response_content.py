from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetConfigResponseContent")


@_attrs_define
class GetConfigResponseContent:
    """
    Attributes:
        data_lake_s3_bucket (str):
        data_lake_s3_region (str):
        data_lake_s3_url (str):
        google_drive_data_connector_client_id (str):
    """

    data_lake_s3_bucket: str
    data_lake_s3_region: str
    data_lake_s3_url: str
    google_drive_data_connector_client_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_lake_s3_bucket = self.data_lake_s3_bucket

        data_lake_s3_region = self.data_lake_s3_region

        data_lake_s3_url = self.data_lake_s3_url

        google_drive_data_connector_client_id = self.google_drive_data_connector_client_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_lake_s3_bucket": data_lake_s3_bucket,
                "data_lake_s3_region": data_lake_s3_region,
                "data_lake_s3_url": data_lake_s3_url,
                "google_drive_data_connector_client_id": google_drive_data_connector_client_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_lake_s3_bucket = d.pop("data_lake_s3_bucket")

        data_lake_s3_region = d.pop("data_lake_s3_region")

        data_lake_s3_url = d.pop("data_lake_s3_url")

        google_drive_data_connector_client_id = d.pop("google_drive_data_connector_client_id")

        get_config_response_content = cls(
            data_lake_s3_bucket=data_lake_s3_bucket,
            data_lake_s3_region=data_lake_s3_region,
            data_lake_s3_url=data_lake_s3_url,
            google_drive_data_connector_client_id=google_drive_data_connector_client_id,
        )

        get_config_response_content.additional_properties = d
        return get_config_response_content

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
