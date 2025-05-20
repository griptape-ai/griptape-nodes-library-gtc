from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.tool_detail import ToolDetail


T = TypeVar("T", bound="ListToolsResponseContent")


@_attrs_define
class ListToolsResponseContent:
    """
    Attributes:
        pagination (Pagination):
        tools (list['ToolDetail']):
    """

    pagination: "Pagination"
    tools: list["ToolDetail"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "tools": tools,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.tool_detail import ToolDetail

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = ToolDetail.from_dict(tools_item_data)

            tools.append(tools_item)

        list_tools_response_content = cls(
            pagination=pagination,
            tools=tools,
        )

        list_tools_response_content.additional_properties = d
        return list_tools_response_content

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
