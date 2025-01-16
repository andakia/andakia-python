# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from andakia import Andakia, AsyncAndakia
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLanguageUnderstanding:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_translate(self, client: Andakia) -> None:
        language_understanding = client.language_understanding.translate(
            prompt="prompt",
            query="query",
            target_language="fr",
        )
        assert_matches_type(str, language_understanding, path=["response"])

    @parametrize
    def test_raw_response_translate(self, client: Andakia) -> None:
        response = client.language_understanding.with_raw_response.translate(
            prompt="prompt",
            query="query",
            target_language="fr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language_understanding = response.parse()
        assert_matches_type(str, language_understanding, path=["response"])

    @parametrize
    def test_streaming_response_translate(self, client: Andakia) -> None:
        with client.language_understanding.with_streaming_response.translate(
            prompt="prompt",
            query="query",
            target_language="fr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language_understanding = response.parse()
            assert_matches_type(str, language_understanding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLanguageUnderstanding:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_translate(self, async_client: AsyncAndakia) -> None:
        language_understanding = await async_client.language_understanding.translate(
            prompt="prompt",
            query="query",
            target_language="fr",
        )
        assert_matches_type(str, language_understanding, path=["response"])

    @parametrize
    async def test_raw_response_translate(self, async_client: AsyncAndakia) -> None:
        response = await async_client.language_understanding.with_raw_response.translate(
            prompt="prompt",
            query="query",
            target_language="fr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language_understanding = await response.parse()
        assert_matches_type(str, language_understanding, path=["response"])

    @parametrize
    async def test_streaming_response_translate(self, async_client: AsyncAndakia) -> None:
        async with async_client.language_understanding.with_streaming_response.translate(
            prompt="prompt",
            query="query",
            target_language="fr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language_understanding = await response.parse()
            assert_matches_type(str, language_understanding, path=["response"])

        assert cast(Any, response.is_closed) is True
