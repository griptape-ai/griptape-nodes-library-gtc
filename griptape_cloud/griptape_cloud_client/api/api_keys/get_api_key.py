from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.get_api_key_response_content import GetApiKeyResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import Response


def _get_kwargs(
    api_key_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api-keys/{api_key_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = GetApiKeyResponseContent.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ClientErrorResponseContent.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = ServiceErrorResponseContent.from_dict(response.json())

        return response_500
    if response.status_code == 401:
        response_401 = ClientErrorResponseContent.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ClientErrorResponseContent.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ClientErrorResponseContent.from_dict(response.json())

        return response_404
    if response.status_code == 406:
        response_406 = ClientErrorResponseContent.from_dict(response.json())

        return response_406
    if response.status_code == 409:
        response_409 = ClientErrorResponseContent.from_dict(response.json())

        return response_409
    if response.status_code == 422:
        response_422 = ClientErrorResponseContent.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    api_key_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        api_key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        api_key_id=api_key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    api_key_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        api_key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        api_key_id=api_key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    api_key_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        api_key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        api_key_id=api_key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    api_key_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        api_key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, GetApiKeyResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            api_key_id=api_key_id,
            client=client,
        )
    ).parsed
