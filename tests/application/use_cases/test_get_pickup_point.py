from unittest.mock import Mock

from universal_pudo.application.use_cases.get_pickup_point import (
    GetPickupPointUseCase,
)


def test_get_pickup_point_calls_repository() -> None:
    repository = Mock()

    repository.get_by_id.return_value = (
        "pickup-point"
    )

    use_case = GetPickupPointUseCase(
        repository,
    )

    result = use_case.execute(
        "pickup-001",
    )

    repository.get_by_id.assert_called_once_with(
        "pickup-001",
    )

    assert result == "pickup-point"