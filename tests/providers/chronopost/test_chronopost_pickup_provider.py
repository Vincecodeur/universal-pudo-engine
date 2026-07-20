from universal_pudo.providers.chronopost.chronopost_pickup_provider import (
    ChronopostPickupProvider,
)


def test_returns_chronopost_pickup_points() -> None:
    provider = ChronopostPickupProvider(
        [
            {
                "identifiant": "1487R",
                "nom": "LE BISTROT DU COIN",
                "adresse1": "29 ROUTE DE TICAILLE",
                "adresse2": "",
                "adresse3": "",
                "codePostal": "31450",
                "localite": "AYGUESVIVES",
                "codePays": "FR",
                "coordGeolocalisationLatitude": "43.4391666667",
                "coordGeolocalisationLongitude": "1.598055555560",
                "typeDePoint": "P",
                "actif": "true",
                "opening_hours": "08:00-13:00 15:00-20:00",
            }
        ]
    )

    result = provider.search_pickup_points(
        carrier_id="chronopost"
    )

    assert len(result) == 1
    assert result[0].carrier_id == "chronopost"
    assert result[0].carrier_pickup_id == "1487R"


def test_returns_empty_list_for_other_carrier() -> None:
    provider = ChronopostPickupProvider(
        [
            {
                "identifiant": "1487R",
                "nom": "LE BISTROT DU COIN",
                "adresse1": "29 ROUTE DE TICAILLE",
                "adresse2": "",
                "adresse3": "",
                "codePostal": "31450",
                "localite": "AYGUESVIVES",
                "codePays": "FR",
                "coordGeolocalisationLatitude": "43.4391666667",
                "coordGeolocalisationLongitude": "1.598055555560",
                "typeDePoint": "P",
                "actif": "true",
                "opening_hours": None,
            }
        ]
    )

    result = provider.search_pickup_points(
        carrier_id="colissimo"
    )

    assert result == []


def test_filters_by_postal_code() -> None:
    provider = ChronopostPickupProvider(
        [
            {
                "identifiant": "1487R",
                "nom": "LE BISTROT DU COIN",
                "adresse1": "29 ROUTE DE TICAILLE",
                "adresse2": "",
                "adresse3": "",
                "codePostal": "31450",
                "localite": "AYGUESVIVES",
                "codePays": "FR",
                "coordGeolocalisationLatitude": "43.4391666667",
                "coordGeolocalisationLongitude": "1.598055555560",
                "typeDePoint": "P",
                "actif": "true",
                "opening_hours": None,
            }
        ]
    )

    result = provider.search_pickup_points(
        carrier_id="chronopost",
        postal_code="31450",
    )

    assert len(result) == 1