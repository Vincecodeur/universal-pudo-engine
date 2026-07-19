from universal_pudo.domain.enums.carrier_capability import CarrierCapability


def test_carrier_capability_search_pickup_points_value() -> None:
    assert CarrierCapability.SEARCH_PICKUP_POINTS == "SEARCH_PICKUP_POINTS"


def test_carrier_capability_get_pickup_details_value() -> None:
    assert CarrierCapability.GET_PICKUP_DETAILS == "GET_PICKUP_DETAILS"


def test_carrier_capability_resolve_pickup_point_value() -> None:
    assert CarrierCapability.RESOLVE_PICKUP_POINT == "RESOLVE_PICKUP_POINT"