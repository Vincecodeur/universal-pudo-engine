from universal_pudo.providers.mondial_relay.mondial_relay_live_provider import (
    MondialRelayLiveProvider,
)


class FakeMondialRelayClient:
    def search_pickup_points(
        self,
        country_code: str,
        postal_code: str,
        city: str = "",
    ) -> str:
        return """
        <root>
            <PointRelais_Details>
                <Num>020243</Num>
                <LgAdr1>LOCKER CARREFOUR CITY ISSY LES</LgAdr1>
                <LgAdr2></LgAdr2>
                <LgAdr3>14 BOULEVARD VOLTAIRE</LgAdr3>
                <LgAdr4></LgAdr4>
                <CP>92130</CP>
                <Ville>ISSY LES MOULINEAUX</Ville>
                <Pays>FR</Pays>
                <Latitude>48,82619</Latitude>
                <Longitude>2,27988</Longitude>
                <TypeActivite></TypeActivite>
                <Distance>0</Distance>
            </PointRelais_Details>
        </root>
        """


def test_search_pickup_points_returns_mapped_results():
    provider = MondialRelayLiveProvider(
        client=FakeMondialRelayClient()
    )

    results = provider.search_pickup_points(
        carrier_id="mondial-relay",
        country_code="FR",
        postal_code="92130",
        city="ISSY LES MOULINEAUX",
    )

    assert len(results) == 1

    result = results[0]

    assert result.carrier_id == "mondial-relay"
    assert result.carrier_pickup_id == "020243"
    assert result.name == "LOCKER CARREFOUR CITY ISSY LES"
    assert result.street_line_1 == "14 BOULEVARD VOLTAIRE"
    assert result.postal_code == "92130"
    assert result.city == "ISSY LES MOULINEAUX"
    assert result.country_code == "FR"
    assert result.latitude == 48.82619
    assert result.longitude == 2.27988


def test_search_pickup_points_returns_empty_for_other_carrier():
    provider = MondialRelayLiveProvider(
        client=FakeMondialRelayClient()
    )

    results = provider.search_pickup_points(
        carrier_id="colissimo",
        country_code="FR",
        postal_code="92130",
        city="ISSY LES MOULINEAUX",
    )

    assert results == []


def test_search_pickup_points_returns_empty_without_country_code():
    provider = MondialRelayLiveProvider(
        client=FakeMondialRelayClient()
    )

    results = provider.search_pickup_points(
        carrier_id="mondial-relay",
        postal_code="92130",
        city="ISSY LES MOULINEAUX",
    )

    assert results == []


def test_search_pickup_points_returns_empty_without_postal_code():
    provider = MondialRelayLiveProvider(
        client=FakeMondialRelayClient()
    )

    results = provider.search_pickup_points(
        carrier_id="mondial-relay",
        country_code="FR",
        city="ISSY LES MOULINEAUX",
    )

    assert results == []


def test_get_pickup_point_details_returns_none_for_now():
    provider = MondialRelayLiveProvider(
        client=FakeMondialRelayClient()
    )

    result = provider.get_pickup_point_details(
        "mondial-relay-020243"
    )

    assert result is None