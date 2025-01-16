# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from andakia import Andakia, AsyncAndakia
from tests.utils import assert_matches_type
from andakia.types import StatisticRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatistics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Andakia) -> None:
        statistic = client.statistics.retrieve()
        assert_matches_type(StatisticRetrieveResponse, statistic, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Andakia) -> None:
        response = client.statistics.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticRetrieveResponse, statistic, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Andakia) -> None:
        with client.statistics.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticRetrieveResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatistics:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAndakia) -> None:
        statistic = await async_client.statistics.retrieve()
        assert_matches_type(StatisticRetrieveResponse, statistic, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAndakia) -> None:
        response = await async_client.statistics.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticRetrieveResponse, statistic, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAndakia) -> None:
        async with async_client.statistics.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticRetrieveResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True
