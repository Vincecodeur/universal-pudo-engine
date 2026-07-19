from enum import StrEnum


class PickupType(StrEnum):
    """
    Supported pickup point types.
    """

    STORE = "STORE"
    LOCKER = "LOCKER"