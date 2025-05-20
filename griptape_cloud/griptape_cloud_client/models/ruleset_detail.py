import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="RulesetDetail")


@_attrs_define
class RulesetDetail:
    """
    Attributes:
        alias (str):
        created_at (datetime.datetime):
        created_by (str):
        description (str):
        metadata (Metadata):
        name (str):
        organization_id (str):
        rule_ids (list[str]):
        ruleset_id (str):
        updated_at (datetime.datetime):
    """

    alias: str
    created_at: datetime.datetime
    created_by: str
    description: str
    metadata: "Metadata"
    name: str
    organization_id: str
    rule_ids: list[str]
    ruleset_id: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        description = self.description

        metadata = self.metadata.to_dict()

        name = self.name

        organization_id = self.organization_id

        rule_ids = self.rule_ids

        ruleset_id = self.ruleset_id

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias": alias,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "metadata": metadata,
                "name": name,
                "organization_id": organization_id,
                "rule_ids": rule_ids,
                "ruleset_id": ruleset_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        alias = d.pop("alias")

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        description = d.pop("description")

        metadata = Metadata.from_dict(d.pop("metadata"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        rule_ids = cast(list[str], d.pop("rule_ids"))

        ruleset_id = d.pop("ruleset_id")

        updated_at = isoparse(d.pop("updated_at"))

        ruleset_detail = cls(
            alias=alias,
            created_at=created_at,
            created_by=created_by,
            description=description,
            metadata=metadata,
            name=name,
            organization_id=organization_id,
            rule_ids=rule_ids,
            ruleset_id=ruleset_id,
            updated_at=updated_at,
        )

        ruleset_detail.additional_properties = d
        return ruleset_detail

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
