from datetime import datetime
from datetime import timezone
from unittest.mock import Mock

from universal_pudo.application.use_cases.deactivate_stale_pickup_points import (
    DeactivateStalePickupPointsUseCase,
)


def test_deactivate_stale_pickup_points() -> None:
    cutoff_date = datetime(
        2026,
        7,
        1,
        tzinfo=timezone.utc,
    )

    pickup_point_a = Mock()
    pickup_point_a.active = True

    pickup_point_b = Mock()
    pickup_point_b.active = True

    repository = Mock()
    repository.find_stale_pickup_points.return_value = [
        pickup_point_a,
        pickup_point_b,
    ]

    use_case = DeactivateStalePickupPointsUseCase(
        repository
    )

    result = use_case.execute(
        cutoff_date
    )

    repository.find_stale_pickup_points.assert_called_once_with(
        cutoff_date
    )

    assert result == 2
    assert pickup_point_a.active is False
    assert pickup_point_b.active is False


def test_deactivate_stale_pickup_points_returns_zero_when_empty() -> None:
    cutoff_date = datetime(
        2026,
        7,
        1,
        tzinfo=timezone.utc,
    )

    repository = Mock()
    repository.find_stale_pickup_points.return_value = []

    use_case = DeactivateStalePickupPointsUseCase(
        repository
    )

    result = use_case.execute(
        cutoff_date
    )

    repository.find_stale_pickup_points.assert_called_once_with(
        cutoff_date
    )

    assert result == 0