from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatMessageDriverConfiguration")


@_attrs_define
class ChatMessageDriverConfiguration:
    """
    Attributes:
        extra_params (Union[Unset, Any]):
        max_tokens (Union[Unset, float]):
        model (Union[Unset, str]):
        structured_output_strategy (Union[Unset, str]):
        temperature (Union[Unset, float]):
        use_native_tools (Union[Unset, bool]):
    """

    extra_params: Union[Unset, Any] = UNSET
    max_tokens: Union[Unset, float] = UNSET
    model: Union[Unset, str] = UNSET
    structured_output_strategy: Union[Unset, str] = UNSET
    temperature: Union[Unset, float] = UNSET
    use_native_tools: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extra_params = self.extra_params

        max_tokens = self.max_tokens

        model = self.model

        structured_output_strategy = self.structured_output_strategy

        temperature = self.temperature

        use_native_tools = self.use_native_tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extra_params is not UNSET:
            field_dict["extra_params"] = extra_params
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if model is not UNSET:
            field_dict["model"] = model
        if structured_output_strategy is not UNSET:
            field_dict["structured_output_strategy"] = structured_output_strategy
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if use_native_tools is not UNSET:
            field_dict["use_native_tools"] = use_native_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extra_params = d.pop("extra_params", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        model = d.pop("model", UNSET)

        structured_output_strategy = d.pop("structured_output_strategy", UNSET)

        temperature = d.pop("temperature", UNSET)

        use_native_tools = d.pop("use_native_tools", UNSET)

        chat_message_driver_configuration = cls(
            extra_params=extra_params,
            max_tokens=max_tokens,
            model=model,
            structured_output_strategy=structured_output_strategy,
            temperature=temperature,
            use_native_tools=use_native_tools,
        )

        chat_message_driver_configuration.additional_properties = d
        return chat_message_driver_configuration

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
