# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from andakia import Andakia, AsyncAndakia
from tests.utils import assert_matches_type
from andakia.types import (
    TokenListResponse,
    TokenCreateResponse,
    TokenRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Andakia) -> None:
        token = client.tokens.create(
            access_type="read",
            name="name",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Andakia) -> None:
        response = client.tokens.with_raw_response.create(
            access_type="read",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Andakia) -> None:
        with client.tokens.with_streaming_response.create(
            access_type="read",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Andakia) -> None:
        token = client.tokens.retrieve(
            "tokenName",
        )
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Andakia) -> None:
        response = client.tokens.with_raw_response.retrieve(
            "tokenName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Andakia) -> None:
        with client.tokens.with_streaming_response.retrieve(
            "tokenName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenRetrieveResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Andakia) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_name` but received ''"):
            client.tokens.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Andakia) -> None:
        token = client.tokens.list()
        assert_matches_type(TokenListResponse, token, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Andakia) -> None:
        response = client.tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenListResponse, token, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Andakia) -> None:
        with client.tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenListResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Andakia) -> None:
        token = client.tokens.delete(
            "tokenName",
        )
        assert_matches_type(str, token, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Andakia) -> None:
        response = client.tokens.with_raw_response.delete(
            "tokenName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(str, token, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Andakia) -> None:
        with client.tokens.with_streaming_response.delete(
            "tokenName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(str, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Andakia) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_name` but received ''"):
            client.tokens.with_raw_response.delete(
                "",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAndakia) -> None:
        token = await async_client.tokens.create(
            access_type="read",
            name="name",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAndakia) -> None:
        response = await async_client.tokens.with_raw_response.create(
            access_type="read",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAndakia) -> None:
        async with async_client.tokens.with_streaming_response.create(
            access_type="read",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenCreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAndakia) -> None:
        token = await async_client.tokens.retrieve(
            "tokenName",
        )
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAndakia) -> None:
        response = await async_client.tokens.with_raw_response.retrieve(
            "tokenName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenRetrieveResponse, token, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAndakia) -> None:
        async with async_client.tokens.with_streaming_response.retrieve(
            "tokenName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenRetrieveResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAndakia) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_name` but received ''"):
            await async_client.tokens.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAndakia) -> None:
        token = await async_client.tokens.list()
        assert_matches_type(TokenListResponse, token, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAndakia) -> None:
        response = await async_client.tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenListResponse, token, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAndakia) -> None:
        async with async_client.tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenListResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAndakia) -> None:
        token = await async_client.tokens.delete(
            "tokenName",
        )
        assert_matches_type(str, token, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAndakia) -> None:
        response = await async_client.tokens.with_raw_response.delete(
            "tokenName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(str, token, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAndakia) -> None:
        async with async_client.tokens.with_streaming_response.delete(
            "tokenName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(str, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAndakia) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_name` but received ''"):
            await async_client.tokens.with_raw_response.delete(
                "",
            )
