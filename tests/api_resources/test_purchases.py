# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from andakia import Andakia, AsyncAndakia
from tests.utils import assert_matches_type
from andakia.types import Purchase, PurchaseListResponse, PurchaseCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurchases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Andakia) -> None:
        purchase = client.purchases.create(
            pack_type="Pack50K",
        )
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Andakia) -> None:
        response = client.purchases.with_raw_response.create(
            pack_type="Pack50K",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = response.parse()
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Andakia) -> None:
        with client.purchases.with_streaming_response.create(
            pack_type="Pack50K",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = response.parse()
            assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Andakia) -> None:
        purchase = client.purchases.retrieve(
            "purchaseId",
        )
        assert_matches_type(Purchase, purchase, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Andakia) -> None:
        response = client.purchases.with_raw_response.retrieve(
            "purchaseId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = response.parse()
        assert_matches_type(Purchase, purchase, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Andakia) -> None:
        with client.purchases.with_streaming_response.retrieve(
            "purchaseId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = response.parse()
            assert_matches_type(Purchase, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Andakia) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purchase_id` but received ''"):
            client.purchases.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Andakia) -> None:
        purchase = client.purchases.list()
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Andakia) -> None:
        response = client.purchases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = response.parse()
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Andakia) -> None:
        with client.purchases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = response.parse()
            assert_matches_type(PurchaseListResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPurchases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAndakia) -> None:
        purchase = await async_client.purchases.create(
            pack_type="Pack50K",
        )
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAndakia) -> None:
        response = await async_client.purchases.with_raw_response.create(
            pack_type="Pack50K",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = await response.parse()
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAndakia) -> None:
        async with async_client.purchases.with_streaming_response.create(
            pack_type="Pack50K",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = await response.parse()
            assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAndakia) -> None:
        purchase = await async_client.purchases.retrieve(
            "purchaseId",
        )
        assert_matches_type(Purchase, purchase, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAndakia) -> None:
        response = await async_client.purchases.with_raw_response.retrieve(
            "purchaseId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = await response.parse()
        assert_matches_type(Purchase, purchase, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAndakia) -> None:
        async with async_client.purchases.with_streaming_response.retrieve(
            "purchaseId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = await response.parse()
            assert_matches_type(Purchase, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAndakia) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purchase_id` but received ''"):
            await async_client.purchases.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncAndakia) -> None:
        purchase = await async_client.purchases.list()
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAndakia) -> None:
        response = await async_client.purchases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = await response.parse()
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAndakia) -> None:
        async with async_client.purchases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = await response.parse()
            assert_matches_type(PurchaseListResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True
