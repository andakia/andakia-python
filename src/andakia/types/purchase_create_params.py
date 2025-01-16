# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PurchaseCreateParams"]


class PurchaseCreateParams(TypedDict, total=False):
    pack_type: Required[Literal["Pack50K", "Pack200K", "Pack1M"]]
