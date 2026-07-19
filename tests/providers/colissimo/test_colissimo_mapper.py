from universal_pudo.providers.colissimo.mapper import (
    ColissimoMapper,
)


def test_to_pickup_point_maps_payload():
    payload = {
        "identifiant": "923560",
        "nom": "BUREAU DE POSTE",
        "typeDePoint": "BPR",
        "adresse1": "60 RUE CAMILLE DESMOULINS",
        "adresse2": "",
        "codePostal": "92130",
        "localite": "ISSY LES MOULINEAUX",
        "codePays": "FR",
        "coordGeolocalisationLatitude": "48.830093",
        "coordGeolocalisationLongitude": "2.265194",
        "horairesOuvertureLundi": "10:00-18:00",
        "congesTotal": False,
    }

    result = ColissimoMapper.to_pickup_point(
        payload
    )

    assert result.id == "colissimo-923560"
    assert result.carrier_id == "colissimo"
    assert result.carrier_pickup_id == "923560"
    assert result.name == "BUREAU DE POSTE"
    assert result.pickup_type == "BPR"
    assert (
        result.street_line_1
        == "60 RUE CAMILLE DESMOULINS"
    )
    assert result.street_line_2 is None
    assert result.postal_code == "92130"
    assert result.city == "ISSY LES MOULINEAUX"
    assert result.country_code == "FR"
    assert result.latitude == 48.830093
    assert result.longitude == 2.265194
    assert result.opening_hours == "10:00-18:00"
    assert result.active is True


def test_to_pickup_point_converts_coordinates():
    payload = {
        "identifiant": "1",
        "nom": "TEST",
        "typeDePoint": "A2P",
        "adresse1": "ADDRESS",
        "adresse2": "",
        "codePostal": "00000",
        "localite": "CITY",
        "codePays": "FR",
        "coordGeolocalisationLatitude": "48.5",
        "coordGeolocalisationLongitude": "2.1",
        "horairesOuvertureLundi": "",
        "congesTotal": False,
    }

    result = ColissimoMapper.to_pickup_point(
        payload
    )

    assert isinstance(
        result.latitude,
        float,
    )

    assert isinstance(
        result.longitude,
        float,
    )


def test_to_pickup_point_sets_inactive_when_closed():
    payload = {
        "identifiant": "2",
        "nom": "TEST",
        "typeDePoint": "A2P",
        "adresse1": "ADDRESS",
        "adresse2": "",
        "codePostal": "00000",
        "localite": "CITY",
        "codePays": "FR",
        "coordGeolocalisationLatitude": "48.5",
        "coordGeolocalisationLongitude": "2.1",
        "horairesOuvertureLundi": "",
        "congesTotal": True,
    }

    result = ColissimoMapper.to_pickup_point(
        payload
    )

    assert result.active is False


def test_to_pickup_point_keeps_address2():
    payload = {
        "identifiant": "3",
        "nom": "TEST",
        "typeDePoint": "A2P",
        "adresse1": "ADDRESS",
        "adresse2": "BATIMENT A",
        "codePostal": "00000",
        "localite": "CITY",
        "codePays": "FR",
        "coordGeolocalisationLatitude": "48.5",
        "coordGeolocalisationLongitude": "2.1",
        "horairesOuvertureLundi": "",
        "congesTotal": False,
    }

    result = ColissimoMapper.to_pickup_point(
        payload
    )

    assert (
        result.street_line_2
        == "BATIMENT A"
    )