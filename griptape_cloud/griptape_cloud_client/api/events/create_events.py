from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.create_events_request_content import CreateEventsRequestContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import Response


def _get_kwargs(
    structure_run_id: str,
    *,
    body: CreateEventsRequestContent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/structure-runs/{structure_run_id}/events",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202
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
) -> Response[Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    structure_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateEventsRequestContent,
) -> Response[Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        structure_run_id (str):
        body (CreateEventsRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        structure_run_id=structure_run_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    structure_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateEventsRequestContent,
) -> Optional[Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        structure_run_id (str):
        body (CreateEventsRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        structure_run_id=structure_run_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    structure_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateEventsRequestContent,
) -> Response[Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        structure_run_id (str):
        body (CreateEventsRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        structure_run_id=structure_run_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    structure_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateEventsRequestContent,
) -> Optional[Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        structure_run_id (str):
        body (CreateEventsRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClientErrorResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            structure_run_id=structure_run_id,
            client=client,
            body=body,
        )
    ).parsed
