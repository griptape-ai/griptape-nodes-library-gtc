from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.github_structure_code_push_config import GithubStructureCodePushConfig


T = TypeVar("T", bound="GithubStructureCode")


@_attrs_define
class GithubStructureCode:
    """
    Attributes:
        name (str):
        owner (str):
        push (GithubStructureCodePushConfig):
    """

    name: str
    owner: str
    push: "GithubStructureCodePushConfig"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner = self.owner

        push = self.push.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "owner": owner,
                "push": push,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_structure_code_push_config import GithubStructureCodePushConfig

        d = dict(src_dict)
        name = d.pop("name")

        owner = d.pop("owner")

        push = GithubStructureCodePushConfig.from_dict(d.pop("push"))

        github_structure_code = cls(
            name=name,
            owner=owner,
            push=push,
        )

        github_structure_code.additional_properties = d
        return github_structure_code

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
