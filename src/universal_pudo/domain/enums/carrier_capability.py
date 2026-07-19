from enum import StrEnum


class CarrierCapability(StrEnum):
    """
    Features supported by a carrier integration.
    """

    SEARCH_PICKUP_POINTS = "SEARCH_PICKUP_POINTS"
    GET_PICKUP_DETAILS = "GET_PICKUP_DETAILS"
    RESOLVE_PICKUP_POINT = "RESOLVE_PICKUP_POINT"