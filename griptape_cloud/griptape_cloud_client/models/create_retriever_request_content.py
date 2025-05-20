from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retriever_component_input import RetrieverComponentInput


T = TypeVar("T", bound="CreateRetrieverRequestContent")


@_attrs_define
class CreateRetrieverRequestContent:
    """
    Attributes:
        name (str):
        description (Union[Unset, str]):
        retriever_component_ids (Union[Unset, list[str]]):
        retriever_components (Union[Unset, list['RetrieverComponentInput']]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    retriever_component_ids: Union[Unset, list[str]] = UNSET
    retriever_components: Union[Unset, list["RetrieverComponentInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        retriever_component_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.retriever_component_ids, Unset):
            retriever_component_ids = self.retriever_component_ids

        retriever_components: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.retriever_components, Unset):
            retriever_components = []
            for retriever_components_item_data in self.retriever_components:
                retriever_components_item = retriever_components_item_data.to_dict()
                retriever_components.append(retriever_components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if retriever_component_ids is not UNSET:
            field_dict["retriever_component_ids"] = retriever_component_ids
        if retriever_components is not UNSET:
            field_dict["retriever_components"] = retriever_components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retriever_component_input import RetrieverComponentInput

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        retriever_component_ids = cast(list[str], d.pop("retriever_component_ids", UNSET))

        retriever_components = []
        _retriever_components = d.pop("retriever_components", UNSET)
        for retriever_components_item_data in _retriever_components or []:
            retriever_components_item = RetrieverComponentInput.from_dict(retriever_components_item_data)

            retriever_components.append(retriever_components_item)

        create_retriever_request_content = cls(
            name=name,
            description=description,
            retriever_component_ids=retriever_component_ids,
            retriever_components=retriever_components,
        )

        create_retriever_request_content.additional_properties = d
        return create_retriever_request_content

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
