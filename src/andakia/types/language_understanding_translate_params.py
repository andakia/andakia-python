# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LanguageUnderstandingTranslateParams"]


class LanguageUnderstandingTranslateParams(TypedDict, total=False):
    prompt: Required[str]

    query: Required[str]

    target_language: Required[Literal["fr", "wo", "en"]]
