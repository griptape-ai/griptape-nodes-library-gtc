from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assert_url_operation import AssertUrlOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAssetUrlRequestContent")


@_attrs_define
class CreateAssetUrlRequestContent:
    """
    Attributes:
        operation (Union[Unset, AssertUrlOperation]):
    """

    operation: Union[Unset, AssertUrlOperation] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, AssertUrlOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = AssertUrlOperation(_operation)

        create_asset_url_request_content = cls(
            operation=operation,
        )

        create_asset_url_request_content.additional_properties = d
        return create_asset_url_request_content

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
