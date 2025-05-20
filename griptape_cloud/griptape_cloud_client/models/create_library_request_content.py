from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_base_config_input_union_type_0 import KnowledgeBaseConfigInputUnionType0
    from ..models.knowledge_base_config_input_union_type_1 import KnowledgeBaseConfigInputUnionType1
    from ..models.knowledge_base_config_input_union_type_2 import KnowledgeBaseConfigInputUnionType2
    from ..models.knowledge_base_config_input_union_type_3 import KnowledgeBaseConfigInputUnionType3


T = TypeVar("T", bound="CreateLibraryRequestContent")


@_attrs_define
class CreateLibraryRequestContent:
    """
    Attributes:
        data_connector_ids (list[str]):
        knowledge_base_configs (list[Union['KnowledgeBaseConfigInputUnionType0', 'KnowledgeBaseConfigInputUnionType1',
            'KnowledgeBaseConfigInputUnionType2', 'KnowledgeBaseConfigInputUnionType3']]):
        name (str):
        description (Union[Unset, str]):
    """

    data_connector_ids: list[str]
    knowledge_base_configs: list[
        Union[
            "KnowledgeBaseConfigInputUnionType0",
            "KnowledgeBaseConfigInputUnionType1",
            "KnowledgeBaseConfigInputUnionType2",
            "KnowledgeBaseConfigInputUnionType3",
        ]
    ]
    name: str
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.knowledge_base_config_input_union_type_0 import KnowledgeBaseConfigInputUnionType0
        from ..models.knowledge_base_config_input_union_type_1 import KnowledgeBaseConfigInputUnionType1
        from ..models.knowledge_base_config_input_union_type_2 import KnowledgeBaseConfigInputUnionType2

        data_connector_ids = self.data_connector_ids

        knowledge_base_configs = []
        for knowledge_base_configs_item_data in self.knowledge_base_configs:
            knowledge_base_configs_item: dict[str, Any]
            if isinstance(knowledge_base_configs_item_data, KnowledgeBaseConfigInputUnionType0):
                knowledge_base_configs_item = knowledge_base_configs_item_data.to_dict()
            elif isinstance(knowledge_base_configs_item_data, KnowledgeBaseConfigInputUnionType1):
                knowledge_base_configs_item = knowledge_base_configs_item_data.to_dict()
            elif isinstance(knowledge_base_configs_item_data, KnowledgeBaseConfigInputUnionType2):
                knowledge_base_configs_item = knowledge_base_configs_item_data.to_dict()
            else:
                knowledge_base_configs_item = knowledge_base_configs_item_data.to_dict()

            knowledge_base_configs.append(knowledge_base_configs_item)

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_connector_ids": data_connector_ids,
                "knowledge_base_configs": knowledge_base_configs,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knowledge_base_config_input_union_type_0 import KnowledgeBaseConfigInputUnionType0
        from ..models.knowledge_base_config_input_union_type_1 import KnowledgeBaseConfigInputUnionType1
        from ..models.knowledge_base_config_input_union_type_2 import KnowledgeBaseConfigInputUnionType2
        from ..models.knowledge_base_config_input_union_type_3 import KnowledgeBaseConfigInputUnionType3

        d = dict(src_dict)
        data_connector_ids = cast(list[str], d.pop("data_connector_ids"))

        knowledge_base_configs = []
        _knowledge_base_configs = d.pop("knowledge_base_configs")
        for knowledge_base_configs_item_data in _knowledge_base_configs:

            def _parse_knowledge_base_configs_item(
                data: object,
            ) -> Union[
                "KnowledgeBaseConfigInputUnionType0",
                "KnowledgeBaseConfigInputUnionType1",
                "KnowledgeBaseConfigInputUnionType2",
                "KnowledgeBaseConfigInputUnionType3",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_knowledge_base_config_input_union_type_0 = (
                        KnowledgeBaseConfigInputUnionType0.from_dict(data)
                    )

                    return componentsschemas_knowledge_base_config_input_union_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_knowledge_base_config_input_union_type_1 = (
                        KnowledgeBaseConfigInputUnionType1.from_dict(data)
                    )

                    return componentsschemas_knowledge_base_config_input_union_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_knowledge_base_config_input_union_type_2 = (
                        KnowledgeBaseConfigInputUnionType2.from_dict(data)
                    )

                    return componentsschemas_knowledge_base_config_input_union_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_knowledge_base_config_input_union_type_3 = (
                    KnowledgeBaseConfigInputUnionType3.from_dict(data)
                )

                return componentsschemas_knowledge_base_config_input_union_type_3

            knowledge_base_configs_item = _parse_knowledge_base_configs_item(knowledge_base_configs_item_data)

            knowledge_base_configs.append(knowledge_base_configs_item)

        name = d.pop("name")

        description = d.pop("description", UNSET)

        create_library_request_content = cls(
            data_connector_ids=data_connector_ids,
            knowledge_base_configs=knowledge_base_configs,
            name=name,
            description=description,
        )

        create_library_request_content.additional_properties = d
        return create_library_request_content

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
