from universal_pudo.domain.enums.pickup_type import PickupType


def test_pickup_type_store_value() -> None:
    assert PickupType.STORE == "STORE"


def test_pickup_type_locker_value() -> None:
    assert PickupType.LOCKER == "LOCKER"