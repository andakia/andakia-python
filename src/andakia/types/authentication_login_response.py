# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthenticationLoginResponse"]


class AuthenticationLoginResponse(BaseModel):
    token: Optional[str] = None

    token_type: Optional[str] = None
