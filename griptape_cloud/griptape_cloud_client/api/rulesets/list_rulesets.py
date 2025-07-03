from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.list_rulesets_response_content import ListRulesetsResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    alias: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["alias"] = alias

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rulesets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = ListRulesetsResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    alias: Union[Unset, str] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        alias (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        alias=alias,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    alias: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        alias (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        alias=alias,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    alias: Union[Unset, str] = UNSET,
) -> Response[Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        alias (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        alias=alias,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    alias: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        alias (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, ListRulesetsResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            alias=alias,
        )
    ).parsed
