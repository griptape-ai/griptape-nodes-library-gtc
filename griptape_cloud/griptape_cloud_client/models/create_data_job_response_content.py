import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_job_status import DataJobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error


T = TypeVar("T", bound="CreateDataJobResponseContent")


@_attrs_define
class CreateDataJobResponseContent:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        data_connector_id (str):
        data_job_id (str):
        status (DataJobStatus):
        bytes_ingested (Union[Unset, float]):
        completed_at (Union[None, Unset, datetime.datetime]):
        errors (Union[Unset, list['Error']]):
        status_detail (Union[Unset, Any]):
    """

    created_at: datetime.datetime
    created_by: str
    data_connector_id: str
    data_job_id: str
    status: DataJobStatus
    bytes_ingested: Union[Unset, float] = UNSET
    completed_at: Union[None, Unset, datetime.datetime] = UNSET
    errors: Union[Unset, list["Error"]] = UNSET
    status_detail: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        data_connector_id = self.data_connector_id

        data_job_id = self.data_job_id

        status = self.status.value

        bytes_ingested = self.bytes_ingested

        completed_at: Union[None, Unset, str]
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        status_detail = self.status_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "data_connector_id": data_connector_id,
                "data_job_id": data_job_id,
                "status": status,
            }
        )
        if bytes_ingested is not UNSET:
            field_dict["bytes_ingested"] = bytes_ingested
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if errors is not UNSET:
            field_dict["errors"] = errors
        if status_detail is not UNSET:
            field_dict["status_detail"] = status_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error import Error

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        data_connector_id = d.pop("data_connector_id")

        data_job_id = d.pop("data_job_id")

        status = DataJobStatus(d.pop("status"))

        bytes_ingested = d.pop("bytes_ingested", UNSET)

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

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = Error.from_dict(errors_item_data)

            errors.append(errors_item)

        status_detail = d.pop("status_detail", UNSET)

        create_data_job_response_content = cls(
            created_at=created_at,
            created_by=created_by,
            data_connector_id=data_connector_id,
            data_job_id=data_job_id,
            status=status,
            bytes_ingested=bytes_ingested,
            completed_at=completed_at,
            errors=errors,
            status_detail=status_detail,
        )

        create_data_job_response_content.additional_properties = d
        return create_data_job_response_content

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
