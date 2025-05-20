from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAssistantRequestContent")


@_attrs_define
class UpdateAssistantRequestContent:
    """
    Attributes:
        description (Union[Unset, str]):
        input_ (Union[Unset, str]):
        knowledge_base_ids (Union[Unset, list[str]]):
        name (Union[Unset, str]):
        ruleset_ids (Union[Unset, list[str]]):
        structure_ids (Union[Unset, list[str]]):
        tool_ids (Union[Unset, list[str]]):
    """

    description: Union[Unset, str] = UNSET
    input_: Union[Unset, str] = UNSET
    knowledge_base_ids: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    ruleset_ids: Union[Unset, list[str]] = UNSET
    structure_ids: Union[Unset, list[str]] = UNSET
    tool_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        input_ = self.input_

        knowledge_base_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.knowledge_base_ids, Unset):
            knowledge_base_ids = self.knowledge_base_ids

        name = self.name

        ruleset_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ruleset_ids, Unset):
            ruleset_ids = self.ruleset_ids

        structure_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.structure_ids, Unset):
            structure_ids = self.structure_ids

        tool_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tool_ids, Unset):
            tool_ids = self.tool_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if input_ is not UNSET:
            field_dict["input"] = input_
        if knowledge_base_ids is not UNSET:
            field_dict["knowledge_base_ids"] = knowledge_base_ids
        if name is not UNSET:
            field_dict["name"] = name
        if ruleset_ids is not UNSET:
            field_dict["ruleset_ids"] = ruleset_ids
        if structure_ids is not UNSET:
            field_dict["structure_ids"] = structure_ids
        if tool_ids is not UNSET:
            field_dict["tool_ids"] = tool_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        input_ = d.pop("input", UNSET)

        knowledge_base_ids = cast(list[str], d.pop("knowledge_base_ids", UNSET))

        name = d.pop("name", UNSET)

        ruleset_ids = cast(list[str], d.pop("ruleset_ids", UNSET))

        structure_ids = cast(list[str], d.pop("structure_ids", UNSET))

        tool_ids = cast(list[str], d.pop("tool_ids", UNSET))

        update_assistant_request_content = cls(
            description=description,
            input_=input_,
            knowledge_base_ids=knowledge_base_ids,
            name=name,
            ruleset_ids=ruleset_ids,
            structure_ids=structure_ids,
            tool_ids=tool_ids,
        )

        update_assistant_request_content.additional_properties = d
        return update_assistant_request_content

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
