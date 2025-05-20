from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_connector_detail import S3ConnectorDetail


T = TypeVar("T", bound="DataConnectorConfigUnionType4")


@_attrs_define
class DataConnectorConfigUnionType4:
    """
    Attributes:
        s3 (S3ConnectorDetail):
    """

    s3: "S3ConnectorDetail"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s3 = self.s3.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s3": s3,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_connector_detail import S3ConnectorDetail

        d = dict(src_dict)
        s3 = S3ConnectorDetail.from_dict(d.pop("s3"))

        data_connector_config_union_type_4 = cls(
            s3=s3,
        )

        data_connector_config_union_type_4.additional_properties = d
        return data_connector_config_union_type_4

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
