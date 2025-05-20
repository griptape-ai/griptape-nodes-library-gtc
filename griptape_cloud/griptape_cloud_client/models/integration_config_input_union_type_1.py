from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.git_hub_app_input import GitHubAppInput


T = TypeVar("T", bound="IntegrationConfigInputUnionType1")


@_attrs_define
class IntegrationConfigInputUnionType1:
    """
    Attributes:
        github_app (GitHubAppInput):
    """

    github_app: "GitHubAppInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        github_app = self.github_app.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "github_app": github_app,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_hub_app_input import GitHubAppInput

        d = dict(src_dict)
        github_app = GitHubAppInput.from_dict(d.pop("github_app"))

        integration_config_input_union_type_1 = cls(
            github_app=github_app,
        )

        integration_config_input_union_type_1.additional_properties = d
        return integration_config_input_union_type_1

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
