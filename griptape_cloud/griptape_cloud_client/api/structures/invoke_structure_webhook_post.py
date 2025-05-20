from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.invoke_structure_webhook_post_response_content import InvokeStructureWebhookPostResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    structure_id: str,
    *,
    api_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["api_key"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/structures/{structure_id}/webhook",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]
]:
    if response.status_code == 200:
        response_200 = InvokeStructureWebhookPostResponseContent.from_dict(response.json())

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
) -> Response[
    Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    structure_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: Union[Unset, str] = UNSET,
) -> Response[
    Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]
]:
    """Invoke a webhook for a structure, sending the POST body as the first Structure arg. Must have the
    `webhook_enabled` flag set to `true`.

    Args:
        structure_id (str):
        api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        structure_id=structure_id,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    structure_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: Union[Unset, str] = UNSET,
) -> Optional[
    Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]
]:
    """Invoke a webhook for a structure, sending the POST body as the first Structure arg. Must have the
    `webhook_enabled` flag set to `true`.

    Args:
        structure_id (str):
        api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        structure_id=structure_id,
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    structure_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: Union[Unset, str] = UNSET,
) -> Response[
    Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]
]:
    """Invoke a webhook for a structure, sending the POST body as the first Structure arg. Must have the
    `webhook_enabled` flag set to `true`.

    Args:
        structure_id (str):
        api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        structure_id=structure_id,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    structure_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: Union[Unset, str] = UNSET,
) -> Optional[
    Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]
]:
    """Invoke a webhook for a structure, sending the POST body as the first Structure arg. Must have the
    `webhook_enabled` flag set to `true`.

    Args:
        structure_id (str):
        api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, InvokeStructureWebhookPostResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            structure_id=structure_id,
            client=client,
            api_key=api_key,
        )
    ).parsed
