from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GeoLocation:
    """
    Geographic coordinates.

    Value Object.
    """

    latitude: float
    longitude: float