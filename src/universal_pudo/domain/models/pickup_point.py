from dataclasses import dataclass

from universal_pudo.domain.enums.pickup_type import PickupType
from universal_pudo.domain.value_objects.address import Address
from universal_pudo.domain.value_objects.geolocation import GeoLocation


@dataclass(slots=True)
class PickupPoint:
    """
    Represents a normalized pickup point.

    This is the primary business entity of Universal PUDO Engine.
    """

    pickup_id: str
    carrier_id: str

    name: str

    pickup_type: PickupType

    address: Address
    geolocation: GeoLocation

    active: bool = True

    opening_hours: str | None = None

    phone_number: str | None = None
    email: str | None = None

    services: list[str] | None = None