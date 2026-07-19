from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Address:
    """
    Normalized postal address.

    Value Object.
    """

    street_line_1: str
    street_line_2: str | None = None

    postal_code: str = ""
    city: str = ""

    state_or_region: str | None = None

    country_code: str = ""

    formatted_address: str | None = None