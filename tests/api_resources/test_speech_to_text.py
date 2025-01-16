# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from andakia import Andakia, AsyncAndakia
from tests.utils import assert_matches_type
from andakia.types import SpeechToTextTranscribeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeechToText:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_transcribe(self, client: Andakia) -> None:
        speech_to_text = client.speech_to_text.transcribe(
            incoming_file=b"raw file contents",
            sample_rate=0,
            target_language="target_language",
            tempo_factor=0,
        )
        assert_matches_type(SpeechToTextTranscribeResponse, speech_to_text, path=["response"])

    @parametrize
    def test_raw_response_transcribe(self, client: Andakia) -> None:
        response = client.speech_to_text.with_raw_response.transcribe(
            incoming_file=b"raw file contents",
            sample_rate=0,
            target_language="target_language",
            tempo_factor=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech_to_text = response.parse()
        assert_matches_type(SpeechToTextTranscribeResponse, speech_to_text, path=["response"])

    @parametrize
    def test_streaming_response_transcribe(self, client: Andakia) -> None:
        with client.speech_to_text.with_streaming_response.transcribe(
            incoming_file=b"raw file contents",
            sample_rate=0,
            target_language="target_language",
            tempo_factor=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech_to_text = response.parse()
            assert_matches_type(SpeechToTextTranscribeResponse, speech_to_text, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeechToText:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_transcribe(self, async_client: AsyncAndakia) -> None:
        speech_to_text = await async_client.speech_to_text.transcribe(
            incoming_file=b"raw file contents",
            sample_rate=0,
            target_language="target_language",
            tempo_factor=0,
        )
        assert_matches_type(SpeechToTextTranscribeResponse, speech_to_text, path=["response"])

    @parametrize
    async def test_raw_response_transcribe(self, async_client: AsyncAndakia) -> None:
        response = await async_client.speech_to_text.with_raw_response.transcribe(
            incoming_file=b"raw file contents",
            sample_rate=0,
            target_language="target_language",
            tempo_factor=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech_to_text = await response.parse()
        assert_matches_type(SpeechToTextTranscribeResponse, speech_to_text, path=["response"])

    @parametrize
    async def test_streaming_response_transcribe(self, async_client: AsyncAndakia) -> None:
        async with async_client.speech_to_text.with_streaming_response.transcribe(
            incoming_file=b"raw file contents",
            sample_rate=0,
            target_language="target_language",
            tempo_factor=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech_to_text = await response.parse()
            assert_matches_type(SpeechToTextTranscribeResponse, speech_to_text, path=["response"])

        assert cast(Any, response.is_closed) is True
