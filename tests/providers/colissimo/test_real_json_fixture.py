import json

from pathlib import Path

from universal_pudo.providers.colissimo.mapper import (
    ColissimoMapper,
)


def test_map_real_colissimo_fixture():
    fixture_path = (
        Path("tests")
        / "data"
        / "colissimo"
        / "findRDVPointRetraitAcheminement_live_response.json"
    )

    payload = json.loads(
        fixture_path.read_text(
            encoding="utf-8"
        )
    )

    pickup_points = (
        payload[
            "listePointRetraitAcheminement"
        ]
    )

    result = (
        ColissimoMapper.to_pickup_point(
            pickup_points[0]
        )
    )

    assert result.carrier_id == "colissimo"

    assert (
        result.carrier_pickup_id
        == pickup_points[0]["identifiant"]
    )

    assert (
        result.postal_code
        == pickup_points[0]["codePostal"]
    )

    assert (
        result.city
        == pickup_points[0]["localite"]
    )