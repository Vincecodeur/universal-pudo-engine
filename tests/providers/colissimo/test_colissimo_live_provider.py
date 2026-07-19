from universal_pudo.providers.colissimo.colissimo_live_provider import (
    ColissimoLiveProvider,
)


class FakeColissimoClient:
    def search_pickup_points(
        self,
        *,
        address: str,
        zip_code: str,
        city: str,
        shipping_date: str,
        country_code: str = "FR",
    ) -> dict:
        return {
            "errorCode": 0,
            "listePointRetraitAcheminement": [
                {
                    "identifiant": "923560",
                    "nom": (
                        "BUREAU DE POSTE "
                        "ISSY FORUM SEINE BP"
                    ),
                    "adresse1": (
                        "60 RUE CAMILLE "
                        "DESMOULINS"
                    ),
                    "adresse2": "",
                    "codePostal": "92130",
                    "localite": (
                        "ISSY LES MOULINEAUX"
                    ),
                    "coordGeolocalisationLatitude":
                        "48.830093",
                    "coordGeolocalisationLongitude":
                        "2.265194",
                    "typeDePoint": "BPR",
                    "codePays": "FR",
                    "horairesOuvertureLundi":
                        "10:00-18:00",
                }
            ],
        }


def test_search_pickup_points_returns_results():
    provider = ColissimoLiveProvider(
        client=FakeColissimoClient()
    )

    results = provider.search_pickup_points(
        carrier_id="colissimo",
        country_code="FR",
        postal_code="92130",
        city="ISSY LES MOULINEAUX",
    )

    assert len(results) == 1

    result = results[0]

    assert result.carrier_id == "colissimo"
    assert result.carrier_pickup_id == "923560"
    assert result.postal_code == "92130"


def test_returns_empty_for_other_carrier():
    provider = ColissimoLiveProvider(
        client=FakeColissimoClient()
    )

    results = provider.search_pickup_points(
        carrier_id="mondial-relay",
        country_code="FR",
        postal_code="92130",
        city="ISSY LES MOULINEAUX",
    )

    assert results == []


def test_returns_empty_without_postal_code():
    provider = ColissimoLiveProvider(
        client=FakeColissimoClient()
    )

    results = provider.search_pickup_points(
        carrier_id="colissimo",
        country_code="FR",
        city="ISSY LES MOULINEAUX",
    )

    assert results == []


def test_returns_empty_without_city():
    provider = ColissimoLiveProvider(
        client=FakeColissimoClient()
    )

    results = provider.search_pickup_points(
        carrier_id="colissimo",
        country_code="FR",
        postal_code="92130",
    )

    assert results == []


def test_get_pickup_point_details_returns_none():
    provider = ColissimoLiveProvider(
        client=FakeColissimoClient()
    )

    result = provider.get_pickup_point_details(
        "colissimo-923560"
    )

    assert result is None