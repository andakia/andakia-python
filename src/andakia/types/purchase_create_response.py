# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PurchaseCreateResponse"]


class PurchaseCreateResponse(BaseModel):
    bonus_credits: Optional[float] = None

    checkout_url: Optional[str] = None

    credits: Optional[float] = None

    expiry_date: Optional[str] = None

    is_paid: Optional[bool] = None

    purchase_date: Optional[str] = None

    total_credits: Optional[float] = None
