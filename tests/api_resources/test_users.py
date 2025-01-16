# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from andakia import Andakia, AsyncAndakia
from tests.utils import assert_matches_type
from andakia.types import (
    UserCreateResponse,
    UserRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Andakia) -> None:
        user = client.users.create(
            address="xx",
            country="Senegal",
            email="email",
            first_name="xx",
            last_name="xx",
            password="xxxxxxxx",
            phone_number="phone_number",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Andakia) -> None:
        response = client.users.with_raw_response.create(
            address="xx",
            country="Senegal",
            email="email",
            first_name="xx",
            last_name="xx",
            password="xxxxxxxx",
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Andakia) -> None:
        with client.users.with_streaming_response.create(
            address="xx",
            country="Senegal",
            email="email",
            first_name="xx",
            last_name="xx",
            password="xxxxxxxx",
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Andakia) -> None:
        user = client.users.retrieve(
            "userId",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Andakia) -> None:
        response = client.users.with_raw_response.retrieve(
            "userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Andakia) -> None:
        with client.users.with_streaming_response.retrieve(
            "userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Andakia) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_change_password(self, client: Andakia) -> None:
        user = client.users.change_password(
            current_password="current_password",
            new_password="new_password",
        )
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_raw_response_change_password(self, client: Andakia) -> None:
        response = client.users.with_raw_response.change_password(
            current_password="current_password",
            new_password="new_password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_streaming_response_change_password(self, client: Andakia) -> None:
        with client.users.with_streaming_response.change_password(
            current_password="current_password",
            new_password="new_password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAndakia) -> None:
        user = await async_client.users.create(
            address="xx",
            country="Senegal",
            email="email",
            first_name="xx",
            last_name="xx",
            password="xxxxxxxx",
            phone_number="phone_number",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAndakia) -> None:
        response = await async_client.users.with_raw_response.create(
            address="xx",
            country="Senegal",
            email="email",
            first_name="xx",
            last_name="xx",
            password="xxxxxxxx",
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAndakia) -> None:
        async with async_client.users.with_streaming_response.create(
            address="xx",
            country="Senegal",
            email="email",
            first_name="xx",
            last_name="xx",
            password="xxxxxxxx",
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAndakia) -> None:
        user = await async_client.users.retrieve(
            "userId",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAndakia) -> None:
        response = await async_client.users.with_raw_response.retrieve(
            "userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAndakia) -> None:
        async with async_client.users.with_streaming_response.retrieve(
            "userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAndakia) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_change_password(self, async_client: AsyncAndakia) -> None:
        user = await async_client.users.change_password(
            current_password="current_password",
            new_password="new_password",
        )
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_raw_response_change_password(self, async_client: AsyncAndakia) -> None:
        response = await async_client.users.with_raw_response.change_password(
            current_password="current_password",
            new_password="new_password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_streaming_response_change_password(self, async_client: AsyncAndakia) -> None:
        async with async_client.users.with_streaming_response.change_password(
            current_password="current_password",
            new_password="new_password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True
