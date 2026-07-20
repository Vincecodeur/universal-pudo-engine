from unittest.mock import Mock

from universal_pudo.application.use_cases.sync_carrier_pickup_points import (
    SyncCarrierPickupPointsUseCase,
)
from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)


class DummyProvider:
    def __init__(
        self,
        pickup_points,
    ) -> None:
        self.pickup_points = pickup_points

    def search_pickup_points(
        self,
        *,
        carrier_id=None,
        country_code=None,
        postal_code=None,
        city=None,
    ):
        return self.pickup_points


def test_sync_pickup_points_saves_all_results() -> None:
    provider = DummyProvider(
        [
            Mock(),
            Mock(),
            Mock(),
        ]
    )

    factory = ProviderFactory(
        {
            "colissimo": provider,
        }
    )

    repository = Mock()

    use_case = SyncCarrierPickupPointsUseCase(
        provider_factory=factory,
        repository=repository,
    )

    result = use_case.execute(
        carrier_id="colissimo",
        country_code="FR",
        postal_code="92130",
        city="ISSY LES MOULINEAUX",
    )

    assert result == 3

    assert repository.save.call_count == 3


def test_sync_returns_zero_when_no_pickup_points() -> None:
    provider = DummyProvider(
        []
    )

    factory = ProviderFactory(
        {
            "colissimo": provider,
        }
    )

    repository = Mock()

    use_case = SyncCarrierPickupPointsUseCase(
        provider_factory=factory,
        repository=repository,
    )

    result = use_case.execute(
        carrier_id="colissimo",
    )

    assert result == 0

    repository.save.assert_not_called()