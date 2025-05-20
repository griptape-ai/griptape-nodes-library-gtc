from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...models.update_data_connector_request_content import UpdateDataConnectorRequestContent
from ...models.update_data_connector_response_content import UpdateDataConnectorResponseContent
from ...types import Response


def _get_kwargs(
    data_connector_id: str,
    *,
    body: UpdateDataConnectorRequestContent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/data-connectors/{data_connector_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]]:
    if response.status_code == 200:
        response_200 = UpdateDataConnectorResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]]:
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
    body: UpdateDataConnectorRequestContent,
) -> Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]]:
    """
    Args:
        data_connector_id (str):
        body (UpdateDataConnectorRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]]
    """

    kwargs = _get_kwargs(
        data_connector_id=data_connector_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDataConnectorRequestContent,
) -> Optional[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]]:
    """
    Args:
        data_connector_id (str):
        body (UpdateDataConnectorRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]
    """

    return sync_detailed(
        data_connector_id=data_connector_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDataConnectorRequestContent,
) -> Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]]:
    """
    Args:
        data_connector_id (str):
        body (UpdateDataConnectorRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]]
    """

    kwargs = _get_kwargs(
        data_connector_id=data_connector_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDataConnectorRequestContent,
) -> Optional[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]]:
    """
    Args:
        data_connector_id (str):
        body (UpdateDataConnectorRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateDataConnectorResponseContent]
    """

    return (
        await asyncio_detailed(
            data_connector_id=data_connector_id,
            client=client,
            body=body,
        )
    ).parsed
