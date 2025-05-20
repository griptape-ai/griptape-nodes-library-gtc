import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryDetail")


@_attrs_define
class LibraryDetail:
    """
    Attributes:
        assistant_id (str):
        created_at (datetime.datetime):
        created_by (str):
        data_connector_ids (list[str]):
        knowledge_base_ids (list[str]):
        library_id (str):
        name (str):
        organization_id (str):
        retriever_id (str):
        updated_at (datetime.datetime):
        description (Union[Unset, str]):
    """

    assistant_id: str
    created_at: datetime.datetime
    created_by: str
    data_connector_ids: list[str]
    knowledge_base_ids: list[str]
    library_id: str
    name: str
    organization_id: str
    retriever_id: str
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistant_id = self.assistant_id

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        data_connector_ids = self.data_connector_ids

        knowledge_base_ids = self.knowledge_base_ids

        library_id = self.library_id

        name = self.name

        organization_id = self.organization_id

        retriever_id = self.retriever_id

        updated_at = self.updated_at.isoformat()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistant_id": assistant_id,
                "created_at": created_at,
                "created_by": created_by,
                "data_connector_ids": data_connector_ids,
                "knowledge_base_ids": knowledge_base_ids,
                "library_id": library_id,
                "name": name,
                "organization_id": organization_id,
                "retriever_id": retriever_id,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assistant_id = d.pop("assistant_id")

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        data_connector_ids = cast(list[str], d.pop("data_connector_ids"))

        knowledge_base_ids = cast(list[str], d.pop("knowledge_base_ids"))

        library_id = d.pop("library_id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        retriever_id = d.pop("retriever_id")

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        library_detail = cls(
            assistant_id=assistant_id,
            created_at=created_at,
            created_by=created_by,
            data_connector_ids=data_connector_ids,
            knowledge_base_ids=knowledge_base_ids,
            library_id=library_id,
            name=name,
            organization_id=organization_id,
            retriever_id=retriever_id,
            updated_at=updated_at,
            description=description,
        )

        library_detail.additional_properties = d
        return library_detail

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
