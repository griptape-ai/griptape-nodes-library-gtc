from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.github_code_source import GithubCodeSource


T = TypeVar("T", bound="CodeSourceType0")


@_attrs_define
class CodeSourceType0:
    """
    Attributes:
        github (GithubCodeSource):
    """

    github: "GithubCodeSource"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        github = self.github.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "github": github,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_code_source import GithubCodeSource

        d = dict(src_dict)
        github = GithubCodeSource.from_dict(d.pop("github"))

        code_source_type_0 = cls(
            github=github,
        )

        code_source_type_0.additional_properties = d
        return code_source_type_0

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
