from datetime import datetime

from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)


class DeactivateStalePickupPointsUseCase:
    def __init__(
        self,
        repository: PickupPointRepository,
    ) -> None:
        self.repository = repository

    def execute(
        self,
        cutoff_date: datetime,
    ) -> int:
        stale_pickup_points = (
            self.repository.find_stale_pickup_points(
                cutoff_date
            )
        )

        for pickup_point in stale_pickup_points:
            pickup_point.active = False

        return len(
            stale_pickup_points
        )