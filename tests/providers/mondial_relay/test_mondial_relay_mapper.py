from universal_pudo.providers.mondial_relay.mapper import (
    MondialRelayMapper,
)


def test_to_pickup_point_maps_payload():
    payload = {
        "Num": "001001",
        "LgAdr1": "MONDIAL RELAY ISSY",
        "LgAdr2": "",
        "LgAdr3": "12 RUE DU GENERAL LECLERC",
        "LgAdr4": "",
        "CP": "92130",
        "Ville": "ISSY LES MOULINEAUX",
        "Pays": "FR",
        "Latitude": "48.823000",
        "Longitude": "2.273000",
        "TypeActivite": "RELAY",
        "Horaire_Lundi": ["09:00", "19:00"],
    }

    result = MondialRelayMapper.to_pickup_point(
        payload
    )

    assert result.id == "mondial-relay-001001"
    assert result.carrier_id == "mondial-relay"
    assert result.carrier_pickup_id == "001001"
    assert result.name == "MONDIAL RELAY ISSY"
    assert result.pickup_type == "RELAY"

    assert (
        result.street_line_1
        == "12 RUE DU GENERAL LECLERC"
    )

    assert result.street_line_2 is None

    assert result.postal_code == "92130"

    assert (
        result.city
        == "ISSY LES MOULINEAUX"
    )

    assert result.country_code == "FR"

    assert result.latitude == 48.823000
    assert result.longitude == 2.273000

    assert result.active is True


def test_to_pickup_point_converts_coordinates():
    payload = {
        "Num": "001002",
        "LgAdr1": "TEST",
        "LgAdr2": "",
        "LgAdr3": "ADDRESS",
        "LgAdr4": "",
        "CP": "75001",
        "Ville": "PARIS",
        "Pays": "FR",
        "Latitude": "48.8566",
        "Longitude": "2.3522",
        "TypeActivite": "RELAY",
        "Horaire_Lundi": [],
    }

    result = MondialRelayMapper.to_pickup_point(
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


def test_to_pickup_point_keeps_address_line_2():
    payload = {
        "Num": "001003",
        "LgAdr1": "TEST",
        "LgAdr2": "",
        "LgAdr3": "ADDRESS",
        "LgAdr4": "BATIMENT A",
        "CP": "75001",
        "Ville": "PARIS",
        "Pays": "FR",
        "Latitude": "48.8566",
        "Longitude": "2.3522",
        "TypeActivite": "RELAY",
        "Horaire_Lundi": [],
    }

    result = MondialRelayMapper.to_pickup_point(
        payload
    )

    assert (
        result.street_line_2
        == "BATIMENT A"
    )