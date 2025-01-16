# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import authentication_login_params
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
from ..types.authentication_login_response import AuthenticationLoginResponse

__all__ = ["AuthenticationResource", "AsyncAuthenticationResource"]


class AuthenticationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andakia/andakia-python#accessing-raw-response-data-eg-headers
        """
        return AuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andakia/andakia-python#with_streaming_response
        """
        return AuthenticationResourceWithStreamingResponse(self)

    def login(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationLoginResponse:
        """
        This endpoint authenticates the user by verifying their email and password,
        returning a JWT token upon successful login.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/login",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                authentication_login_params.AuthenticationLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationLoginResponse,
        )


class AsyncAuthenticationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andakia/andakia-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andakia/andakia-python#with_streaming_response
        """
        return AsyncAuthenticationResourceWithStreamingResponse(self)

    async def login(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationLoginResponse:
        """
        This endpoint authenticates the user by verifying their email and password,
        returning a JWT token upon successful login.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/login",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                authentication_login_params.AuthenticationLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationLoginResponse,
        )


class AuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.login = to_raw_response_wrapper(
            authentication.login,
        )


class AsyncAuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.login = async_to_raw_response_wrapper(
            authentication.login,
        )


class AuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.login = to_streamed_response_wrapper(
            authentication.login,
        )


class AsyncAuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.login = async_to_streamed_response_wrapper(
            authentication.login,
        )
