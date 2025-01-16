# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["TokenListResponse", "TokenListResponseItem"]


class TokenListResponseItem(BaseModel):
    access_type: Optional[Literal["read", "write", "readAndWrite"]] = None

    last_usage: Optional[str] = None

    name: Optional[str] = None

    usage: Optional[int] = None


TokenListResponse: TypeAlias = List[TokenListResponseItem]
