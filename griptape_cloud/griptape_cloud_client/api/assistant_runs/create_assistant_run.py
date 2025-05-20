from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.create_assistant_run_request_content import CreateAssistantRunRequestContent
from ...models.create_assistant_run_response_content import CreateAssistantRunResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import Response


def _get_kwargs(
    assistant_id: str,
    *,
    body: CreateAssistantRunRequestContent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/assistants/{assistant_id}/runs",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 201:
        response_201 = CreateAssistantRunResponseContent.from_dict(response.json())

        return response_201
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
) -> Response[Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    assistant_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAssistantRunRequestContent,
) -> Response[Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        assistant_id (str):
        body (CreateAssistantRunRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    assistant_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAssistantRunRequestContent,
) -> Optional[Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        assistant_id (str):
        body (CreateAssistantRunRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        assistant_id=assistant_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    assistant_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAssistantRunRequestContent,
) -> Response[Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        assistant_id (str):
        body (CreateAssistantRunRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assistant_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAssistantRunRequestContent,
) -> Optional[Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        assistant_id (str):
        body (CreateAssistantRunRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, CreateAssistantRunResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            assistant_id=assistant_id,
            client=client,
            body=body,
        )
    ).parsed
