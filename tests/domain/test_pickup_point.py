from universal_pudo.domain.enums.pickup_type import PickupType
from universal_pudo.domain.models.pickup_point import PickupPoint
from universal_pudo.domain.value_objects.address import Address
from universal_pudo.domain.value_objects.geolocation import GeoLocation


def test_pickup_point_can_be_created() -> None:
    pickup_point = PickupPoint(
        pickup_id="MR-001",
        carrier_id="mondial_relay",
        name="Relay Demo",
        pickup_type=PickupType.STORE,
        address=Address(
            street_line_1="10 Rue de Rivoli",
            postal_code="75001",
            city="Paris",
            country_code="FR",
        ),
        geolocation=GeoLocation(
            latitude=48.8566,
            longitude=2.3522,
        ),
    )

    assert pickup_point.pickup_id == "MR-001"
    assert pickup_point.carrier_id == "mondial_relay"
    assert pickup_point.pickup_type == PickupType.STORE
    assert pickup_point.active is True


def test_pickup_point_supports_optional_fields() -> None:
    pickup_point = PickupPoint(
        pickup_id="LOCKER-001",
        carrier_id="carrier-001",
        name="Locker Demo",
        pickup_type=PickupType.LOCKER,
        address=Address(
            street_line_1="1 Main Street",
            postal_code="10000",
            city="Demo City",
            country_code="FR",
        ),
        geolocation=GeoLocation(
            latitude=48.0,
            longitude=2.0,
        ),
        opening_hours="24/7",
        phone_number="+33123456789",
        email="demo@example.com",
        services=["PICKUP", "RETURN"],
    )

    assert pickup_point.pickup_type == PickupType.LOCKER
    assert pickup_point.opening_hours == "24/7"
    assert "RETURN" in pickup_point.services