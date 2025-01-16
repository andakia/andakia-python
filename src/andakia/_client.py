# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    users,
    tokens,
    purchases,
    statistics,
    authentication,
    speech_to_text,
    text_to_speech,
    language_understanding,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import AndakiaError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Andakia", "AsyncAndakia", "Client", "AsyncClient"]


class Andakia(SyncAPIClient):
    speech_to_text: speech_to_text.SpeechToTextResource
    language_understanding: language_understanding.LanguageUnderstandingResource
    authentication: authentication.AuthenticationResource
    purchases: purchases.PurchasesResource
    statistics: statistics.StatisticsResource
    tokens: tokens.TokensResource
    text_to_speech: text_to_speech.TextToSpeechResource
    users: users.UsersResource
    with_raw_response: AndakiaWithRawResponse
    with_streaming_response: AndakiaWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous andakia client instance.

        This automatically infers the `bearer_token` argument from the `BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BEARER_TOKEN")
        if bearer_token is None:
            raise AndakiaError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("ANDAKIA_BASE_URL")
        if base_url is None:
            base_url = f"//api.andakia.tech/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.speech_to_text = speech_to_text.SpeechToTextResource(self)
        self.language_understanding = language_understanding.LanguageUnderstandingResource(self)
        self.authentication = authentication.AuthenticationResource(self)
        self.purchases = purchases.PurchasesResource(self)
        self.statistics = statistics.StatisticsResource(self)
        self.tokens = tokens.TokensResource(self)
        self.text_to_speech = text_to_speech.TextToSpeechResource(self)
        self.users = users.UsersResource(self)
        self.with_raw_response = AndakiaWithRawResponse(self)
        self.with_streaming_response = AndakiaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncAndakia(AsyncAPIClient):
    speech_to_text: speech_to_text.AsyncSpeechToTextResource
    language_understanding: language_understanding.AsyncLanguageUnderstandingResource
    authentication: authentication.AsyncAuthenticationResource
    purchases: purchases.AsyncPurchasesResource
    statistics: statistics.AsyncStatisticsResource
    tokens: tokens.AsyncTokensResource
    text_to_speech: text_to_speech.AsyncTextToSpeechResource
    users: users.AsyncUsersResource
    with_raw_response: AsyncAndakiaWithRawResponse
    with_streaming_response: AsyncAndakiaWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async andakia client instance.

        This automatically infers the `bearer_token` argument from the `BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BEARER_TOKEN")
        if bearer_token is None:
            raise AndakiaError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("ANDAKIA_BASE_URL")
        if base_url is None:
            base_url = f"//api.andakia.tech/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.speech_to_text = speech_to_text.AsyncSpeechToTextResource(self)
        self.language_understanding = language_understanding.AsyncLanguageUnderstandingResource(self)
        self.authentication = authentication.AsyncAuthenticationResource(self)
        self.purchases = purchases.AsyncPurchasesResource(self)
        self.statistics = statistics.AsyncStatisticsResource(self)
        self.tokens = tokens.AsyncTokensResource(self)
        self.text_to_speech = text_to_speech.AsyncTextToSpeechResource(self)
        self.users = users.AsyncUsersResource(self)
        self.with_raw_response = AsyncAndakiaWithRawResponse(self)
        self.with_streaming_response = AsyncAndakiaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AndakiaWithRawResponse:
    def __init__(self, client: Andakia) -> None:
        self.speech_to_text = speech_to_text.SpeechToTextResourceWithRawResponse(client.speech_to_text)
        self.language_understanding = language_understanding.LanguageUnderstandingResourceWithRawResponse(
            client.language_understanding
        )
        self.authentication = authentication.AuthenticationResourceWithRawResponse(client.authentication)
        self.purchases = purchases.PurchasesResourceWithRawResponse(client.purchases)
        self.statistics = statistics.StatisticsResourceWithRawResponse(client.statistics)
        self.tokens = tokens.TokensResourceWithRawResponse(client.tokens)
        self.text_to_speech = text_to_speech.TextToSpeechResourceWithRawResponse(client.text_to_speech)
        self.users = users.UsersResourceWithRawResponse(client.users)


class AsyncAndakiaWithRawResponse:
    def __init__(self, client: AsyncAndakia) -> None:
        self.speech_to_text = speech_to_text.AsyncSpeechToTextResourceWithRawResponse(client.speech_to_text)
        self.language_understanding = language_understanding.AsyncLanguageUnderstandingResourceWithRawResponse(
            client.language_understanding
        )
        self.authentication = authentication.AsyncAuthenticationResourceWithRawResponse(client.authentication)
        self.purchases = purchases.AsyncPurchasesResourceWithRawResponse(client.purchases)
        self.statistics = statistics.AsyncStatisticsResourceWithRawResponse(client.statistics)
        self.tokens = tokens.AsyncTokensResourceWithRawResponse(client.tokens)
        self.text_to_speech = text_to_speech.AsyncTextToSpeechResourceWithRawResponse(client.text_to_speech)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)


class AndakiaWithStreamedResponse:
    def __init__(self, client: Andakia) -> None:
        self.speech_to_text = speech_to_text.SpeechToTextResourceWithStreamingResponse(client.speech_to_text)
        self.language_understanding = language_understanding.LanguageUnderstandingResourceWithStreamingResponse(
            client.language_understanding
        )
        self.authentication = authentication.AuthenticationResourceWithStreamingResponse(client.authentication)
        self.purchases = purchases.PurchasesResourceWithStreamingResponse(client.purchases)
        self.statistics = statistics.StatisticsResourceWithStreamingResponse(client.statistics)
        self.tokens = tokens.TokensResourceWithStreamingResponse(client.tokens)
        self.text_to_speech = text_to_speech.TextToSpeechResourceWithStreamingResponse(client.text_to_speech)
        self.users = users.UsersResourceWithStreamingResponse(client.users)


class AsyncAndakiaWithStreamedResponse:
    def __init__(self, client: AsyncAndakia) -> None:
        self.speech_to_text = speech_to_text.AsyncSpeechToTextResourceWithStreamingResponse(client.speech_to_text)
        self.language_understanding = language_understanding.AsyncLanguageUnderstandingResourceWithStreamingResponse(
            client.language_understanding
        )
        self.authentication = authentication.AsyncAuthenticationResourceWithStreamingResponse(client.authentication)
        self.purchases = purchases.AsyncPurchasesResourceWithStreamingResponse(client.purchases)
        self.statistics = statistics.AsyncStatisticsResourceWithStreamingResponse(client.statistics)
        self.tokens = tokens.AsyncTokensResourceWithStreamingResponse(client.tokens)
        self.text_to_speech = text_to_speech.AsyncTextToSpeechResourceWithStreamingResponse(client.text_to_speech)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)


Client = Andakia

AsyncClient = AsyncAndakia
