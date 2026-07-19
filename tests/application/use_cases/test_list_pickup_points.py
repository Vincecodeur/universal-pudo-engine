from unittest.mock import Mock

from universal_pudo.application.use_cases.list_pickup_points import (
    ListPickupPointsUseCase,
)


def test_list_pickup_points_calls_repository() -> None:
    repository = Mock()

    repository.list_by_carrier.return_value = [
        "point-a",
        "point-b",
    ]

    use_case = ListPickupPointsUseCase(
        repository,
    )

    result = use_case.execute(
        "carrier-001",
    )

    repository.list_by_carrier.assert_called_once_with(
        "carrier-001",
    )

    assert len(result) == 2