# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["StatisticRetrieveResponse", "CreditBalance", "CreditBalanceCreditDetail", "Usage"]


class CreditBalanceCreditDetail(BaseModel):
    credits: Optional[float] = None

    expiry_date: Optional[str] = None

    pack_name: Optional[str] = None


class CreditBalance(BaseModel):
    credit_details: Optional[List[CreditBalanceCreditDetail]] = None

    total_credits: Optional[float] = None


class Usage(BaseModel):
    asr: Optional[float] = None

    llm: Optional[float] = None

    tts: Optional[float] = None


class StatisticRetrieveResponse(BaseModel):
    credit_balance: Optional[CreditBalance] = None

    usage: Optional[Usage] = None
