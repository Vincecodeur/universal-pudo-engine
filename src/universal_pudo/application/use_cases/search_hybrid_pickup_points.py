from datetime import datetime
from datetime import timezone

from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)
from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)
from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)


class SearchHybridPickupPointsUseCase:
    def __init__(
        self,
        repository: PickupPointRepository,
        provider_factory: ProviderFactory,
    ) -> None:
        self.repository = repository
        self.provider_factory = provider_factory
        self.settings = DatabaseSettings()

    def execute(
        self,
        *,
        carrier_id: str| None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
        active: bool | None = True,
    ):
        cached_results = self.repository.search(
            carrier_id=carrier_id,
            country_code=country_code,
            postal_code=postal_code,
            city=city,
            pickup_type=pickup_type,
            active=active,
        )

        if cached_results:
            if self.repository.is_cache_fresh(
                cached_results,
                self.settings.hybrid_search_cache_ttl_days,
            ):
                return cached_results

        provider = self.provider_factory.get_provider(
            carrier_id
        )

        live_results = provider.search_pickup_points(
            carrier_id=carrier_id,
            country_code=country_code,
            postal_code=postal_code,
            city=city,
        )

        synced_at = datetime.now(
            timezone.utc
        )

        for pickup_point in live_results:
            pickup_point.last_synced_at = synced_at

            self.repository.upsert(
                pickup_point
            )

        return live_results