from pathlib import Path

from universal_pudo.providers.chronopost.response_parser import (
    ChronopostResponseParser,
)


def test_real_chronopost_xml_fixture() -> None:
    fixture_path = Path(
        "tests/fixtures/chronopost/pudo_search_response.xml"
    )

    xml_content = fixture_path.read_text(
        encoding="utf-8",
    )

    result = (
        ChronopostResponseParser
        .extract_pickup_points(
            xml_content
        )
    )

    assert len(result) == 1

    pickup_point = result[0]

    assert (
        pickup_point["identifiant"]
        == "1487R"
    )

    assert (
        pickup_point["nom"]
        == "LE BISTROT DU COIN"
    )

    assert (
        pickup_point["adresse1"]
        == "29 ROUTE DE TICAILLE"
    )

    assert (
        pickup_point["codePostal"]
        == "31450"
    )

    assert (
        pickup_point["localite"]
        == "AYGUESVIVES"
    )

    assert (
        pickup_point["codePays"]
        == "FR"
    )

    assert (
        pickup_point["typeDePoint"]
        == "P"
    )

    assert (
        pickup_point["actif"]
        == "true"
    )

    assert (
        pickup_point[
            "coordGeolocalisationLatitude"
        ]
        == "43.4391666667"
    )

    assert (
        pickup_point[
            "coordGeolocalisationLongitude"
        ]
        == "1.598055555560"
    )

    assert (
        pickup_point["opening_hours"]
        == "08:00-13:00 15:00-20:00"
    )