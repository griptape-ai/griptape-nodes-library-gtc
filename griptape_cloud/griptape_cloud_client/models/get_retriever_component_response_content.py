import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetRetrieverComponentResponseContent")


@_attrs_define
class GetRetrieverComponentResponseContent:
    """
    Attributes:
        config (Any):
        created_at (datetime.datetime):
        created_by (str):
        name (str):
        organization_id (str):
        retriever_component_id (str):
        type_ (str):
        updated_at (datetime.datetime):
        description (Union[Unset, str]):
    """

    config: Any
    created_at: datetime.datetime
    created_by: str
    name: str
    organization_id: str
    retriever_component_id: str
    type_: str
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        name = self.name

        organization_id = self.organization_id

        retriever_component_id = self.retriever_component_id

        type_ = self.type_

        updated_at = self.updated_at.isoformat()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "created_at": created_at,
                "created_by": created_by,
                "name": name,
                "organization_id": organization_id,
                "retriever_component_id": retriever_component_id,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config = d.pop("config")

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        retriever_component_id = d.pop("retriever_component_id")

        type_ = d.pop("type")

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        get_retriever_component_response_content = cls(
            config=config,
            created_at=created_at,
            created_by=created_by,
            name=name,
            organization_id=organization_id,
            retriever_component_id=retriever_component_id,
            type_=type_,
            updated_at=updated_at,
            description=description,
        )

        get_retriever_component_response_content.additional_properties = d
        return get_retriever_component_response_content

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
