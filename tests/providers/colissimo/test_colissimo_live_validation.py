import json
from pathlib import Path

from universal_pudo.providers.colissimo.mapper import (
    ColissimoMapper,
)


def test_colissimo_live_fixture_can_be_mapped() -> None:
    fixture_path = Path(
        "tests/data/colissimo/"
        "findRDVPointRetraitAcheminement_live_response.json"
    )

    payload = json.loads(
        fixture_path.read_text(
            encoding="utf-8",
        )
    )

    pickup_points = payload.get(
        "listePointRetraitAcheminement",
        [],
    )

    assert len(pickup_points) > 0

    pickup_point = ColissimoMapper.to_pickup_point(
        pickup_points[0]
    )

    assert pickup_point.carrier_id == "colissimo"
    assert pickup_point.carrier_pickup_id
    assert pickup_point.name
    assert pickup_point.postal_code
    assert pickup_point.city
    assert pickup_point.country_code == "FR"

    assert isinstance(
        pickup_point.latitude,
        float,
    )

    assert isinstance(
        pickup_point.longitude,
        float,
    )