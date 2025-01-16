# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["SpeechToTextTranscribeParams"]


class SpeechToTextTranscribeParams(TypedDict, total=False):
    incoming_file: Required[FileTypes]
    """
    Audio file for transcription (supported formats: audio/wav, audio/mpeg,
    audio/ogg, etc.)
    """

    sample_rate: Required[int]
    """Sample rate of the provided audio file in Hz (e.g., 16000)"""

    target_language: Required[str]
    """This is the target language (e.g. en wo or fr)"""

    tempo_factor: Required[float]
    """Tempo adjustment factor for playback speed (e.g., 1.0 for normal speed)"""
