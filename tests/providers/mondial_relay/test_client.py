from universal_pudo.providers.mondial_relay.client import (
    MondialRelayClient,
)


def test_client_has_endpoint():
    client = MondialRelayClient(
        enseigne="TEST",
        private_key="SECRET",
    )

    assert (
        "api.mondialrelay.com"
        in client.ENDPOINT
    )


def test_client_has_soap_action():
    client = MondialRelayClient(
        enseigne="TEST",
        private_key="SECRET",
    )

    assert (
        "WSI4_PointRelais_Recherche"
        in client.SOAP_ACTION
    )


def test_build_search_envelope_contains_values():
    client = MondialRelayClient(
        enseigne="CC234C1G",
        private_key="SECRET",
    )

    envelope = client.build_search_envelope(
        security="ABC123",
        country_code="FR",
        postal_code="92130",
        city="ISSY LES MOULINEAUX",
    )

    assert "CC234C1G" in envelope
    assert "FR" in envelope
    assert "92130" in envelope
    assert "ISSY LES MOULINEAUX" in envelope
    assert "ABC123" in envelope


def test_build_search_envelope_contains_operation():
    client = MondialRelayClient(
        enseigne="TEST",
        private_key="SECRET",
    )

    envelope = client.build_search_envelope(
        security="ABC",
        country_code="FR",
        postal_code="75001",
    )

    assert (
        "WSI4_PointRelais_Recherche"
        in envelope
    )