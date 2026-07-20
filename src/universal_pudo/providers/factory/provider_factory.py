from universal_pudo.providers.base.pickup_provider import (
    PickupProvider,
)
from universal_pudo.providers.exceptions import (
    ProviderNotFoundError,
)


class ProviderFactory:
    def __init__(
        self,
        providers: dict[str, PickupProvider],
    ) -> None:
        self._providers = providers

    def get_provider(
        self,
        carrier_id: str,
    ) -> PickupProvider:
        provider = self._providers.get(
            carrier_id
        )

        if provider is None:
            raise ProviderNotFoundError(
                (
                    "Provider not found for "
                    f"carrier '{carrier_id}'"
                )
            )

        return provider

    def supported_carriers(
        self,
    ) -> list[str]:
        return sorted(
            self._providers.keys()
        )