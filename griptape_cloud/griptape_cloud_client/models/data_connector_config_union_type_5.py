from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_lake_connector_detail import DataLakeConnectorDetail


T = TypeVar("T", bound="DataConnectorConfigUnionType5")


@_attrs_define
class DataConnectorConfigUnionType5:
    """
    Attributes:
        data_lake (DataLakeConnectorDetail):
    """

    data_lake: "DataLakeConnectorDetail"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_lake = self.data_lake.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_lake": data_lake,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_lake_connector_detail import DataLakeConnectorDetail

        d = dict(src_dict)
        data_lake = DataLakeConnectorDetail.from_dict(d.pop("data_lake"))

        data_connector_config_union_type_5 = cls(
            data_lake=data_lake,
        )

        data_connector_config_union_type_5.additional_properties = d
        return data_connector_config_union_type_5

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
