from universal_pudo.providers.mondial_relay.mondial_relay_pickup_provider import (
    MondialRelayPickupProvider,
)


def test_search_pickup_points_returns_results():
    provider = MondialRelayPickupProvider()

    results = provider.search_pickup_points()

    assert len(results) == 3


def test_search_pickup_points_filter_by_city():
    provider = MondialRelayPickupProvider()

    results = provider.search_pickup_points(
        city="PARIS"
    )

    assert len(results) == 1

    assert (
        results[0].city
        == "PARIS"
    )


def test_search_pickup_points_filter_by_postal_code():
    provider = MondialRelayPickupProvider()

    results = provider.search_pickup_points(
        postal_code="92130"
    )

    assert len(results) == 1

    assert (
        results[0].postal_code
        == "92130"
    )


def test_search_pickup_points_filter_by_country():
    provider = MondialRelayPickupProvider()

    results = provider.search_pickup_points(
        country_code="FR"
    )

    assert len(results) == 3


def test_get_pickup_point_details_found():
    provider = MondialRelayPickupProvider()

    result = provider.get_pickup_point_details(
        "mondial-relay-001001"
    )

    assert result is not None

    assert (
        result.id
        == "mondial-relay-001001"
    )

    assert (
        result.carrier_pickup_id
        == "001001"
    )


def test_get_pickup_point_details_not_found():
    provider = MondialRelayPickupProvider()

    result = provider.get_pickup_point_details(
        "unknown-id"
    )

    assert result is None