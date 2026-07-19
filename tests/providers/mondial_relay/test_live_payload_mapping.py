import json

from pathlib import Path

from universal_pudo.providers.mondial_relay.mapper import (
    MondialRelayMapper,
)


def test_maps_real_parsed_mondial_relay_payload():
    fixture_path = (
        Path("tests")
        / "data"
        / "mondial_relay"
        / "point_relais_recherche_parsed_response.json"
    )

    payload = json.loads(
        fixture_path.read_text(
            encoding="utf-8"
        )
    )

    pickup_points = payload["pickup_points"]

    result = MondialRelayMapper.to_pickup_point(
        pickup_points[0]
    )

    assert result.id == "mondial-relay-020243"
    assert result.carrier_id == "mondial-relay"
    assert result.carrier_pickup_id == "020243"
    assert result.name == "LOCKER CARREFOUR CITY ISSY LES"
    assert result.street_line_1 == "14 BOULEVARD VOLTAIRE"
    assert result.street_line_2 is None
    assert result.postal_code == "92130"
    assert result.city == "ISSY LES MOULINEAUX"
    assert result.country_code == "FR"
    assert result.latitude == 48.82619
    assert result.longitude == 2.27988
    assert result.active is True