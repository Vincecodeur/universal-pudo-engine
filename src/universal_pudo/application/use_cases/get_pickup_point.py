from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)


class GetPickupPointUseCase:
    def __init__(
        self,
        repository: PickupPointRepository,
    ) -> None:
        self.repository = repository

    def execute(
        self,
        pickup_point_id: str,
    ):
        return self.repository.get_by_id(
            pickup_point_id,
        )