from universal_pudo.providers.colissimo.colissimo_pickup_provider import (
    ColissimoPickupProvider,
)


def test_search_pickup_points_returns_results():
    provider = ColissimoPickupProvider()

    results = provider.search_pickup_points()

    assert len(results) == 3


def test_search_pickup_points_filter_by_city():
    provider = ColissimoPickupProvider()

    results = provider.search_pickup_points(
        city="PARIS"
    )

    assert len(results) == 2

    assert all(
        point.city == "PARIS"
        for point in results
    )


def test_search_pickup_points_filter_by_postal_code():
    provider = ColissimoPickupProvider()

    results = provider.search_pickup_points(
        postal_code="92130"
    )

    assert len(results) == 1

    assert (
        results[0].postal_code
        == "92130"
    )


def test_search_pickup_points_filter_by_country():
    provider = ColissimoPickupProvider()

    results = provider.search_pickup_points(
        country_code="FR"
    )

    assert len(results) == 3


def test_get_pickup_point_details_found():
    provider = ColissimoPickupProvider()

    result = provider.get_pickup_point_details(
        "colissimo-paris-1"
    )

    assert result is not None

    assert (
        result.id
        == "colissimo-paris-1"
    )

    assert (
        result.carrier_pickup_id
        == "923560"
    )


def test_get_pickup_point_details_not_found():
    provider = ColissimoPickupProvider()

    result = provider.get_pickup_point_details(
        "unknown-id"
    )

    assert result is None