import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retriever_component_detail import RetrieverComponentDetail


T = TypeVar("T", bound="GetRetrieverResponseContent")


@_attrs_define
class GetRetrieverResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        name (str):
        organization_id (str):
        retriever_components (list['RetrieverComponentDetail']):
        retriever_components_schema (Any):
        retriever_id (str):
        updated_at (datetime.datetime):
        description (Union[Unset, str]):
    """

    created_at: datetime.datetime
    created_by: str
    name: str
    organization_id: str
    retriever_components: list["RetrieverComponentDetail"]
    retriever_components_schema: Any
    retriever_id: str
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        name = self.name

        organization_id = self.organization_id

        retriever_components = []
        for retriever_components_item_data in self.retriever_components:
            retriever_components_item = retriever_components_item_data.to_dict()
            retriever_components.append(retriever_components_item)

        retriever_components_schema = self.retriever_components_schema

        retriever_id = self.retriever_id

        updated_at = self.updated_at.isoformat()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "name": name,
                "organization_id": organization_id,
                "retriever_components": retriever_components,
                "retriever_components_schema": retriever_components_schema,
                "retriever_id": retriever_id,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retriever_component_detail import RetrieverComponentDetail

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        retriever_components = []
        _retriever_components = d.pop("retriever_components")
        for retriever_components_item_data in _retriever_components:
            retriever_components_item = RetrieverComponentDetail.from_dict(retriever_components_item_data)

            retriever_components.append(retriever_components_item)

        retriever_components_schema = d.pop("retriever_components_schema")

        retriever_id = d.pop("retriever_id")

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        get_retriever_response_content = cls(
            created_at=created_at,
            created_by=created_by,
            name=name,
            organization_id=organization_id,
            retriever_components=retriever_components,
            retriever_components_schema=retriever_components_schema,
            retriever_id=retriever_id,
            updated_at=updated_at,
            description=description,
        )

        get_retriever_response_content.additional_properties = d
        return get_retriever_response_content

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
