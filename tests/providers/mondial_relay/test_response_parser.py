from universal_pudo.providers.mondial_relay.response_parser import (
    MondialRelayResponseParser,
)


def test_extract_pickup_points():
    xml_content = """
    <root>
        <PointRelais_Details>
            <Num>001001</Num>
            <LgAdr1>MONDIAL RELAY ISSY</LgAdr1>
            <LgAdr3>12 RUE DU GENERAL LECLERC</LgAdr3>
            <CP>92130</CP>
            <Ville>ISSY LES MOULINEAUX</Ville>
            <Pays>FR</Pays>
            <Latitude>48.823</Latitude>
            <Longitude>2.273</Longitude>
            <TypeActivite>RELAY</TypeActivite>
            <Distance>100</Distance>
        </PointRelais_Details>
    </root>
    """

    results = (
        MondialRelayResponseParser
        .extract_pickup_points(
            xml_content
        )
    )

    assert len(results) == 1

    assert (
        results[0]["Num"]
        == "001001"
    )

    assert (
        results[0]["Ville"]
        == "ISSY LES MOULINEAUX"
    )