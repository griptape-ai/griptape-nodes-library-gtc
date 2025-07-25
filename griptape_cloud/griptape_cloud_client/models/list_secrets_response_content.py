from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.secret_detail import SecretDetail


T = TypeVar("T", bound="ListSecretsResponseContent")


@_attrs_define
class ListSecretsResponseContent:
    """
    Attributes:
        pagination (Pagination):
        secrets (list['SecretDetail']):
    """

    pagination: "Pagination"
    secrets: list["SecretDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        secrets = []
        for secrets_item_data in self.secrets:
            secrets_item = secrets_item_data.to_dict()
            secrets.append(secrets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "secrets": secrets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.secret_detail import SecretDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        secrets = []
        _secrets = d.pop("secrets")
        for secrets_item_data in _secrets:
            secrets_item = SecretDetail.from_dict(secrets_item_data)

            secrets.append(secrets_item)

        list_secrets_response_content = cls(
            pagination=pagination,
            secrets=secrets,
        )

        list_secrets_response_content.additional_properties = d
        return list_secrets_response_content

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
