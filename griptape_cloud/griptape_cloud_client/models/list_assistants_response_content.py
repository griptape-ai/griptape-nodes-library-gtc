from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.assistant_detail import AssistantDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListAssistantsResponseContent")


@_attrs_define
class ListAssistantsResponseContent:
    """
    Attributes:
        assistants (list['AssistantDetail']):
        pagination (Pagination):
    """

    assistants: list["AssistantDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistants = []
        for assistants_item_data in self.assistants:
            assistants_item = assistants_item_data.to_dict()
            assistants.append(assistants_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistants": assistants,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assistant_detail import AssistantDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        assistants = []
        _assistants = d.pop("assistants")
        for assistants_item_data in _assistants:
            assistants_item = AssistantDetail.from_dict(assistants_item_data)

            assistants.append(assistants_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_assistants_response_content = cls(
            assistants=assistants,
            pagination=pagination,
        )

        list_assistants_response_content.additional_properties = d
        return list_assistants_response_content

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
