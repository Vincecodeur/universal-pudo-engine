from universal_pudo.application.use_cases.get_provider_health import (
    GetProviderHealthUseCase,
)
from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)


class DummyProvider:
    pass


def test_get_provider_health_returns_registered_providers() -> None:
    factory = ProviderFactory(
        {
            "colissimo": DummyProvider(),
            "mondial-relay": DummyProvider(),
        }
    )

    use_case = GetProviderHealthUseCase(
        factory,
    )

    result = use_case.execute()

    assert len(result) == 2

    assert result[0].provider_name == "colissimo"
    assert result[1].provider_name == "mondial-relay"