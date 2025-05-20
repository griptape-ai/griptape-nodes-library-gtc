from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error_response_content import ClientErrorResponseContent
from ...models.get_asset_response_content import GetAssetResponseContent
from ...models.service_error_response_content import ServiceErrorResponseContent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_id: str,
    name: str,
    *,
    include_contents: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include_contents"] = include_contents

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/buckets/{bucket_id}/assets/{name}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]]:
    if response.status_code == 200:
        response_200 = GetAssetResponseContent.from_dict(response.json())

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
) -> Response[Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bucket_id: str,
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_contents: Union[Unset, bool] = UNSET,
) -> Response[Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        bucket_id (str):
        name (str):
        include_contents (Union[Unset, bool]): true/false to include contents for the asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        bucket_id=bucket_id,
        name=name,
        include_contents=include_contents,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bucket_id: str,
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_contents: Union[Unset, bool] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        bucket_id (str):
        name (str):
        include_contents (Union[Unset, bool]): true/false to include contents for the asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]
    """

    return sync_detailed(
        bucket_id=bucket_id,
        name=name,
        client=client,
        include_contents=include_contents,
    ).parsed


async def asyncio_detailed(
    bucket_id: str,
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_contents: Union[Unset, bool] = UNSET,
) -> Response[Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        bucket_id (str):
        name (str):
        include_contents (Union[Unset, bool]): true/false to include contents for the asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]]
    """

    kwargs = _get_kwargs(
        bucket_id=bucket_id,
        name=name,
        include_contents=include_contents,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_id: str,
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_contents: Union[Unset, bool] = UNSET,
) -> Optional[Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]]:
    """
    Args:
        bucket_id (str):
        name (str):
        include_contents (Union[Unset, bool]): true/false to include contents for the asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientErrorResponseContent, GetAssetResponseContent, ServiceErrorResponseContent]
    """

    return (
        await asyncio_detailed(
            bucket_id=bucket_id,
            name=name,
            client=client,
            include_contents=include_contents,
        )
    ).parsed
