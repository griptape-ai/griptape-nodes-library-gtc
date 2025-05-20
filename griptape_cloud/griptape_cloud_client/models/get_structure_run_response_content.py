import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.structure_run_status import StructureRunStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env_var import EnvVar


T = TypeVar("T", bound="GetStructureRunResponseContent")


@_attrs_define
class GetStructureRunResponseContent:
    """
    Attributes:
        args (list[str]):
        completed_at (Union[None, datetime.datetime]):
        created_at (datetime.datetime):
        created_by (str):
        started_at (Union[None, datetime.datetime]):
        status (StructureRunStatus):
        structure_id (str):
        structure_run_id (str):
        updated_at (datetime.datetime):
        deployment_id (Union[Unset, str]):
        env_vars (Union[Unset, list['EnvVar']]):
        output (Union[Unset, Any]):
        output_timestamp (Union[Unset, float]):
        status_detail (Union[Unset, Any]):
    """

    args: list[str]
    completed_at: Union[None, datetime.datetime]
    created_at: datetime.datetime
    created_by: str
    started_at: Union[None, datetime.datetime]
    status: StructureRunStatus
    structure_id: str
    structure_run_id: str
    updated_at: datetime.datetime
    deployment_id: Union[Unset, str] = UNSET
    env_vars: Union[Unset, list["EnvVar"]] = UNSET
    output: Union[Unset, Any] = UNSET
    output_timestamp: Union[Unset, float] = UNSET
    status_detail: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args = self.args

        completed_at: Union[None, str]
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        started_at: Union[None, str]
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        status = self.status.value

        structure_id = self.structure_id

        structure_run_id = self.structure_run_id

        updated_at = self.updated_at.isoformat()

        deployment_id = self.deployment_id

        env_vars: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = []
            for env_vars_item_data in self.env_vars:
                env_vars_item = env_vars_item_data.to_dict()
                env_vars.append(env_vars_item)

        output = self.output

        output_timestamp = self.output_timestamp

        status_detail = self.status_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "args": args,
                "completed_at": completed_at,
                "created_at": created_at,
                "created_by": created_by,
                "started_at": started_at,
                "status": status,
                "structure_id": structure_id,
                "structure_run_id": structure_run_id,
                "updated_at": updated_at,
            }
        )
        if deployment_id is not UNSET:
            field_dict["deployment_id"] = deployment_id
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if output is not UNSET:
            field_dict["output"] = output
        if output_timestamp is not UNSET:
            field_dict["output_timestamp"] = output_timestamp
        if status_detail is not UNSET:
            field_dict["status_detail"] = status_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.env_var import EnvVar

        d = dict(src_dict)
        args = cast(list[str], d.pop("args"))

        def _parse_completed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        def _parse_started_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = StructureRunStatus(d.pop("status"))

        structure_id = d.pop("structure_id")

        structure_run_id = d.pop("structure_run_id")

        updated_at = isoparse(d.pop("updated_at"))

        deployment_id = d.pop("deployment_id", UNSET)

        env_vars = []
        _env_vars = d.pop("env_vars", UNSET)
        for env_vars_item_data in _env_vars or []:
            env_vars_item = EnvVar.from_dict(env_vars_item_data)

            env_vars.append(env_vars_item)

        output = d.pop("output", UNSET)

        output_timestamp = d.pop("output_timestamp", UNSET)

        status_detail = d.pop("status_detail", UNSET)

        get_structure_run_response_content = cls(
            args=args,
            completed_at=completed_at,
            created_at=created_at,
            created_by=created_by,
            started_at=started_at,
            status=status,
            structure_id=structure_id,
            structure_run_id=structure_run_id,
            updated_at=updated_at,
            deployment_id=deployment_id,
            env_vars=env_vars,
            output=output,
            output_timestamp=output_timestamp,
            status_detail=status_detail,
        )

        get_structure_run_response_content.additional_properties = d
        return get_structure_run_response_content

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
