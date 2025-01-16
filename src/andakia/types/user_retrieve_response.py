# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserRetrieveResponse"]


class UserRetrieveResponse(BaseModel):
    api_id: Optional[str] = FieldInfo(alias="_id", default=None)

    address: Optional[str] = None

    country: Optional[str] = None

    created_at: Optional[str] = None

    email: Optional[str] = None

    enable2fac: Optional[bool] = None

    first_name: Optional[str] = None

    is_activated: Optional[bool] = None

    last_login: Optional[str] = None

    last_name: Optional[str] = None

    organizations: Optional[List[str]] = None

    phone_number: Optional[str] = None

    role: Optional[Literal["admin", "super_admin", "dev", "owner"]] = None

    updated_at: Optional[str] = None
