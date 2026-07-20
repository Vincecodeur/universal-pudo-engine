import pytest

from universal_pudo.application.use_cases.search_live_pickup_points import (
    SearchLivePickupPointsUseCase,
)
from universal_pudo.providers.exceptions import (
    ProviderNotFoundError,
)
from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)


class DummyProvider:
    def search_pickup_points(
        self,
        *,
        carrier_id: str | None =None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str| None = None,
    ):
        return [
            {
                "carrier_id": carrier_id,
                "country_code": country_code,
                "postal_code": postal_code,
                "city": city,
            }
        ]


def test_execute_returns_provider_results():
    factory = ProviderFactory(
        {
            "colissimo": DummyProvider(),
        }
    )
    use_case = SearchLivePickupPointsUseCase(
        provider_factory=factory
    )

    results = use_case.execute(
        carrier_id="colissimo",
        country_code="FR",
        postal_code="92130",
        city="ISSY LES MOULINEAUX",
    )

    assert len(results) == 1
    assert (
        results[0]["carrier_id"]
        == "colissimo"
    )

    assert (
        results[0]["country_code"]
        == "FR"
    )

    assert (
        results[0]["postal_code"]
        == "92130"
    )

    assert (
        results[0]["city"]
        == "ISSY LES MOULINEAUX"
    )


def test_execute_raises_for_unknown_provider():
    factory = ProviderFactory(
        {}
    )

    use_case = SearchLivePickupPointsUseCase(
        provider_factory=factory
    )

    with pytest.raises(
        ProviderNotFoundError
    ):
        use_case.execute(
            carrier_id="unknown",
            country_code="FR",
            postal_code="92130",
            city="ISSY LES MOULINEAUX",
        )