from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3ConnectorDetail")


@_attrs_define
class S3ConnectorDetail:
    """
    Attributes:
        aws_access_key_id (str):
        uris (list[str]):
    """

    aws_access_key_id: str
    uris: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_access_key_id = self.aws_access_key_id

        uris = self.uris

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aws_access_key_id": aws_access_key_id,
                "uris": uris,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aws_access_key_id = d.pop("aws_access_key_id")

        uris = cast(list[str], d.pop("uris"))

        s3_connector_detail = cls(
            aws_access_key_id=aws_access_key_id,
            uris=uris,
        )

        s3_connector_detail.additional_properties = d
        return s3_connector_detail

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
