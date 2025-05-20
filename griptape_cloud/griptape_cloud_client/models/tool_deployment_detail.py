import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.deployment_status import DeploymentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_source_type_0 import CodeSourceType0
    from ..models.code_source_type_1 import CodeSourceType1


T = TypeVar("T", bound="ToolDeploymentDetail")


@_attrs_define
class ToolDeploymentDetail:
    """
    Attributes:
        code_source (Union['CodeSourceType0', 'CodeSourceType1']):
        created_at (datetime.datetime):
        created_by (str):
        deployment_id (str):
        status (DeploymentStatus):
        tool_id (str):
        completed_at (Union[None, Unset, datetime.datetime]):
        status_detail (Union[Unset, Any]):
    """

    code_source: Union["CodeSourceType0", "CodeSourceType1"]
    created_at: datetime.datetime
    created_by: str
    deployment_id: str
    status: DeploymentStatus
    tool_id: str
    completed_at: Union[None, Unset, datetime.datetime] = UNSET
    status_detail: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.code_source_type_0 import CodeSourceType0

        code_source: dict[str, Any]
        if isinstance(self.code_source, CodeSourceType0):
            code_source = self.code_source.to_dict()
        else:
            code_source = self.code_source.to_dict()

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        deployment_id = self.deployment_id

        status = self.status.value

        tool_id = self.tool_id

        completed_at: Union[None, Unset, str]
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        status_detail = self.status_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code_source": code_source,
                "created_at": created_at,
                "created_by": created_by,
                "deployment_id": deployment_id,
                "status": status,
                "tool_id": tool_id,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if status_detail is not UNSET:
            field_dict["status_detail"] = status_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_source_type_0 import CodeSourceType0
        from ..models.code_source_type_1 import CodeSourceType1

        d = dict(src_dict)

        def _parse_code_source(data: object) -> Union["CodeSourceType0", "CodeSourceType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_code_source_type_0 = CodeSourceType0.from_dict(data)

                return componentsschemas_code_source_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_code_source_type_1 = CodeSourceType1.from_dict(data)

            return componentsschemas_code_source_type_1

        code_source = _parse_code_source(d.pop("code_source"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        deployment_id = d.pop("deployment_id")

        status = DeploymentStatus(d.pop("status"))

        tool_id = d.pop("tool_id")

        def _parse_completed_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        status_detail = d.pop("status_detail", UNSET)

        tool_deployment_detail = cls(
            code_source=code_source,
            created_at=created_at,
            created_by=created_by,
            deployment_id=deployment_id,
            status=status,
            tool_id=tool_id,
            completed_at=completed_at,
            status_detail=status_detail,
        )

        tool_deployment_detail.additional_properties = d
        return tool_deployment_detail

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
