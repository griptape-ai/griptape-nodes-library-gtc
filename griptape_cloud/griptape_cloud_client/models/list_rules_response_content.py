from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.rule_detail import RuleDetail


T = TypeVar("T", bound="ListRulesResponseContent")


@_attrs_define
class ListRulesResponseContent:
    """
    Attributes:
        pagination (Pagination):
        rules (list['RuleDetail']):
    """

    pagination: "Pagination"
    rules: list["RuleDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.rule_detail import RuleDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = RuleDetail.from_dict(rules_item_data)

            rules.append(rules_item)

        list_rules_response_content = cls(
            pagination=pagination,
            rules=rules,
        )

        list_rules_response_content.additional_properties = d
        return list_rules_response_content

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
