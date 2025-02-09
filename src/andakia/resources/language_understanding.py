# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import language_understanding_translate_params
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

__all__ = ["LanguageUnderstandingResource", "AsyncLanguageUnderstandingResource"]


class LanguageUnderstandingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LanguageUnderstandingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/andakia-python#accessing-raw-response-data-eg-headers
        """
        return LanguageUnderstandingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LanguageUnderstandingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/andakia-python#with_streaming_response
        """
        return LanguageUnderstandingResourceWithStreamingResponse(self)

    def translate(
        self,
        *,
        prompt: str,
        query: str,
        target_language: Literal["fr", "wo", "en"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        This endpoint receives a JSON payload with Wolof text and returns a JSON
        response containing the translation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/comprehend",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "query": query,
                    "target_language": target_language,
                },
                language_understanding_translate_params.LanguageUnderstandingTranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncLanguageUnderstandingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLanguageUnderstandingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/andakia-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLanguageUnderstandingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLanguageUnderstandingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/andakia-python#with_streaming_response
        """
        return AsyncLanguageUnderstandingResourceWithStreamingResponse(self)

    async def translate(
        self,
        *,
        prompt: str,
        query: str,
        target_language: Literal["fr", "wo", "en"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        This endpoint receives a JSON payload with Wolof text and returns a JSON
        response containing the translation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/comprehend",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "query": query,
                    "target_language": target_language,
                },
                language_understanding_translate_params.LanguageUnderstandingTranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class LanguageUnderstandingResourceWithRawResponse:
    def __init__(self, language_understanding: LanguageUnderstandingResource) -> None:
        self._language_understanding = language_understanding

        self.translate = to_raw_response_wrapper(
            language_understanding.translate,
        )


class AsyncLanguageUnderstandingResourceWithRawResponse:
    def __init__(self, language_understanding: AsyncLanguageUnderstandingResource) -> None:
        self._language_understanding = language_understanding

        self.translate = async_to_raw_response_wrapper(
            language_understanding.translate,
        )


class LanguageUnderstandingResourceWithStreamingResponse:
    def __init__(self, language_understanding: LanguageUnderstandingResource) -> None:
        self._language_understanding = language_understanding

        self.translate = to_streamed_response_wrapper(
            language_understanding.translate,
        )


class AsyncLanguageUnderstandingResourceWithStreamingResponse:
    def __init__(self, language_understanding: AsyncLanguageUnderstandingResource) -> None:
        self._language_understanding = language_understanding

        self.translate = async_to_streamed_response_wrapper(
            language_understanding.translate,
        )
