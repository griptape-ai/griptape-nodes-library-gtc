from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryRetrieverRequestContent")


@_attrs_define
class QueryRetrieverRequestContent:
    """
    Attributes:
        query (str):
        retriever_components_query_args (Union[Unset, Any]):
    """

    query: str
    retriever_components_query_args: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        retriever_components_query_args = self.retriever_components_query_args

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if retriever_components_query_args is not UNSET:
            field_dict["retriever_components_query_args"] = retriever_components_query_args

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        retriever_components_query_args = d.pop("retriever_components_query_args", UNSET)

        query_retriever_request_content = cls(
            query=query,
            retriever_components_query_args=retriever_components_query_args,
        )

        query_retriever_request_content.additional_properties = d
        return query_retriever_request_content

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
