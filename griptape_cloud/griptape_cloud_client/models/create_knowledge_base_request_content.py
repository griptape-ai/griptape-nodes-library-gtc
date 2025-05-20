from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.embedding_model import EmbeddingModel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_base_config_input_union_type_0 import KnowledgeBaseConfigInputUnionType0
    from ..models.knowledge_base_config_input_union_type_1 import KnowledgeBaseConfigInputUnionType1
    from ..models.knowledge_base_config_input_union_type_2 import KnowledgeBaseConfigInputUnionType2
    from ..models.knowledge_base_config_input_union_type_3 import KnowledgeBaseConfigInputUnionType3
    from ..models.transform_detail import TransformDetail


T = TypeVar("T", bound="CreateKnowledgeBaseRequestContent")


@_attrs_define
class CreateKnowledgeBaseRequestContent:
    """
    Attributes:
        config (Union['KnowledgeBaseConfigInputUnionType0', 'KnowledgeBaseConfigInputUnionType1',
            'KnowledgeBaseConfigInputUnionType2', 'KnowledgeBaseConfigInputUnionType3']):
        name (str):
        type_ (str):
        asset_paths (Union[Unset, list[str]]):
        description (Union[Unset, str]):
        embedding_model (Union[Unset, EmbeddingModel]):
        transforms (Union[Unset, list['TransformDetail']]):
        use_default_embedding_model (Union[Unset, bool]):
    """

    config: Union[
        "KnowledgeBaseConfigInputUnionType0",
        "KnowledgeBaseConfigInputUnionType1",
        "KnowledgeBaseConfigInputUnionType2",
        "KnowledgeBaseConfigInputUnionType3",
    ]
    name: str
    type_: str
    asset_paths: Union[Unset, list[str]] = UNSET
    description: Union[Unset, str] = UNSET
    embedding_model: Union[Unset, EmbeddingModel] = UNSET
    transforms: Union[Unset, list["TransformDetail"]] = UNSET
    use_default_embedding_model: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.knowledge_base_config_input_union_type_0 import KnowledgeBaseConfigInputUnionType0
        from ..models.knowledge_base_config_input_union_type_1 import KnowledgeBaseConfigInputUnionType1
        from ..models.knowledge_base_config_input_union_type_2 import KnowledgeBaseConfigInputUnionType2

        config: dict[str, Any]
        if isinstance(self.config, KnowledgeBaseConfigInputUnionType0):
            config = self.config.to_dict()
        elif isinstance(self.config, KnowledgeBaseConfigInputUnionType1):
            config = self.config.to_dict()
        elif isinstance(self.config, KnowledgeBaseConfigInputUnionType2):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        name = self.name

        type_ = self.type_

        asset_paths: Union[Unset, list[str]] = UNSET
        if not isinstance(self.asset_paths, Unset):
            asset_paths = self.asset_paths

        description = self.description

        embedding_model: Union[Unset, str] = UNSET
        if not isinstance(self.embedding_model, Unset):
            embedding_model = self.embedding_model.value

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
                "config": config,
                "name": name,
                "type": type_,
            }
        )
        if asset_paths is not UNSET:
            field_dict["asset_paths"] = asset_paths
        if description is not UNSET:
            field_dict["description"] = description
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if transforms is not UNSET:
            field_dict["transforms"] = transforms
        if use_default_embedding_model is not UNSET:
            field_dict["use_default_embedding_model"] = use_default_embedding_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knowledge_base_config_input_union_type_0 import KnowledgeBaseConfigInputUnionType0
        from ..models.knowledge_base_config_input_union_type_1 import KnowledgeBaseConfigInputUnionType1
        from ..models.knowledge_base_config_input_union_type_2 import KnowledgeBaseConfigInputUnionType2
        from ..models.knowledge_base_config_input_union_type_3 import KnowledgeBaseConfigInputUnionType3
        from ..models.transform_detail import TransformDetail

        d = dict(src_dict)

        def _parse_config(
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
            componentsschemas_knowledge_base_config_input_union_type_3 = KnowledgeBaseConfigInputUnionType3.from_dict(
                data
            )

            return componentsschemas_knowledge_base_config_input_union_type_3

        config = _parse_config(d.pop("config"))

        name = d.pop("name")

        type_ = d.pop("type")

        asset_paths = cast(list[str], d.pop("asset_paths", UNSET))

        description = d.pop("description", UNSET)

        _embedding_model = d.pop("embedding_model", UNSET)
        embedding_model: Union[Unset, EmbeddingModel]
        if isinstance(_embedding_model, Unset):
            embedding_model = UNSET
        else:
            embedding_model = EmbeddingModel(_embedding_model)

        transforms = []
        _transforms = d.pop("transforms", UNSET)
        for transforms_item_data in _transforms or []:
            transforms_item = TransformDetail.from_dict(transforms_item_data)

            transforms.append(transforms_item)

        use_default_embedding_model = d.pop("use_default_embedding_model", UNSET)

        create_knowledge_base_request_content = cls(
            config=config,
            name=name,
            type_=type_,
            asset_paths=asset_paths,
            description=description,
            embedding_model=embedding_model,
            transforms=transforms,
            use_default_embedding_model=use_default_embedding_model,
        )

        create_knowledge_base_request_content.additional_properties = d
        return create_knowledge_base_request_content

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
