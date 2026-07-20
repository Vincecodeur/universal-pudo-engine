from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)


class SearchLivePickupPointsUseCase:
    def __init__(
        self,
        provider_factory: ProviderFactory,
    ) -> None:
        self.provider_factory = provider_factory

    def execute(
        self,
        *,
        carrier_id: str,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
    ):
        provider = self.provider_factory.get_provider(
            carrier_id
        )

        return provider.search_pickup_points(
            carrier_id=carrier_id,
            country_code=country_code,
            postal_code=postal_code,
            city=city,
        )
