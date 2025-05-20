from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_credentials_input_type_0 import ConnectionCredentialsInputType0


T = TypeVar("T", bound="CreateConnectionRequestContent")


@_attrs_define
class CreateConnectionRequestContent:
    """
    Attributes:
        credentials ('ConnectionCredentialsInputType0'):
        type_ (str):
        name (Union[Unset, str]):
    """

    credentials: "ConnectionCredentialsInputType0"
    type_: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_credentials_input_type_0 import ConnectionCredentialsInputType0

        credentials: dict[str, Any]
        if isinstance(self.credentials, ConnectionCredentialsInputType0):
            credentials = self.credentials.to_dict()

        type_ = self.type_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_credentials_input_type_0 import ConnectionCredentialsInputType0

        d = dict(src_dict)

        def _parse_credentials(data: object) -> "ConnectionCredentialsInputType0":
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_connection_credentials_input_type_0 = ConnectionCredentialsInputType0.from_dict(data)

            return componentsschemas_connection_credentials_input_type_0

        credentials = _parse_credentials(d.pop("credentials"))

        type_ = d.pop("type")

        name = d.pop("name", UNSET)

        create_connection_request_content = cls(
            credentials=credentials,
            type_=type_,
            name=name,
        )

        create_connection_request_content.additional_properties = d
        return create_connection_request_content

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
