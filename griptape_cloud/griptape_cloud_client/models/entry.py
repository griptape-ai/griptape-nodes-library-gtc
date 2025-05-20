from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta import Meta


T = TypeVar("T", bound="Entry")


@_attrs_define
class Entry:
    """
    Attributes:
        id (str):
        score (float):
        meta (Union[Unset, Meta]):
        namespace (Union[Unset, str]):
        vector (Union[Unset, list[float]]):
    """

    id: str
    score: float
    meta: Union[Unset, "Meta"] = UNSET
    namespace: Union[Unset, str] = UNSET
    vector: Union[Unset, list[float]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        score = self.score

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        namespace = self.namespace

        vector: Union[Unset, list[float]] = UNSET
        if not isinstance(self.vector, Unset):
            vector = self.vector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "score": score,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta import Meta

        d = dict(src_dict)
        id = d.pop("id")

        score = d.pop("score")

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, Meta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = Meta.from_dict(_meta)

        namespace = d.pop("namespace", UNSET)

        vector = cast(list[float], d.pop("vector", UNSET))

        entry = cls(
            id=id,
            score=score,
            meta=meta,
            namespace=namespace,
            vector=vector,
        )

        entry.additional_properties = d
        return entry

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
