from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)


class SearchPickupPointsByRadiusUseCase:
    def __init__(
        self,
        repository: PickupPointRepository,
    ) -> None:
        self.repository = repository

    def execute(
        self,
        latitude: float,
        longitude: float,
        radius_km: float,
    ):
        return self.repository.search_by_radius(
            latitude,
            longitude,
            radius_km,
        )