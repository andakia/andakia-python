# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import purchase_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.purchase import Purchase
from ..types.purchase_list_response import PurchaseListResponse
from ..types.purchase_create_response import PurchaseCreateResponse

__all__ = ["PurchasesResource", "AsyncPurchasesResource"]


class PurchasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andakia/andakia-python#accessing-raw-response-data-eg-headers
        """
        return PurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andakia/andakia-python#with_streaming_response
        """
        return PurchasesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        pack_type: Literal["Pack50K", "Pack200K", "Pack1M"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseCreateResponse:
        """
        This endpoint allows an authorized admin user to create a new purchase with
        specified pack details and returns a checkout URL for payment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/purchase",
            body=maybe_transform({"pack_type": pack_type}, purchase_create_params.PurchaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseCreateResponse,
        )

    def retrieve(
        self,
        purchase_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Purchase:
        """
        This endpoint retrieves details of a single purchase by purchase ID for an
        authorized user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purchase_id:
            raise ValueError(f"Expected a non-empty value for `purchase_id` but received {purchase_id!r}")
        return self._get(
            f"/purchase/{purchase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Purchase,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseListResponse:
        """This endpoint retrieves all purchases for an authorized user."""
        return self._get(
            "/purchase",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseListResponse,
        )


class AsyncPurchasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andakia/andakia-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andakia/andakia-python#with_streaming_response
        """
        return AsyncPurchasesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        pack_type: Literal["Pack50K", "Pack200K", "Pack1M"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseCreateResponse:
        """
        This endpoint allows an authorized admin user to create a new purchase with
        specified pack details and returns a checkout URL for payment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/purchase",
            body=await async_maybe_transform({"pack_type": pack_type}, purchase_create_params.PurchaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseCreateResponse,
        )

    async def retrieve(
        self,
        purchase_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Purchase:
        """
        This endpoint retrieves details of a single purchase by purchase ID for an
        authorized user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purchase_id:
            raise ValueError(f"Expected a non-empty value for `purchase_id` but received {purchase_id!r}")
        return await self._get(
            f"/purchase/{purchase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Purchase,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseListResponse:
        """This endpoint retrieves all purchases for an authorized user."""
        return await self._get(
            "/purchase",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseListResponse,
        )


class PurchasesResourceWithRawResponse:
    def __init__(self, purchases: PurchasesResource) -> None:
        self._purchases = purchases

        self.create = to_raw_response_wrapper(
            purchases.create,
        )
        self.retrieve = to_raw_response_wrapper(
            purchases.retrieve,
        )
        self.list = to_raw_response_wrapper(
            purchases.list,
        )


class AsyncPurchasesResourceWithRawResponse:
    def __init__(self, purchases: AsyncPurchasesResource) -> None:
        self._purchases = purchases

        self.create = async_to_raw_response_wrapper(
            purchases.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            purchases.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            purchases.list,
        )


class PurchasesResourceWithStreamingResponse:
    def __init__(self, purchases: PurchasesResource) -> None:
        self._purchases = purchases

        self.create = to_streamed_response_wrapper(
            purchases.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            purchases.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            purchases.list,
        )


class AsyncPurchasesResourceWithStreamingResponse:
    def __init__(self, purchases: AsyncPurchasesResource) -> None:
        self._purchases = purchases

        self.create = async_to_streamed_response_wrapper(
            purchases.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            purchases.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            purchases.list,
        )
