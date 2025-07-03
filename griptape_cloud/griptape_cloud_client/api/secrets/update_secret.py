from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...models.update_secret_request_content import UpdateSecretRequestContent
from ...models.update_secret_response_content import UpdateSecretResponseContent
from ...types import Response


def _get_kwargs(
    secret_id: str,
    *,
    body: UpdateSecretRequestContent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/secrets/{secret_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]]:
    if response.status_code == 200:
        response_200 = UpdateSecretResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    secret_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSecretRequestContent,
) -> Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]]:
    """
    Args:
        secret_id (str):
        body (UpdateSecretRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]]
    """

    kwargs = _get_kwargs(
        secret_id=secret_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    secret_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSecretRequestContent,
) -> Optional[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]]:
    """
    Args:
        secret_id (str):
        body (UpdateSecretRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]
    """

    return sync_detailed(
        secret_id=secret_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    secret_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSecretRequestContent,
) -> Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]]:
    """
    Args:
        secret_id (str):
        body (UpdateSecretRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]]
    """

    kwargs = _get_kwargs(
        secret_id=secret_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    secret_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSecretRequestContent,
) -> Optional[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]]:
    """
    Args:
        secret_id (str):
        body (UpdateSecretRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateSecretResponseContent]
    """

    return (
        await asyncio_detailed(
            secret_id=secret_id,
            client=client,
            body=body,
        )
    ).parsed
