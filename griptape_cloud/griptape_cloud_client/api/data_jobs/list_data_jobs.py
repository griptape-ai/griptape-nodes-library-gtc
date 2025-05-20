from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.data_job_status import DataJobStatus
from ...models.list_data_jobs_response_content import ListDataJobsResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    data_connector_id: str,
    *,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[DataJobStatus]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/data-connectors/{data_connector_id}/data-jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = ListDataJobsResponseContent.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ClientErrorResponseContent.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = ServiceErrorResponseContent.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[DataJobStatus]] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        data_connector_id (str):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        status (Union[Unset, list[DataJobStatus]]): Comma-separated list of statuses to filter by.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        data_connector_id=data_connector_id,
        page=page,
        page_size=page_size,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[DataJobStatus]] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        data_connector_id (str):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        status (Union[Unset, list[DataJobStatus]]): Comma-separated list of statuses to filter by.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        data_connector_id=data_connector_id,
        client=client,
        page=page,
        page_size=page_size,
        status=status,
    ).parsed


async def asyncio_detailed(
    data_connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[DataJobStatus]] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        data_connector_id (str):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        status (Union[Unset, list[DataJobStatus]]): Comma-separated list of statuses to filter by.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        data_connector_id=data_connector_id,
        page=page,
        page_size=page_size,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[DataJobStatus]] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        data_connector_id (str):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        status (Union[Unset, list[DataJobStatus]]): Comma-separated list of statuses to filter by.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListDataJobsResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            data_connector_id=data_connector_id,
            client=client,
            page=page,
            page_size=page_size,
            status=status,
        )
    ).parsed
