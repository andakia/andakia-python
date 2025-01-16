# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TokenRetrieveResponse"]


class TokenRetrieveResponse(BaseModel):
    access_type: Optional[Literal["read", "write", "readAndWrite"]] = None

    last_usage: Optional[str] = None

    name: Optional[str] = None

    usage: Optional[int] = None
