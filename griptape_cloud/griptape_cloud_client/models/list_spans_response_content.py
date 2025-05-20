from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_detail import SpanDetail


T = TypeVar("T", bound="ListSpansResponseContent")


@_attrs_define
class ListSpansResponseContent:
    """
    Attributes:
        spans (list['SpanDetail']):
        page (Union[Unset, float]):
    """

    spans: list["SpanDetail"]
    page: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spans = []
        for spans_item_data in self.spans:
            spans_item = spans_item_data.to_dict()
            spans.append(spans_item)

        page = self.page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spans": spans,
            }
        )
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_detail import SpanDetail

        d = dict(src_dict)
        spans = []
        _spans = d.pop("spans")
        for spans_item_data in _spans:
            spans_item = SpanDetail.from_dict(spans_item_data)

            spans.append(spans_item)

        page = d.pop("page", UNSET)

        list_spans_response_content = cls(
            spans=spans,
            page=page,
        )

        list_spans_response_content.additional_properties = d
        return list_spans_response_content

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
