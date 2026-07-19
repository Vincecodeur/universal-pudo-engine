from universal_pudo.domain.enums.carrier_capability import CarrierCapability
from universal_pudo.domain.enums.carrier_lifecycle import CarrierLifecycle
from universal_pudo.domain.models.carrier import Carrier


def test_carrier_can_be_created_with_required_fields() -> None:
    carrier = Carrier(
        carrier_id="carrier-001",
        code="colissimo_pickup",
        name="Colissimo Pickup",
    )

    assert carrier.carrier_id == "carrier-001"
    assert carrier.code == "colissimo_pickup"
    assert carrier.name == "Colissimo Pickup"
    assert carrier.lifecycle == CarrierLifecycle.ACTIVE
    assert carrier.supported_countries == []
    assert carrier.capabilities == []


def test_carrier_can_be_created_with_supported_countries_and_capabilities() -> None:
    carrier = Carrier(
        carrier_id="carrier-002",
        code="mondial_relay",
        name="Mondial Relay",
        lifecycle=CarrierLifecycle.ACTIVE,
        supported_countries=["FR", "BE"],
        capabilities=[
            CarrierCapability.SEARCH_PICKUP_POINTS,
            CarrierCapability.GET_PICKUP_DETAILS,
        ],
    )

    assert carrier.supported_countries == ["FR", "BE"]
    assert CarrierCapability.SEARCH_PICKUP_POINTS in carrier.capabilities
    assert CarrierCapability.GET_PICKUP_DETAILS in carrier.capabilities