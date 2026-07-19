from universal_pudo.domain.enums.carrier_lifecycle import CarrierLifecycle


def test_carrier_lifecycle_active_value() -> None:
    assert CarrierLifecycle.ACTIVE == "ACTIVE"


def test_carrier_lifecycle_deprecated_value() -> None:
    assert CarrierLifecycle.DEPRECATED == "DEPRECATED"


def test_carrier_lifecycle_unlisted_value() -> None:
    assert CarrierLifecycle.UNLISTED == "UNLISTED"


def test_carrier_lifecycle_sunset_value() -> None:
    assert CarrierLifecycle.SUNSET == "SUNSET"


def test_carrier_lifecycle_removed_value() -> None:
    assert CarrierLifecycle.REMOVED == "REMOVED"