from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...models.update_retriever_request_content import UpdateRetrieverRequestContent
from ...models.update_retriever_response_content import UpdateRetrieverResponseContent
from ...types import Response


def _get_kwargs(
    retriever_id: str,
    *,
    body: UpdateRetrieverRequestContent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/retrievers/{retriever_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]]:
    if response.status_code == 200:
        response_200 = UpdateRetrieverResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    retriever_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateRetrieverRequestContent,
) -> Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]]:
    """
    Args:
        retriever_id (str):
        body (UpdateRetrieverRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    retriever_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateRetrieverRequestContent,
) -> Optional[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]]:
    """
    Args:
        retriever_id (str):
        body (UpdateRetrieverRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]
    """

    return sync_detailed(
        retriever_id=retriever_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    retriever_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateRetrieverRequestContent,
) -> Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]]:
    """
    Args:
        retriever_id (str):
        body (UpdateRetrieverRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retriever_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateRetrieverRequestContent,
) -> Optional[Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]]:
    """
    Args:
        retriever_id (str):
        body (UpdateRetrieverRequestContent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ServiceErrorResponseContent, UpdateRetrieverResponseContent]
    """

    return (
        await asyncio_detailed(
            retriever_id=retriever_id,
            client=client,
            body=body,
        )
    ).parsed
