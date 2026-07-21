from universal_pudo.providers.chronopost.client import (
    ChronopostClient,
)


class DummyResponse:
    def __init__(
        self,
        text: str,
    ) -> None:
        self.text = text

    def raise_for_status(
        self,
    ) -> None:
        return None


def test_chronopost_client_search_pickup_points(
    monkeypatch,
) -> None:
    captured = {}

    def fake_get(
        url,
        *,
        params,
        timeout,
    ):
        captured["url"] = url
        captured["params"] = params
        captured["timeout"] = timeout

        return DummyResponse(
            "<xml>ok</xml>"
        )

    monkeypatch.setattr(
        "requests.get",
        fake_get,
    )

    client = ChronopostClient(
        account_number="ACCOUNT",
        password="PASSWORD",
        timeout=15,
    )

    result = client.search_pickup_points(
        address="10 Rue de Test",
        zip_code="31450",
        city="AYGUESVIVES",
        country_code="FR",
        shipping_date="20/07/2026",
    )

    assert result == "<xml>ok</xml>"

    assert (
        captured["url"]
        == ChronopostClient.BASE_URL
    )

    assert captured["timeout"] == 15

    assert (
        captured["params"]["accountNumber"]
        == "ACCOUNT"
    )

    assert (
        captured["params"]["password"]
        == "PASSWORD"
    )

    assert (
        captured["params"]["address"]
        == "10 Rue de Test"
    )

    assert (
        captured["params"]["zipCode"]
        == "31450"
    )

    assert (
        captured["params"]["city"]
        == "AYGUESVIVES"
    )

    assert (
        captured["params"]["countryCode"]
        == "FR"
    )

    assert (
        captured["params"]["type"]
        == "P"
    )

    assert (
        captured["params"]["productCode"]
        == "86"
    )

    assert (
        captured["params"]["service"]
        == "L"
    )

    assert (
        captured["params"]["weight"]
        == "1"
    )

    assert (
        captured["params"]["shippingDate"]
        == "20/07/2026"
    )