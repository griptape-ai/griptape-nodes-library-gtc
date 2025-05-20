import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_connector_config_union_type_0 import DataConnectorConfigUnionType0
    from ..models.data_connector_config_union_type_1 import DataConnectorConfigUnionType1
    from ..models.data_connector_config_union_type_2 import DataConnectorConfigUnionType2
    from ..models.data_connector_config_union_type_3 import DataConnectorConfigUnionType3
    from ..models.data_connector_config_union_type_4 import DataConnectorConfigUnionType4
    from ..models.data_connector_config_union_type_5 import DataConnectorConfigUnionType5


T = TypeVar("T", bound="CreateDataConnectorResponseContent")


@_attrs_define
class CreateDataConnectorResponseContent:
    """
    Attributes:
        config (Union['DataConnectorConfigUnionType0', 'DataConnectorConfigUnionType1', 'DataConnectorConfigUnionType2',
            'DataConnectorConfigUnionType3', 'DataConnectorConfigUnionType4', 'DataConnectorConfigUnionType5']):
        created_at (datetime.datetime):
        created_by (str):
        data_connector_id (str):
        name (str):
        type_ (str):
        updated_at (datetime.datetime):
        data_job_id (Union[Unset, str]):
        description (Union[Unset, str]):
        schedule_expression (Union[Unset, str]):
    """

    config: Union[
        "DataConnectorConfigUnionType0",
        "DataConnectorConfigUnionType1",
        "DataConnectorConfigUnionType2",
        "DataConnectorConfigUnionType3",
        "DataConnectorConfigUnionType4",
        "DataConnectorConfigUnionType5",
    ]
    created_at: datetime.datetime
    created_by: str
    data_connector_id: str
    name: str
    type_: str
    updated_at: datetime.datetime
    data_job_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    schedule_expression: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.data_connector_config_union_type_0 import DataConnectorConfigUnionType0
        from ..models.data_connector_config_union_type_1 import DataConnectorConfigUnionType1
        from ..models.data_connector_config_union_type_2 import DataConnectorConfigUnionType2
        from ..models.data_connector_config_union_type_3 import DataConnectorConfigUnionType3
        from ..models.data_connector_config_union_type_4 import DataConnectorConfigUnionType4

        config: dict[str, Any]
        if isinstance(self.config, DataConnectorConfigUnionType0):
            config = self.config.to_dict()
        elif isinstance(self.config, DataConnectorConfigUnionType1):
            config = self.config.to_dict()
        elif isinstance(self.config, DataConnectorConfigUnionType2):
            config = self.config.to_dict()
        elif isinstance(self.config, DataConnectorConfigUnionType3):
            config = self.config.to_dict()
        elif isinstance(self.config, DataConnectorConfigUnionType4):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        data_connector_id = self.data_connector_id

        name = self.name

        type_ = self.type_

        updated_at = self.updated_at.isoformat()

        data_job_id = self.data_job_id

        description = self.description

        schedule_expression = self.schedule_expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "created_at": created_at,
                "created_by": created_by,
                "data_connector_id": data_connector_id,
                "name": name,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if data_job_id is not UNSET:
            field_dict["data_job_id"] = data_job_id
        if description is not UNSET:
            field_dict["description"] = description
        if schedule_expression is not UNSET:
            field_dict["schedule_expression"] = schedule_expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_connector_config_union_type_0 import DataConnectorConfigUnionType0
        from ..models.data_connector_config_union_type_1 import DataConnectorConfigUnionType1
        from ..models.data_connector_config_union_type_2 import DataConnectorConfigUnionType2
        from ..models.data_connector_config_union_type_3 import DataConnectorConfigUnionType3
        from ..models.data_connector_config_union_type_4 import DataConnectorConfigUnionType4
        from ..models.data_connector_config_union_type_5 import DataConnectorConfigUnionType5

        d = dict(src_dict)

        def _parse_config(
            data: object,
        ) -> Union[
            "DataConnectorConfigUnionType0",
            "DataConnectorConfigUnionType1",
            "DataConnectorConfigUnionType2",
            "DataConnectorConfigUnionType3",
            "DataConnectorConfigUnionType4",
            "DataConnectorConfigUnionType5",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_union_type_0 = DataConnectorConfigUnionType0.from_dict(data)

                return componentsschemas_data_connector_config_union_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_union_type_1 = DataConnectorConfigUnionType1.from_dict(data)

                return componentsschemas_data_connector_config_union_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_union_type_2 = DataConnectorConfigUnionType2.from_dict(data)

                return componentsschemas_data_connector_config_union_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_union_type_3 = DataConnectorConfigUnionType3.from_dict(data)

                return componentsschemas_data_connector_config_union_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_data_connector_config_union_type_4 = DataConnectorConfigUnionType4.from_dict(data)

                return componentsschemas_data_connector_config_union_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_data_connector_config_union_type_5 = DataConnectorConfigUnionType5.from_dict(data)

            return componentsschemas_data_connector_config_union_type_5

        config = _parse_config(d.pop("config"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        data_connector_id = d.pop("data_connector_id")

        name = d.pop("name")

        type_ = d.pop("type")

        updated_at = isoparse(d.pop("updated_at"))

        data_job_id = d.pop("data_job_id", UNSET)

        description = d.pop("description", UNSET)

        schedule_expression = d.pop("schedule_expression", UNSET)

        create_data_connector_response_content = cls(
            config=config,
            created_at=created_at,
            created_by=created_by,
            data_connector_id=data_connector_id,
            name=name,
            type_=type_,
            updated_at=updated_at,
            data_job_id=data_job_id,
            description=description,
            schedule_expression=schedule_expression,
        )

        create_data_connector_response_content.additional_properties = d
        return create_data_connector_response_content

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
