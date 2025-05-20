from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_detail import WebhookDetail


T = TypeVar("T", bound="IntegrationConfigUnionType2")


@_attrs_define
class IntegrationConfigUnionType2:
    """
    Attributes:
        webhook (WebhookDetail):
    """

    webhook: "WebhookDetail"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook = self.webhook.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhook": webhook,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_detail import WebhookDetail

        d = dict(src_dict)
        webhook = WebhookDetail.from_dict(d.pop("webhook"))

        integration_config_union_type_2 = cls(
            webhook=webhook,
        )

        integration_config_union_type_2.additional_properties = d
        return integration_config_union_type_2

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
