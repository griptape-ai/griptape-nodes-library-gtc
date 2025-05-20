from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.tool_deployment_detail import ToolDeploymentDetail


T = TypeVar("T", bound="ListToolDeploymentsResponseContent")


@_attrs_define
class ListToolDeploymentsResponseContent:
    """
    Attributes:
        deployments (list['ToolDeploymentDetail']):
        pagination (Pagination):
    """

    deployments: list["ToolDeploymentDetail"]
    pagination: "Pagination"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployments = []
        for deployments_item_data in self.deployments:
            deployments_item = deployments_item_data.to_dict()
            deployments.append(deployments_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deployments": deployments,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.tool_deployment_detail import ToolDeploymentDetail

        d = dict(src_dict)
        deployments = []
        _deployments = d.pop("deployments")
        for deployments_item_data in _deployments:
            deployments_item = ToolDeploymentDetail.from_dict(deployments_item_data)

            deployments.append(deployments_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        list_tool_deployments_response_content = cls(
            deployments=deployments,
            pagination=pagination,
        )

        list_tool_deployments_response_content.additional_properties = d
        return list_tool_deployments_response_content

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
