from unittest.mock import Mock

from universal_pudo.application.use_cases.search_hybrid_pickup_points import (
    SearchHybridPickupPointsUseCase,
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


def test_returns_cached_results_when_available() -> None:
    cached_pickups = [
        Mock(),
        Mock(),
    ]

    repository = Mock()

    repository.search.return_value = (
        cached_pickups
    )

    provider = DummyProvider(
        []
    )

    factory = ProviderFactory(
        {
            "colissimo": provider,
        }
    )

    use_case = SearchHybridPickupPointsUseCase(
        repository=repository,
        provider_factory=factory,
    )

    result = use_case.execute(
        carrier_id="colissimo",
    )

    assert result == cached_pickups

    repository.search.assert_called_once()

    repository.upsert.assert_not_called()


def test_fallbacks_to_live_provider_when_cache_is_empty() -> None:
    live_pickups = [
        Mock(),
        Mock(),
    ]

    repository = Mock()

    repository.search.return_value = []

    provider = DummyProvider(
        live_pickups
    )

    factory = ProviderFactory(
        {
            "colissimo": provider,
        }
    )

    use_case = SearchHybridPickupPointsUseCase(
        repository=repository,
        provider_factory=factory,
    )

    result = use_case.execute(
        carrier_id="colissimo",
    )

    assert result == live_pickups

    assert repository.upsert.call_count == 2


def test_returns_empty_list_when_cache_and_provider_are_empty() -> None:
    repository = Mock()

    repository.search.return_value = []

    provider = DummyProvider(
        []
    )

    factory = ProviderFactory(
        {
            "colissimo": provider,
        }
    )

    use_case = SearchHybridPickupPointsUseCase(
        repository=repository,
        provider_factory=factory,
    )

    result = use_case.execute(
        carrier_id="colissimo",
    )

    assert result == []

    repository.upsert.assert_not_called()


def test_sets_last_synced_at_when_loading_from_provider() -> None:
    pickup_point = Mock()

    repository = Mock()

    repository.search.return_value = []

    provider = DummyProvider(
        [
            pickup_point,
        ]
    )

    factory = ProviderFactory(
        {
            "colissimo": provider,
        }
    )

    use_case = SearchHybridPickupPointsUseCase(
        repository=repository,
        provider_factory=factory,
    )

    use_case.execute(
        carrier_id="colissimo",
    )

    assert (
        pickup_point.last_synced_at
        is not None
    )

    repository.upsert.assert_called_once_with(
        pickup_point
    )
    
    
def test_refreshes_provider_when_cache_is_stale() -> None:
    stale_cached_pickup = Mock()

    live_pickup = Mock()

    repository = Mock()

    repository.search.return_value = [
        stale_cached_pickup
    ]

    repository.is_cache_fresh.return_value = (
        False
    )

    provider = DummyProvider(
        [
            live_pickup,
        ]
    )

    factory = ProviderFactory(
        {
            "colissimo": provider,
        }
    )

    use_case = SearchHybridPickupPointsUseCase(
        repository=repository,
        provider_factory=factory,
    )

    result = use_case.execute(
        carrier_id="colissimo",
    )

    assert result == [
        live_pickup,
    ]

    repository.upsert.assert_called_once_with(
        live_pickup
    )