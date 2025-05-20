from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.function_run_status import FunctionRunStatus
from ...models.list_function_runs_response_content import ListFunctionRunsResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    function_id: str,
    *,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[FunctionRunStatus]] = UNSET,
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
        "url": f"/functions/{function_id}/runs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = ListFunctionRunsResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    function_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[FunctionRunStatus]] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        function_id (str):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        status (Union[Unset, list[FunctionRunStatus]]): Comma-separated list of run statuses to
            filter by.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        function_id=function_id,
        page=page,
        page_size=page_size,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    function_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[FunctionRunStatus]] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        function_id (str):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        status (Union[Unset, list[FunctionRunStatus]]): Comma-separated list of run statuses to
            filter by.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        function_id=function_id,
        client=client,
        page=page,
        page_size=page_size,
        status=status,
    ).parsed


async def asyncio_detailed(
    function_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[FunctionRunStatus]] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        function_id (str):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        status (Union[Unset, list[FunctionRunStatus]]): Comma-separated list of run statuses to
            filter by.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        function_id=function_id,
        page=page,
        page_size=page_size,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    function_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    status: Union[Unset, list[FunctionRunStatus]] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        function_id (str):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        status (Union[Unset, list[FunctionRunStatus]]): Comma-separated list of run statuses to
            filter by.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListFunctionRunsResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            function_id=function_id,
            client=client,
            page=page,
            page_size=page_size,
            status=status,
        )
    ).parsed
