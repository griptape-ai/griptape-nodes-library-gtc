import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.embedding_model import EmbeddingModel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_base_config_union_type_0 import KnowledgeBaseConfigUnionType0
    from ..models.knowledge_base_config_union_type_1 import KnowledgeBaseConfigUnionType1
    from ..models.knowledge_base_config_union_type_2 import KnowledgeBaseConfigUnionType2
    from ..models.knowledge_base_config_union_type_3 import KnowledgeBaseConfigUnionType3
    from ..models.transform_detail import TransformDetail


T = TypeVar("T", bound="KnowledgeBaseDetail")


@_attrs_define
class KnowledgeBaseDetail:
    """
    Attributes:
        asset_paths (list[str]):
        config (Union['KnowledgeBaseConfigUnionType0', 'KnowledgeBaseConfigUnionType1', 'KnowledgeBaseConfigUnionType2',
            'KnowledgeBaseConfigUnionType3']):
        created_at (datetime.datetime):
        created_by (str):
        knowledge_base_id (str):
        name (str):
        organization_id (str):
        type_ (str):
        updated_at (datetime.datetime):
        description (Union[Unset, str]):
        embedding_model (Union[Unset, EmbeddingModel]):
        schedule_expression (Union[Unset, str]):
        transforms (Union[Unset, list['TransformDetail']]):
        use_default_embedding_model (Union[Unset, bool]):
    """

    asset_paths: list[str]
    config: Union[
        "KnowledgeBaseConfigUnionType0",
        "KnowledgeBaseConfigUnionType1",
        "KnowledgeBaseConfigUnionType2",
        "KnowledgeBaseConfigUnionType3",
    ]
    created_at: datetime.datetime
    created_by: str
    knowledge_base_id: str
    name: str
    organization_id: str
    type_: str
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    embedding_model: Union[Unset, EmbeddingModel] = UNSET
    schedule_expression: Union[Unset, str] = UNSET
    transforms: Union[Unset, list["TransformDetail"]] = UNSET
    use_default_embedding_model: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.knowledge_base_config_union_type_0 import KnowledgeBaseConfigUnionType0
        from ..models.knowledge_base_config_union_type_1 import KnowledgeBaseConfigUnionType1
        from ..models.knowledge_base_config_union_type_2 import KnowledgeBaseConfigUnionType2

        asset_paths = self.asset_paths

        config: dict[str, Any]
        if isinstance(self.config, KnowledgeBaseConfigUnionType0):
            config = self.config.to_dict()
        elif isinstance(self.config, KnowledgeBaseConfigUnionType1):
            config = self.config.to_dict()
        elif isinstance(self.config, KnowledgeBaseConfigUnionType2):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        knowledge_base_id = self.knowledge_base_id

        name = self.name

        organization_id = self.organization_id

        type_ = self.type_

        updated_at = self.updated_at.isoformat()

        description = self.description

        embedding_model: Union[Unset, str] = UNSET
        if not isinstance(self.embedding_model, Unset):
            embedding_model = self.embedding_model.value

        schedule_expression = self.schedule_expression

        transforms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transforms, Unset):
            transforms = []
            for transforms_item_data in self.transforms:
                transforms_item = transforms_item_data.to_dict()
                transforms.append(transforms_item)

        use_default_embedding_model = self.use_default_embedding_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_paths": asset_paths,
                "config": config,
                "created_at": created_at,
                "created_by": created_by,
                "knowledge_base_id": knowledge_base_id,
                "name": name,
                "organization_id": organization_id,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if schedule_expression is not UNSET:
            field_dict["schedule_expression"] = schedule_expression
        if transforms is not UNSET:
            field_dict["transforms"] = transforms
        if use_default_embedding_model is not UNSET:
            field_dict["use_default_embedding_model"] = use_default_embedding_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knowledge_base_config_union_type_0 import KnowledgeBaseConfigUnionType0
        from ..models.knowledge_base_config_union_type_1 import KnowledgeBaseConfigUnionType1
        from ..models.knowledge_base_config_union_type_2 import KnowledgeBaseConfigUnionType2
        from ..models.knowledge_base_config_union_type_3 import KnowledgeBaseConfigUnionType3
        from ..models.transform_detail import TransformDetail

        d = dict(src_dict)
        asset_paths = cast(list[str], d.pop("asset_paths"))

        def _parse_config(
            data: object,
        ) -> Union[
            "KnowledgeBaseConfigUnionType0",
            "KnowledgeBaseConfigUnionType1",
            "KnowledgeBaseConfigUnionType2",
            "KnowledgeBaseConfigUnionType3",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_knowledge_base_config_union_type_0 = KnowledgeBaseConfigUnionType0.from_dict(data)

                return componentsschemas_knowledge_base_config_union_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_knowledge_base_config_union_type_1 = KnowledgeBaseConfigUnionType1.from_dict(data)

                return componentsschemas_knowledge_base_config_union_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_knowledge_base_config_union_type_2 = KnowledgeBaseConfigUnionType2.from_dict(data)

                return componentsschemas_knowledge_base_config_union_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_knowledge_base_config_union_type_3 = KnowledgeBaseConfigUnionType3.from_dict(data)

            return componentsschemas_knowledge_base_config_union_type_3

        config = _parse_config(d.pop("config"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        knowledge_base_id = d.pop("knowledge_base_id")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        type_ = d.pop("type")

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        _embedding_model = d.pop("embedding_model", UNSET)
        embedding_model: Union[Unset, EmbeddingModel]
        if isinstance(_embedding_model, Unset):
            embedding_model = UNSET
        else:
            embedding_model = EmbeddingModel(_embedding_model)

        schedule_expression = d.pop("schedule_expression", UNSET)

        transforms = []
        _transforms = d.pop("transforms", UNSET)
        for transforms_item_data in _transforms or []:
            transforms_item = TransformDetail.from_dict(transforms_item_data)

            transforms.append(transforms_item)

        use_default_embedding_model = d.pop("use_default_embedding_model", UNSET)

        knowledge_base_detail = cls(
            asset_paths=asset_paths,
            config=config,
            created_at=created_at,
            created_by=created_by,
            knowledge_base_id=knowledge_base_id,
            name=name,
            organization_id=organization_id,
            type_=type_,
            updated_at=updated_at,
            description=description,
            embedding_model=embedding_model,
            schedule_expression=schedule_expression,
            transforms=transforms,
            use_default_embedding_model=use_default_embedding_model,
        )

        knowledge_base_detail.additional_properties = d
        return knowledge_base_detail

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
