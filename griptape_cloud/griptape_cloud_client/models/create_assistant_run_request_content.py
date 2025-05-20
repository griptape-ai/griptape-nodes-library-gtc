from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAssistantRunRequestContent")


@_attrs_define
class CreateAssistantRunRequestContent:
    """
    Attributes:
        additional_knowledge_base_ids (Union[Unset, list[str]]):
        additional_retriever_ids (Union[Unset, list[str]]):
        additional_ruleset_ids (Union[Unset, list[str]]):
        additional_structure_ids (Union[Unset, list[str]]):
        additional_tool_ids (Union[Unset, list[str]]):
        args (Union[Unset, list[str]]):
        input_ (Union[Unset, str]):
        knowledge_base_ids (Union[Unset, list[str]]):
        new_thread (Union[Unset, bool]): If true, create a new thread for this run to be returned in the response
            thread_id.
        retriever_ids (Union[Unset, list[str]]):
        ruleset_ids (Union[Unset, list[str]]):
        stream (Union[Unset, bool]):
        structure_ids (Union[Unset, list[str]]):
        thread_id (Union[Unset, str]): If provided, the run will be associated with the given thread. This takes
            precedence over new_thread.
        tool_ids (Union[Unset, list[str]]):
    """

    additional_knowledge_base_ids: Union[Unset, list[str]] = UNSET
    additional_retriever_ids: Union[Unset, list[str]] = UNSET
    additional_ruleset_ids: Union[Unset, list[str]] = UNSET
    additional_structure_ids: Union[Unset, list[str]] = UNSET
    additional_tool_ids: Union[Unset, list[str]] = UNSET
    args: Union[Unset, list[str]] = UNSET
    input_: Union[Unset, str] = UNSET
    knowledge_base_ids: Union[Unset, list[str]] = UNSET
    new_thread: Union[Unset, bool] = UNSET
    retriever_ids: Union[Unset, list[str]] = UNSET
    ruleset_ids: Union[Unset, list[str]] = UNSET
    stream: Union[Unset, bool] = UNSET
    structure_ids: Union[Unset, list[str]] = UNSET
    thread_id: Union[Unset, str] = UNSET
    tool_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_knowledge_base_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.additional_knowledge_base_ids, Unset):
            additional_knowledge_base_ids = self.additional_knowledge_base_ids

        additional_retriever_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.additional_retriever_ids, Unset):
            additional_retriever_ids = self.additional_retriever_ids

        additional_ruleset_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.additional_ruleset_ids, Unset):
            additional_ruleset_ids = self.additional_ruleset_ids

        additional_structure_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.additional_structure_ids, Unset):
            additional_structure_ids = self.additional_structure_ids

        additional_tool_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.additional_tool_ids, Unset):
            additional_tool_ids = self.additional_tool_ids

        args: Union[Unset, list[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        input_ = self.input_

        knowledge_base_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.knowledge_base_ids, Unset):
            knowledge_base_ids = self.knowledge_base_ids

        new_thread = self.new_thread

        retriever_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.retriever_ids, Unset):
            retriever_ids = self.retriever_ids

        ruleset_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ruleset_ids, Unset):
            ruleset_ids = self.ruleset_ids

        stream = self.stream

        structure_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.structure_ids, Unset):
            structure_ids = self.structure_ids

        thread_id = self.thread_id

        tool_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tool_ids, Unset):
            tool_ids = self.tool_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_knowledge_base_ids is not UNSET:
            field_dict["additional_knowledge_base_ids"] = additional_knowledge_base_ids
        if additional_retriever_ids is not UNSET:
            field_dict["additional_retriever_ids"] = additional_retriever_ids
        if additional_ruleset_ids is not UNSET:
            field_dict["additional_ruleset_ids"] = additional_ruleset_ids
        if additional_structure_ids is not UNSET:
            field_dict["additional_structure_ids"] = additional_structure_ids
        if additional_tool_ids is not UNSET:
            field_dict["additional_tool_ids"] = additional_tool_ids
        if args is not UNSET:
            field_dict["args"] = args
        if input_ is not UNSET:
            field_dict["input"] = input_
        if knowledge_base_ids is not UNSET:
            field_dict["knowledge_base_ids"] = knowledge_base_ids
        if new_thread is not UNSET:
            field_dict["new_thread"] = new_thread
        if retriever_ids is not UNSET:
            field_dict["retriever_ids"] = retriever_ids
        if ruleset_ids is not UNSET:
            field_dict["ruleset_ids"] = ruleset_ids
        if stream is not UNSET:
            field_dict["stream"] = stream
        if structure_ids is not UNSET:
            field_dict["structure_ids"] = structure_ids
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if tool_ids is not UNSET:
            field_dict["tool_ids"] = tool_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additional_knowledge_base_ids = cast(list[str], d.pop("additional_knowledge_base_ids", UNSET))

        additional_retriever_ids = cast(list[str], d.pop("additional_retriever_ids", UNSET))

        additional_ruleset_ids = cast(list[str], d.pop("additional_ruleset_ids", UNSET))

        additional_structure_ids = cast(list[str], d.pop("additional_structure_ids", UNSET))

        additional_tool_ids = cast(list[str], d.pop("additional_tool_ids", UNSET))

        args = cast(list[str], d.pop("args", UNSET))

        input_ = d.pop("input", UNSET)

        knowledge_base_ids = cast(list[str], d.pop("knowledge_base_ids", UNSET))

        new_thread = d.pop("new_thread", UNSET)

        retriever_ids = cast(list[str], d.pop("retriever_ids", UNSET))

        ruleset_ids = cast(list[str], d.pop("ruleset_ids", UNSET))

        stream = d.pop("stream", UNSET)

        structure_ids = cast(list[str], d.pop("structure_ids", UNSET))

        thread_id = d.pop("thread_id", UNSET)

        tool_ids = cast(list[str], d.pop("tool_ids", UNSET))

        create_assistant_run_request_content = cls(
            additional_knowledge_base_ids=additional_knowledge_base_ids,
            additional_retriever_ids=additional_retriever_ids,
            additional_ruleset_ids=additional_ruleset_ids,
            additional_structure_ids=additional_structure_ids,
            additional_tool_ids=additional_tool_ids,
            args=args,
            input_=input_,
            knowledge_base_ids=knowledge_base_ids,
            new_thread=new_thread,
            retriever_ids=retriever_ids,
            ruleset_ids=ruleset_ids,
            stream=stream,
            structure_ids=structure_ids,
            thread_id=thread_id,
            tool_ids=tool_ids,
        )

        create_assistant_run_request_content.additional_properties = d
        return create_assistant_run_request_content

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
