from universal_pudo.providers.chronopost.mapper import (
    ChronopostMapper,
)


def test_maps_chronopost_payload_to_pickup_point() -> None:
    payload = {
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

    result = ChronopostMapper.to_pickup_point(
        payload
    )

    assert result.id == "chronopost-1487R"
    assert result.carrier_id == "chronopost"
    assert result.carrier_pickup_id == "1487R"
    assert result.name == "LE BISTROT DU COIN"
    assert result.pickup_type == "STORE"
    assert result.street_line_1 == "29 ROUTE DE TICAILLE"
    assert result.street_line_2 is None
    assert result.postal_code == "31450"
    assert result.city == "AYGUESVIVES"
    assert result.country_code == "FR"
    assert result.latitude == 43.4391666667
    assert result.longitude == 1.598055555560
    assert (
        result.opening_hours
        == "08:00-13:00 15:00-20:00"
    )
    assert result.active is True