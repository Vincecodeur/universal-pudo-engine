from enum import StrEnum


class CarrierLifecycle(StrEnum):
    """
    Lifecycle states of a carrier integration.
    """

    ACTIVE = "ACTIVE"
    DEPRECATED = "DEPRECATED"
    UNLISTED = "UNLISTED"
    SUNSET = "SUNSET"
    REMOVED = "REMOVED"