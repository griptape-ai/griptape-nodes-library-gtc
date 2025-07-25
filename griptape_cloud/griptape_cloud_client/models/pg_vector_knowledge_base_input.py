from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PGVectorKnowledgeBaseInput")


@_attrs_define
class PGVectorKnowledgeBaseInput:
    """
    Attributes:
        connection_string (str):
        password (str):
        embedding_model (Union[Unset, str]):
        use_default_embedding_model (Union[Unset, bool]):
    """

    connection_string: str
    password: str
    embedding_model: Union[Unset, str] = UNSET
    use_default_embedding_model: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_string = self.connection_string

        password = self.password

        embedding_model = self.embedding_model

        use_default_embedding_model = self.use_default_embedding_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_string": connection_string,
                "password": password,
            }
        )
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if use_default_embedding_model is not UNSET:
            field_dict["use_default_embedding_model"] = use_default_embedding_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_string = d.pop("connection_string")

        password = d.pop("password")

        embedding_model = d.pop("embedding_model", UNSET)

        use_default_embedding_model = d.pop("use_default_embedding_model", UNSET)

        pg_vector_knowledge_base_input = cls(
            connection_string=connection_string,
            password=password,
            embedding_model=embedding_model,
            use_default_embedding_model=use_default_embedding_model,
        )

        pg_vector_knowledge_base_input.additional_properties = d
        return pg_vector_knowledge_base_input

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
