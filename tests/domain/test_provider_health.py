from universal_pudo.domain.provider_health import (
    ProviderHealth,
)


def test_provider_health_creation() -> None:
    health = ProviderHealth(
        provider_name="colissimo",
        status="UP",
    )

    assert health.provider_name == "colissimo"
    assert health.status == "UP"
    assert health.response_time_ms is None