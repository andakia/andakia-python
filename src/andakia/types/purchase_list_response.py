# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .purchase import Purchase

__all__ = ["PurchaseListResponse"]

PurchaseListResponse: TypeAlias = List[Purchase]
