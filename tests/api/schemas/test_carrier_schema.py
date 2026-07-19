from universal_pudo.api.schemas.carrier import (
    CarrierResponse,
)


def test_carrier_response_can_be_created() -> None:
    schema = CarrierResponse(
        id="carrier-001",
        code="colissimo_pickup",
        name="Colissimo Pickup",
        lifecycle="ACTIVE",
    )

    assert schema.id == "carrier-001"
    assert schema.code == "colissimo_pickup"
    assert schema.name == "Colissimo Pickup"
    assert schema.lifecycle == "ACTIVE"


def test_carrier_response_can_be_serialized() -> None:
    schema = CarrierResponse(
        id="carrier-001",
        code="colissimo_pickup",
        name="Colissimo Pickup",
        lifecycle="ACTIVE",
    )

    data = schema.model_dump()

    assert data == {
        "id": "carrier-001",
        "code": "colissimo_pickup",
        "name": "Colissimo Pickup",
        "lifecycle": "ACTIVE",
    }