from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.list_function_run_logs_response_content import ListFunctionRunLogsResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import Response


def _get_kwargs(
    function_run_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/function-runs/{function_run_id}/logs",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = ListFunctionRunLogsResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    function_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        function_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        function_run_id=function_run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    function_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        function_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        function_run_id=function_run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    function_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        function_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        function_run_id=function_run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    function_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        function_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListFunctionRunLogsResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            function_run_id=function_run_id,
            client=client,
        )
    ).parsed
