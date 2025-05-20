import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAssistantResponseContent")


@_attrs_define
class UpdateAssistantResponseContent:
    """
    Attributes:
        assistant_id (str):
        created_at (datetime.datetime):
        created_by (str):
        description (str):
        knowledge_base_ids (list[str]):
        name (str):
        organization_id (str):
        retriever_ids (list[str]):
        ruleset_ids (list[str]):
        structure_ids (list[str]):
        tool_ids (list[str]):
        updated_at (datetime.datetime):
        input_ (Union[Unset, str]):
    """

    assistant_id: str
    created_at: datetime.datetime
    created_by: str
    description: str
    knowledge_base_ids: list[str]
    name: str
    organization_id: str
    retriever_ids: list[str]
    ruleset_ids: list[str]
    structure_ids: list[str]
    tool_ids: list[str]
    updated_at: datetime.datetime
    input_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistant_id = self.assistant_id

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        description = self.description

        knowledge_base_ids = self.knowledge_base_ids

        name = self.name

        organization_id = self.organization_id

        retriever_ids = self.retriever_ids

        ruleset_ids = self.ruleset_ids

        structure_ids = self.structure_ids

        tool_ids = self.tool_ids

        updated_at = self.updated_at.isoformat()

        input_ = self.input_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistant_id": assistant_id,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "knowledge_base_ids": knowledge_base_ids,
                "name": name,
                "organization_id": organization_id,
                "retriever_ids": retriever_ids,
                "ruleset_ids": ruleset_ids,
                "structure_ids": structure_ids,
                "tool_ids": tool_ids,
                "updated_at": updated_at,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assistant_id = d.pop("assistant_id")

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        description = d.pop("description")

        knowledge_base_ids = cast(list[str], d.pop("knowledge_base_ids"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        retriever_ids = cast(list[str], d.pop("retriever_ids"))

        ruleset_ids = cast(list[str], d.pop("ruleset_ids"))

        structure_ids = cast(list[str], d.pop("structure_ids"))

        tool_ids = cast(list[str], d.pop("tool_ids"))

        updated_at = isoparse(d.pop("updated_at"))

        input_ = d.pop("input", UNSET)

        update_assistant_response_content = cls(
            assistant_id=assistant_id,
            created_at=created_at,
            created_by=created_by,
            description=description,
            knowledge_base_ids=knowledge_base_ids,
            name=name,
            organization_id=organization_id,
            retriever_ids=retriever_ids,
            ruleset_ids=ruleset_ids,
            structure_ids=structure_ids,
            tool_ids=tool_ids,
            updated_at=updated_at,
            input_=input_,
        )

        update_assistant_response_content.additional_properties = d
        return update_assistant_response_content

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
