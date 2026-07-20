from universal_pudo.domain.provider_health import (
    ProviderHealth,
)
from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)


class GetProviderHealthUseCase:
    def __init__(
        self,
        provider_factory: ProviderFactory,
    ) -> None:
        self.provider_factory = provider_factory

    def execute(
        self,
    ) -> list[ProviderHealth]:
        return [
            ProviderHealth(
                provider_name=carrier,
                status="UP",
                response_time_ms=None,
            )
            for carrier in self.provider_factory.supported_carriers()
        ]