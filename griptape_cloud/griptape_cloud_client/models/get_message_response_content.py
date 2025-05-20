import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.metadata import Metadata


T = TypeVar("T", bound="GetMessageResponseContent")


@_attrs_define
class GetMessageResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        index (float):
        input_ (str):
        message_id (str):
        metadata (Metadata):
        output (str):
        thread_id (str):
        updated_at (datetime.datetime):
    """

    created_at: datetime.datetime
    created_by: str
    index: float
    input_: str
    message_id: str
    metadata: "Metadata"
    output: str
    thread_id: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        index = self.index

        input_ = self.input_

        message_id = self.message_id

        metadata = self.metadata.to_dict()

        output = self.output

        thread_id = self.thread_id

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "index": index,
                "input": input_,
                "message_id": message_id,
                "metadata": metadata,
                "output": output,
                "thread_id": thread_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata import Metadata

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        index = d.pop("index")

        input_ = d.pop("input")

        message_id = d.pop("message_id")

        metadata = Metadata.from_dict(d.pop("metadata"))

        output = d.pop("output")

        thread_id = d.pop("thread_id")

        updated_at = isoparse(d.pop("updated_at"))

        get_message_response_content = cls(
            created_at=created_at,
            created_by=created_by,
            index=index,
            input_=input_,
            message_id=message_id,
            metadata=metadata,
            output=output,
            thread_id=thread_id,
            updated_at=updated_at,
        )

        get_message_response_content.additional_properties = d
        return get_message_response_content

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
