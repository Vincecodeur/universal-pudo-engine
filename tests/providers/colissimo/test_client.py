from universal_pudo.providers.colissimo.client import (
    ColissimoClient,
)


def test_client_stores_api_key():
    client = ColissimoClient(
        api_key="TEST"
    )

    assert client.api_key == "TEST"