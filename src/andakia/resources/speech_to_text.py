# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import speech_to_text_transcribe_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from ..types.speech_to_text_transcribe_response import SpeechToTextTranscribeResponse

__all__ = ["SpeechToTextResource", "AsyncSpeechToTextResource"]


class SpeechToTextResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeechToTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andakia/andakia-python#accessing-raw-response-data-eg-headers
        """
        return SpeechToTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeechToTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andakia/andakia-python#with_streaming_response
        """
        return SpeechToTextResourceWithStreamingResponse(self)

    def transcribe(
        self,
        *,
        incoming_file: FileTypes,
        sample_rate: int,
        target_language: str,
        tempo_factor: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpeechToTextTranscribeResponse:
        """
        This endpoint accepts an audio file, processes it, and returns the corresponding
        text transcription. It allows specifying the sample rate and adjusting the tempo
        to handle various types of audio.

        Args:
          incoming_file: Audio file for transcription (supported formats: audio/wav, audio/mpeg,
              audio/ogg, etc.)

          sample_rate: Sample rate of the provided audio file in Hz (e.g., 16000)

          target_language: This is the target language (e.g. en wo or fr)

          tempo_factor: Tempo adjustment factor for playback speed (e.g., 1.0 for normal speed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "incoming_file": incoming_file,
                "sample_rate": sample_rate,
                "target_language": target_language,
                "tempo_factor": tempo_factor,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["incoming_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/asr",
            body=maybe_transform(body, speech_to_text_transcribe_params.SpeechToTextTranscribeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextTranscribeResponse,
        )


class AsyncSpeechToTextResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpeechToTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andakia/andakia-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeechToTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeechToTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andakia/andakia-python#with_streaming_response
        """
        return AsyncSpeechToTextResourceWithStreamingResponse(self)

    async def transcribe(
        self,
        *,
        incoming_file: FileTypes,
        sample_rate: int,
        target_language: str,
        tempo_factor: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpeechToTextTranscribeResponse:
        """
        This endpoint accepts an audio file, processes it, and returns the corresponding
        text transcription. It allows specifying the sample rate and adjusting the tempo
        to handle various types of audio.

        Args:
          incoming_file: Audio file for transcription (supported formats: audio/wav, audio/mpeg,
              audio/ogg, etc.)

          sample_rate: Sample rate of the provided audio file in Hz (e.g., 16000)

          target_language: This is the target language (e.g. en wo or fr)

          tempo_factor: Tempo adjustment factor for playback speed (e.g., 1.0 for normal speed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "incoming_file": incoming_file,
                "sample_rate": sample_rate,
                "target_language": target_language,
                "tempo_factor": tempo_factor,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["incoming_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/asr",
            body=await async_maybe_transform(body, speech_to_text_transcribe_params.SpeechToTextTranscribeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextTranscribeResponse,
        )


class SpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.transcribe = to_raw_response_wrapper(
            speech_to_text.transcribe,
        )


class AsyncSpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.transcribe = async_to_raw_response_wrapper(
            speech_to_text.transcribe,
        )


class SpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.transcribe = to_streamed_response_wrapper(
            speech_to_text.transcribe,
        )


class AsyncSpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.transcribe = async_to_streamed_response_wrapper(
            speech_to_text.transcribe,
        )
