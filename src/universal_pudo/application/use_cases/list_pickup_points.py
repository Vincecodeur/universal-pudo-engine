from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)


class ListPickupPointsUseCase:
    def __init__(
        self,
        repository: PickupPointRepository,
    ) -> None:
        self.repository = repository

    def execute(
        self,
        carrier_id: str,
    ):
        return self.repository.list_by_carrier(
            carrier_id,
        )