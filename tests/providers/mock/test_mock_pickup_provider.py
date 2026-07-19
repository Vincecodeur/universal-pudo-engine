from sqlalchemy.orm import Session

from universal_pudo.providers.mock.mock_pickup_provider import (
    MockPickupProvider,
)


def test_get_pickup_point_details(
    session: Session,
) -> None:
    provider = MockPickupProvider(
        session,
    )

    pickup_point = (
        provider.get_pickup_point_details(
            "pickup-colissimo-paris-rivoli",
        )
    )

    assert pickup_point is not None

    assert (
        pickup_point.id
        == "pickup-colissimo-paris-rivoli"
    )

    assert (
        pickup_point.carrier_id
        == "carrier-colissimo"
    )


def test_search_pickup_points_by_country(
    session: Session,
) -> None:
    provider = MockPickupProvider(
        session,
    )

    results = provider.search_pickup_points(
        country_code="FR",
    )

    assert len(results) >= 1


def test_search_pickup_points_by_carrier(
    session: Session,
) -> None:
    provider = MockPickupProvider(
        session,
    )

    results = provider.search_pickup_points(
        carrier_id="carrier-colissimo",
    )

    assert len(results) == 1

    assert (
        results[0].id
        == "pickup-colissimo-paris-rivoli"
    )