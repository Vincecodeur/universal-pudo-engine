from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)


class SearchPickupPointsUseCase:
    def __init__(
        self,
        repository: PickupPointRepository,
    ) -> None:
        self.repository = repository

    def execute(
        self,
        carrier_id: str | None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
        active: bool | None = None,
    ):
        return self.repository.search(
            carrier_id=carrier_id,
            country_code=country_code,
            postal_code=postal_code,
            city=city,
            pickup_type=pickup_type,
            active=active,
        )