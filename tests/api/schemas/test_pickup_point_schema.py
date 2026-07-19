from universal_pudo.api.schemas.pickup_point import (
    PickupPointResponse,
)


def test_pickup_point_response_can_be_created() -> None:
    schema = PickupPointResponse(
        id="pickup-point-001",
        carrier_id="carrier-001",
        carrier_pickup_id="COL-001",
        name="Demo Pickup Point",
        pickup_type="STORE",
        city="Paris",
        country_code="FR",
    )

    assert schema.id == "pickup-point-001"
    assert schema.carrier_id == "carrier-001"
    assert schema.carrier_pickup_id == "COL-001"
    assert schema.name == "Demo Pickup Point"
    assert schema.pickup_type == "STORE"
    assert schema.city == "Paris"
    assert schema.country_code == "FR"


def test_pickup_point_response_can_be_serialized() -> None:
    schema = PickupPointResponse(
        id="pickup-point-001",
        carrier_id="carrier-001",
        carrier_pickup_id="COL-001",
        name="Demo Pickup Point",
        pickup_type="STORE",
        city="Paris",
        country_code="FR",
    )

    data = schema.model_dump()

    assert data == {
        "id": "pickup-point-001",
        "carrier_id": "carrier-001",
        "carrier_pickup_id": "COL-001",
        "name": "Demo Pickup Point",
        "pickup_type": "STORE",
        "city": "Paris",
        "country_code": "FR",
    }