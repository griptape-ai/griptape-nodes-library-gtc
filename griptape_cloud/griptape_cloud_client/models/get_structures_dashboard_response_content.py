from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_count_gauge import DeploymentCountGauge
    from ..models.deployment_duration_gauge import DeploymentDurationGauge
    from ..models.deployment_error_rate_gauge import DeploymentErrorRateGauge
    from ..models.duration_plot import DurationPlot
    from ..models.error_rate_gauge import ErrorRateGauge
    from ..models.run_count_gauge import RunCountGauge
    from ..models.run_duration_gauge import RunDurationGauge
    from ..models.token_count_gauge import TokenCountGauge


T = TypeVar("T", bound="GetStructuresDashboardResponseContent")


@_attrs_define
class GetStructuresDashboardResponseContent:
    """
    Attributes:
        deployment_count_gauge (Union[Unset, DeploymentCountGauge]):
        deployment_duration_gauge (Union[Unset, DeploymentDurationGauge]):
        deployment_error_rate_gauge (Union[Unset, DeploymentErrorRateGauge]):
        duration_plot (Union[Unset, DurationPlot]):
        error_rate_gauge (Union[Unset, ErrorRateGauge]):
        run_count_gauge (Union[Unset, RunCountGauge]):
        run_duration_gauge (Union[Unset, RunDurationGauge]):
        token_count_gauge (Union[Unset, TokenCountGauge]):
    """

    deployment_count_gauge: Union[Unset, "DeploymentCountGauge"] = UNSET
    deployment_duration_gauge: Union[Unset, "DeploymentDurationGauge"] = UNSET
    deployment_error_rate_gauge: Union[Unset, "DeploymentErrorRateGauge"] = UNSET
    duration_plot: Union[Unset, "DurationPlot"] = UNSET
    error_rate_gauge: Union[Unset, "ErrorRateGauge"] = UNSET
    run_count_gauge: Union[Unset, "RunCountGauge"] = UNSET
    run_duration_gauge: Union[Unset, "RunDurationGauge"] = UNSET
    token_count_gauge: Union[Unset, "TokenCountGauge"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployment_count_gauge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deployment_count_gauge, Unset):
            deployment_count_gauge = self.deployment_count_gauge.to_dict()

        deployment_duration_gauge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deployment_duration_gauge, Unset):
            deployment_duration_gauge = self.deployment_duration_gauge.to_dict()

        deployment_error_rate_gauge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deployment_error_rate_gauge, Unset):
            deployment_error_rate_gauge = self.deployment_error_rate_gauge.to_dict()

        duration_plot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.duration_plot, Unset):
            duration_plot = self.duration_plot.to_dict()

        error_rate_gauge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error_rate_gauge, Unset):
            error_rate_gauge = self.error_rate_gauge.to_dict()

        run_count_gauge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.run_count_gauge, Unset):
            run_count_gauge = self.run_count_gauge.to_dict()

        run_duration_gauge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.run_duration_gauge, Unset):
            run_duration_gauge = self.run_duration_gauge.to_dict()

        token_count_gauge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.token_count_gauge, Unset):
            token_count_gauge = self.token_count_gauge.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployment_count_gauge is not UNSET:
            field_dict["deployment_count_gauge"] = deployment_count_gauge
        if deployment_duration_gauge is not UNSET:
            field_dict["deployment_duration_gauge"] = deployment_duration_gauge
        if deployment_error_rate_gauge is not UNSET:
            field_dict["deployment_error_rate_gauge"] = deployment_error_rate_gauge
        if duration_plot is not UNSET:
            field_dict["duration_plot"] = duration_plot
        if error_rate_gauge is not UNSET:
            field_dict["error_rate_gauge"] = error_rate_gauge
        if run_count_gauge is not UNSET:
            field_dict["run_count_gauge"] = run_count_gauge
        if run_duration_gauge is not UNSET:
            field_dict["run_duration_gauge"] = run_duration_gauge
        if token_count_gauge is not UNSET:
            field_dict["token_count_gauge"] = token_count_gauge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_count_gauge import DeploymentCountGauge
        from ..models.deployment_duration_gauge import DeploymentDurationGauge
        from ..models.deployment_error_rate_gauge import DeploymentErrorRateGauge
        from ..models.duration_plot import DurationPlot
        from ..models.error_rate_gauge import ErrorRateGauge
        from ..models.run_count_gauge import RunCountGauge
        from ..models.run_duration_gauge import RunDurationGauge
        from ..models.token_count_gauge import TokenCountGauge

        d = dict(src_dict)
        _deployment_count_gauge = d.pop("deployment_count_gauge", UNSET)
        deployment_count_gauge: Union[Unset, DeploymentCountGauge]
        if isinstance(_deployment_count_gauge, Unset):
            deployment_count_gauge = UNSET
        else:
            deployment_count_gauge = DeploymentCountGauge.from_dict(_deployment_count_gauge)

        _deployment_duration_gauge = d.pop("deployment_duration_gauge", UNSET)
        deployment_duration_gauge: Union[Unset, DeploymentDurationGauge]
        if isinstance(_deployment_duration_gauge, Unset):
            deployment_duration_gauge = UNSET
        else:
            deployment_duration_gauge = DeploymentDurationGauge.from_dict(_deployment_duration_gauge)

        _deployment_error_rate_gauge = d.pop("deployment_error_rate_gauge", UNSET)
        deployment_error_rate_gauge: Union[Unset, DeploymentErrorRateGauge]
        if isinstance(_deployment_error_rate_gauge, Unset):
            deployment_error_rate_gauge = UNSET
        else:
            deployment_error_rate_gauge = DeploymentErrorRateGauge.from_dict(_deployment_error_rate_gauge)

        _duration_plot = d.pop("duration_plot", UNSET)
        duration_plot: Union[Unset, DurationPlot]
        if isinstance(_duration_plot, Unset):
            duration_plot = UNSET
        else:
            duration_plot = DurationPlot.from_dict(_duration_plot)

        _error_rate_gauge = d.pop("error_rate_gauge", UNSET)
        error_rate_gauge: Union[Unset, ErrorRateGauge]
        if isinstance(_error_rate_gauge, Unset):
            error_rate_gauge = UNSET
        else:
            error_rate_gauge = ErrorRateGauge.from_dict(_error_rate_gauge)

        _run_count_gauge = d.pop("run_count_gauge", UNSET)
        run_count_gauge: Union[Unset, RunCountGauge]
        if isinstance(_run_count_gauge, Unset):
            run_count_gauge = UNSET
        else:
            run_count_gauge = RunCountGauge.from_dict(_run_count_gauge)

        _run_duration_gauge = d.pop("run_duration_gauge", UNSET)
        run_duration_gauge: Union[Unset, RunDurationGauge]
        if isinstance(_run_duration_gauge, Unset):
            run_duration_gauge = UNSET
        else:
            run_duration_gauge = RunDurationGauge.from_dict(_run_duration_gauge)

        _token_count_gauge = d.pop("token_count_gauge", UNSET)
        token_count_gauge: Union[Unset, TokenCountGauge]
        if isinstance(_token_count_gauge, Unset):
            token_count_gauge = UNSET
        else:
            token_count_gauge = TokenCountGauge.from_dict(_token_count_gauge)

        get_structures_dashboard_response_content = cls(
            deployment_count_gauge=deployment_count_gauge,
            deployment_duration_gauge=deployment_duration_gauge,
            deployment_error_rate_gauge=deployment_error_rate_gauge,
            duration_plot=duration_plot,
            error_rate_gauge=error_rate_gauge,
            run_count_gauge=run_count_gauge,
            run_duration_gauge=run_duration_gauge,
            token_count_gauge=token_count_gauge,
        )

        get_structures_dashboard_response_content.additional_properties = d
        return get_structures_dashboard_response_content

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
