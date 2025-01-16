# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from andakia import Andakia, AsyncAndakia
from andakia._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTextToSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Andakia, respx_mock: MockRouter) -> None:
        respx_mock.post("/tts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        text_to_speech = client.text_to_speech.create()
        assert text_to_speech.is_closed
        assert text_to_speech.json() == {"foo": "bar"}
        assert cast(Any, text_to_speech.is_closed) is True
        assert isinstance(text_to_speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: Andakia, respx_mock: MockRouter) -> None:
        respx_mock.post("/tts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        text_to_speech = client.text_to_speech.create(
            output_format="output_format",
            text="text",
        )
        assert text_to_speech.is_closed
        assert text_to_speech.json() == {"foo": "bar"}
        assert cast(Any, text_to_speech.is_closed) is True
        assert isinstance(text_to_speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Andakia, respx_mock: MockRouter) -> None:
        respx_mock.post("/tts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        text_to_speech = client.text_to_speech.with_raw_response.create()

        assert text_to_speech.is_closed is True
        assert text_to_speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert text_to_speech.json() == {"foo": "bar"}
        assert isinstance(text_to_speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Andakia, respx_mock: MockRouter) -> None:
        respx_mock.post("/tts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.text_to_speech.with_streaming_response.create() as text_to_speech:
            assert not text_to_speech.is_closed
            assert text_to_speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert text_to_speech.json() == {"foo": "bar"}
            assert cast(Any, text_to_speech.is_closed) is True
            assert isinstance(text_to_speech, StreamedBinaryAPIResponse)

        assert cast(Any, text_to_speech.is_closed) is True


class TestAsyncTextToSpeech:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncAndakia, respx_mock: MockRouter) -> None:
        respx_mock.post("/tts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        text_to_speech = await async_client.text_to_speech.create()
        assert text_to_speech.is_closed
        assert await text_to_speech.json() == {"foo": "bar"}
        assert cast(Any, text_to_speech.is_closed) is True
        assert isinstance(text_to_speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncAndakia, respx_mock: MockRouter) -> None:
        respx_mock.post("/tts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        text_to_speech = await async_client.text_to_speech.create(
            output_format="output_format",
            text="text",
        )
        assert text_to_speech.is_closed
        assert await text_to_speech.json() == {"foo": "bar"}
        assert cast(Any, text_to_speech.is_closed) is True
        assert isinstance(text_to_speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncAndakia, respx_mock: MockRouter) -> None:
        respx_mock.post("/tts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        text_to_speech = await async_client.text_to_speech.with_raw_response.create()

        assert text_to_speech.is_closed is True
        assert text_to_speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await text_to_speech.json() == {"foo": "bar"}
        assert isinstance(text_to_speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncAndakia, respx_mock: MockRouter) -> None:
        respx_mock.post("/tts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.text_to_speech.with_streaming_response.create() as text_to_speech:
            assert not text_to_speech.is_closed
            assert text_to_speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await text_to_speech.json() == {"foo": "bar"}
            assert cast(Any, text_to_speech.is_closed) is True
            assert isinstance(text_to_speech, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, text_to_speech.is_closed) is True
