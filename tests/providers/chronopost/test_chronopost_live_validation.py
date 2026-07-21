from pathlib import Path

from universal_pudo.providers.chronopost.response_parser import (
    ChronopostResponseParser,
)

from universal_pudo.providers.chronopost.mapper import (
    ChronopostMapper,
)


def test_chronopost_live_fixture_can_be_mapped() -> None:

    fixture_path = Path(
        "tests/fixtures/chronopost/"
        "recherchePointChronopostInter_live_response.xml"
    )

    xml_content = fixture_path.read_text(
        encoding="utf-8",
    )

    payloads = (
        ChronopostResponseParser.extract_pickup_points(
            xml_content
        )
    )

    assert len(payloads) > 0

    pickup_point = (
        ChronopostMapper.to_pickup_point(
            payloads[0]
        )
    )

    assert pickup_point.carrier_id == "chronopost"
    assert pickup_point.carrier_pickup_id
    assert pickup_point.name
    assert pickup_point.postal_code
    assert pickup_point.city
    assert pickup_point.country_code

    assert isinstance(
        pickup_point.latitude,
        float,
    )

    assert isinstance(
        pickup_point.longitude,
        float,
    )