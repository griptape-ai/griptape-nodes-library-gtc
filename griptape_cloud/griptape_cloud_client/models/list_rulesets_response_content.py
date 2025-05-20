from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.ruleset_detail import RulesetDetail


T = TypeVar("T", bound="ListRulesetsResponseContent")


@_attrs_define
class ListRulesetsResponseContent:
    """
    Attributes:
        pagination (Pagination):
        rulesets (list['RulesetDetail']):
    """

    pagination: "Pagination"
    rulesets: list["RulesetDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        rulesets = []
        for rulesets_item_data in self.rulesets:
            rulesets_item = rulesets_item_data.to_dict()
            rulesets.append(rulesets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "rulesets": rulesets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.ruleset_detail import RulesetDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        rulesets = []
        _rulesets = d.pop("rulesets")
        for rulesets_item_data in _rulesets:
            rulesets_item = RulesetDetail.from_dict(rulesets_item_data)

            rulesets.append(rulesets_item)

        list_rulesets_response_content = cls(
            pagination=pagination,
            rulesets=rulesets,
        )

        list_rulesets_response_content.additional_properties = d
        return list_rulesets_response_content

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
