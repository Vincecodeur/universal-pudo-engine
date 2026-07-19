from unittest.mock import Mock

from universal_pudo.application.use_cases.search_pickup_points import (
    SearchPickupPointsUseCase,
)


def test_search_pickup_points_calls_repository() -> None:
    repository = Mock()

    repository.search.return_value = [
        "pickup-point-a",
        "pickup-point-b",
    ]

    use_case = SearchPickupPointsUseCase(
        repository,
    )

    result = use_case.execute(
        carrier_id="carrier-colissimo",
        country_code="FR",
        postal_code="75001",
        city="Paris",
        pickup_type="STORE",
        active=True,
    )

    repository.search.assert_called_once_with(
        carrier_id="carrier-colissimo",
        country_code="FR",
        postal_code="75001",
        city="Paris",
        pickup_type="STORE",
        active=True,
    )

    assert result == [
        "pickup-point-a",
        "pickup-point-b",
    ]