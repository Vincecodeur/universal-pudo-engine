from universal_pudo.providers.chronopost.response_parser import (
    ChronopostResponseParser,
)


def test_extract_pickup_points() -> None:
    xml = """
    <root>
        <listePointRelais>
            <identifiant>1487R</identifiant>
            <nom>LE BISTROT DU COIN</nom>

            <adresse1>29 ROUTE DE TICAILLE</adresse1>
            <adresse2></adresse2>
            <adresse3></adresse3>

            <codePostal>31450</codePostal>
            <localite>AYGUESVIVES</localite>
            <codePays>FR</codePays>

            <coordGeolocalisationLatitude>
                43.4391666667
            </coordGeolocalisationLatitude>

            <coordGeolocalisationLongitude>
                1.598055555560
            </coordGeolocalisationLongitude>

            <typeDePoint>P</typeDePoint>

            <actif>true</actif>

            <listeHoraireOuverture>
                <horairesAsString>
                    08:00-13:00 15:00-20:00
                </horairesAsString>
            </listeHoraireOuverture>
        </listePointRelais>
    </root>
    """

    result = (
        ChronopostResponseParser
        .extract_pickup_points(
            xml
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
        pickup_point["opening_hours"]
        == "08:00-13:00 15:00-20:00"
    )