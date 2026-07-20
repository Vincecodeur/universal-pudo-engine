from universal_pudo.providers.chronopost.chronopost_live_provider import (
    ChronopostLiveProvider,
)


class DummyChronopostClient:
    def __init__(
        self,
        xml_response: str,
    ) -> None:
        self.xml_response = xml_response
        self.calls: list[dict] = []

    def search_pickup_points(
        self,
        *,
        address: str,
        zip_code: str,
        city: str,
        country_code: str,
        shipping_date: str,
    ) -> str:
        self.calls.append(
            {
                "address": address,
                "zip_code": zip_code,
                "city": city,
                "country_code": country_code,
                "shipping_date": shipping_date,
            }
        )

        return self.xml_response


def test_chronopost_live_provider_returns_pickup_points() -> None:
    xml_response = """
    <root>
        <listePointRelais>
            <identifiant>1487R</identifiant>
            <nom>LE BISTROT DU COIN</nom>
            <adresse1>29 ROUTE DE TICAILLE</adresse1>
            <adresse2></adresse2>
            <adresse3></adresse3>
            <codePostal>31450</codePostal>
            <localite>AYGUESVIVES</localite>
            <codePays>FR</codePays>
            <coordGeolocalisationLatitude>43.4391666667</coordGeolocalisationLatitude>
            <coordGeolocalisationLongitude>1.598055555560</coordGeolocalisationLongitude>
            <typeDePoint>P</typeDePoint>
            <actif>true</actif>
        </listePointRelais>
    </root>
    """

    client = DummyChronopostClient(
        xml_response
    )

    provider = ChronopostLiveProvider(
        client
    )

    result = provider.search_pickup_points(
        carrier_id="chronopost",
        country_code="FR",
        postal_code="31450",
        city="AYGUESVIVES",
    )

    assert len(result) == 1

    assert (
        result[0].carrier_id
        == "chronopost"
    )

    assert (
        result[0].carrier_pickup_id
        == "1487R"
    )

    assert (
        client.calls[0]["zip_code"]
        == "31450"
    )


def test_chronopost_live_provider_returns_empty_for_other_carrier() -> None:
    client = DummyChronopostClient(
        "<root></root>"
    )

    provider = ChronopostLiveProvider(
        client
    )

    result = provider.search_pickup_points(
        carrier_id="colissimo",
        country_code="FR",
        postal_code="31450",
        city="AYGUESVIVES",
    )

    assert result == []
    assert client.calls == []


def test_chronopost_live_provider_returns_empty_without_postal_code() -> None:
    client = DummyChronopostClient(
        "<root></root>"
    )

    provider = ChronopostLiveProvider(
        client
    )

    result = provider.search_pickup_points(
        carrier_id="chronopost",
        country_code="FR",
        postal_code=None,
        city="AYGUESVIVES",
    )

    assert result == []
    assert client.calls == []