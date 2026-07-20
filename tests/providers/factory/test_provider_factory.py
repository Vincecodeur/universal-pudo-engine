import pytest

from universal_pudo.providers.exceptions import (
    ProviderNotFoundError,
)
from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)


class DummyProvider:
    pass


def test_returns_colissimo_provider():
    colissimo = DummyProvider()

    factory = ProviderFactory(
        {
            "colissimo": colissimo,
        }
    )

    result = factory.get_provider(
        "colissimo"
    )

    assert result is colissimo


def test_returns_mondial_relay_provider():
    mondial_relay = DummyProvider()

    factory = ProviderFactory(
        {
            "mondial-relay": mondial_relay,
        }
    )

    result = factory.get_provider(
        "mondial-relay"
    )

    assert result is mondial_relay


def test_raises_when_provider_not_found():
    factory = ProviderFactory(
        {}
    )

    with pytest.raises(
        ProviderNotFoundError
    ):
        factory.get_provider(
            "unknown"
        )


def test_supported_carriers_returns_sorted_list():
    factory = ProviderFactory(
        {
            "mondial-relay": DummyProvider(),
            "colissimo": DummyProvider(),
        }
    )

    result = (
        factory.supported_carriers()
    )

    assert result == [
        "colissimo",
        "mondial-relay",
    ]


def test_supported_carriers_returns_empty_list():
    factory = ProviderFactory(
        {}
    )

    result = (
        factory.supported_carriers()
    )

    assert result == []