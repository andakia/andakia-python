# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    address: Required[str]

    country: Required[
        Literal[
            "Senegal",
            "Mauritania",
            "Mali",
            "Niger",
            "Cape Verde",
            "Burkina Faso",
            "Côte d'Ivoire",
            "Ghana",
            "Togo",
            "Benin",
            "Nigeria",
            "Gambia",
            "Guinea",
            "Guinea-Bissau",
            "Sierra Leone",
            "Liberia",
        ]
    ]

    email: Required[str]

    first_name: Required[str]

    last_name: Required[str]

    password: Required[str]

    phone_number: Required[str]
