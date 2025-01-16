# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Purchase"]


class Purchase(BaseModel):
    id: Optional[str] = None

    bonus_credits: Optional[float] = FieldInfo(alias="bonusCredits", default=None)

    credits: Optional[float] = None

    expiry_date: Optional[str] = FieldInfo(alias="expiryDate", default=None)

    is_paid: Optional[bool] = FieldInfo(alias="isPaid", default=None)

    order_refenrece: Optional[str] = FieldInfo(alias="orderRefenrece", default=None)

    pack_name: Optional[Literal["Pack50K", "Pack200K", "Pack1M"]] = FieldInfo(alias="packName", default=None)

    purchase_date: Optional[str] = FieldInfo(alias="purchaseDate", default=None)

    total_credits: Optional[float] = FieldInfo(alias="totalCredits", default=None)

    user_id: Optional[str] = FieldInfo(alias="userID", default=None)
