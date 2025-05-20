import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.assistant_run_status import AssistantRunStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAssistantRunResponseContent")


@_attrs_define
class CreateAssistantRunResponseContent:
    """
    Attributes:
        args (list[str]):
        assistant_id (str):
        assistant_run_id (str):
        completed_at (Union[None, datetime.datetime]):
        created_at (datetime.datetime):
        created_by (str):
        knowledge_base_ids (list[str]):
        retriever_ids (list[str]):
        ruleset_ids (list[str]):
        status (AssistantRunStatus):
        stream (bool):
        structure_ids (list[str]):
        tool_ids (list[str]):
        updated_at (datetime.datetime):
        input_ (Union[Unset, str]):
        output (Union[Unset, Any]):
        status_detail (Union[Unset, Any]):
        thread_id (Union[Unset, str]):
    """

    args: list[str]
    assistant_id: str
    assistant_run_id: str
    completed_at: Union[None, datetime.datetime]
    created_at: datetime.datetime
    created_by: str
    knowledge_base_ids: list[str]
    retriever_ids: list[str]
    ruleset_ids: list[str]
    status: AssistantRunStatus
    stream: bool
    structure_ids: list[str]
    tool_ids: list[str]
    updated_at: datetime.datetime
    input_: Union[Unset, str] = UNSET
    output: Union[Unset, Any] = UNSET
    status_detail: Union[Unset, Any] = UNSET
    thread_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args = self.args

        assistant_id = self.assistant_id

        assistant_run_id = self.assistant_run_id

        completed_at: Union[None, str]
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        knowledge_base_ids = self.knowledge_base_ids

        retriever_ids = self.retriever_ids

        ruleset_ids = self.ruleset_ids

        status = self.status.value

        stream = self.stream

        structure_ids = self.structure_ids

        tool_ids = self.tool_ids

        updated_at = self.updated_at.isoformat()

        input_ = self.input_

        output = self.output

        status_detail = self.status_detail

        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "args": args,
                "assistant_id": assistant_id,
                "assistant_run_id": assistant_run_id,
                "completed_at": completed_at,
                "created_at": created_at,
                "created_by": created_by,
                "knowledge_base_ids": knowledge_base_ids,
                "retriever_ids": retriever_ids,
                "ruleset_ids": ruleset_ids,
                "status": status,
                "stream": stream,
                "structure_ids": structure_ids,
                "tool_ids": tool_ids,
                "updated_at": updated_at,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output
        if status_detail is not UNSET:
            field_dict["status_detail"] = status_detail
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        args = cast(list[str], d.pop("args"))

        assistant_id = d.pop("assistant_id")

        assistant_run_id = d.pop("assistant_run_id")

        def _parse_completed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        knowledge_base_ids = cast(list[str], d.pop("knowledge_base_ids"))

        retriever_ids = cast(list[str], d.pop("retriever_ids"))

        ruleset_ids = cast(list[str], d.pop("ruleset_ids"))

        status = AssistantRunStatus(d.pop("status"))

        stream = d.pop("stream")

        structure_ids = cast(list[str], d.pop("structure_ids"))

        tool_ids = cast(list[str], d.pop("tool_ids"))

        updated_at = isoparse(d.pop("updated_at"))

        input_ = d.pop("input", UNSET)

        output = d.pop("output", UNSET)

        status_detail = d.pop("status_detail", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        create_assistant_run_response_content = cls(
            args=args,
            assistant_id=assistant_id,
            assistant_run_id=assistant_run_id,
            completed_at=completed_at,
            created_at=created_at,
            created_by=created_by,
            knowledge_base_ids=knowledge_base_ids,
            retriever_ids=retriever_ids,
            ruleset_ids=ruleset_ids,
            status=status,
            stream=stream,
            structure_ids=structure_ids,
            tool_ids=tool_ids,
            updated_at=updated_at,
            input_=input_,
            output=output,
            status_detail=status_detail,
            thread_id=thread_id,
        )

        create_assistant_run_response_content.additional_properties = d
        return create_assistant_run_response_content

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
