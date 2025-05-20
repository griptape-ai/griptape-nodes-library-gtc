from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="CreateRulesetRequestContent")


@_attrs_define
class CreateRulesetRequestContent:
    """
    Attributes:
        name (str):
        alias (Union[Unset, str]):
        description (Union[Unset, str]):
        metadata (Union[Unset, Metadata]):
        rule_ids (Union[Unset, list[str]]):
    """

    name: str
    alias: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    rule_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alias = self.alias

        description = self.description

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        rule_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.rule_ids, Unset):
            rule_ids = self.rule_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if rule_ids is not UNSET:
            field_dict["rule_ids"] = rule_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        name = d.pop("name")

        alias = d.pop("alias", UNSET)

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        rule_ids = cast(list[str], d.pop("rule_ids", UNSET))

        create_ruleset_request_content = cls(
            name=name,
            alias=alias,
            description=description,
            metadata=metadata,
            rule_ids=rule_ids,
        )

        create_ruleset_request_content.additional_properties = d
        return create_ruleset_request_content

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
