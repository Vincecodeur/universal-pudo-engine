from pathlib import Path

from universal_pudo.providers.mondial_relay.response_parser import (
    MondialRelayResponseParser,
)


def test_parse_real_mondial_relay_xml_fixture():
    fixture_path = (
        Path("tests")
        / "data"
        / "mondial_relay"
        / "point_relais_recherche_response.xml"
    )

    xml_content = fixture_path.read_text(
        encoding="utf-8"
    )

    pickup_points = (
        MondialRelayResponseParser
        .extract_pickup_points(
            xml_content
        )
    )

    assert len(pickup_points) >= 1

    first = pickup_points[0]

    assert first["Num"] == "020243"
    assert first["CP"] == "92130"
    assert first["Ville"] == (
        "ISSY LES MOULINEAUX"
    )