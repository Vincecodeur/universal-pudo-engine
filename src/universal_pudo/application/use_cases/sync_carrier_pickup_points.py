from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)
from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)


class SyncCarrierPickupPointsUseCase:
    def __init__(
        self,
        provider_factory: ProviderFactory,
        repository: PickupPointRepository,
    ) -> None:
        self.provider_factory = provider_factory
        self.repository = repository

    def execute(
        self,
        *,
        carrier_id: str,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
    ) -> int:
        provider = self.provider_factory.get_provider(
            carrier_id
        )

        pickup_points = provider.search_pickup_points(
            carrier_id=carrier_id,
            country_code=country_code,
            postal_code=postal_code,
            city=city,
        )

        for pickup_point in pickup_points:
            self.repository.upsert(
                pickup_point
            )

        return len(pickup_points)