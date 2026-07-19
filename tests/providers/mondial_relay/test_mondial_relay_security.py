from universal_pudo.providers.mondial_relay.security import (
    MondialRelaySecurity,
)


class MondialRelayClient:
    ENDPOINT = (
        "https://api.mondialrelay.com/"
        "Web_Services.asmx"
    )

    SOAP_ACTION = (
        "http://www.mondialrelay.fr/webservice/"
        "WSI4_PointRelais_Recherche"
    )

    def __init__(
        self,
        enseigne: str,
        private_key: str,
    ) -> None:
        self.enseigne = enseigne
        self.private_key = private_key

    def generate_search_security(
        self,
        country_code: str,
        postal_code: str,
        city: str = "",
        num_point_relais: str = "",
        latitude: str = "",
        longitude: str = "",
        taille: str = "",
        poids: str = "",
        action: str = "",
        delai_envoi: str = "",
        rayon_recherche: str = "20",
        type_activite: str = "",
        nace: str = "",
        nombre_resultats: int = 10,
    ) -> str:
        """
        SECURITY for WSI4_PointRelais_Recherche.

        According to Mondial Relay documentation:

        [Enseigne]
        [Pays]
        [NumPointRelais]
        [Ville]
        [CP]
        [Latitude]
        [Longitude]
        [Taille]
        [Poids]
        [Action]
        [DelaiEnvoi]
        [RayonRecherche]
        [TypeActivite]
        [NombreResultats]
        [CLE PRIVEE]

        NOTE:
        NACE is present in the SOAP request
        but not in the SECURITY string.
        """
        return MondialRelaySecurity.generate(
            self.enseigne,
            country_code,
            num_point_relais,
            city,
            postal_code,
            latitude,
            longitude,
            taille,
            poids,
            action,
            delai_envoi,
            rayon_recherche,
            type_activite,
            str(nombre_resultats),
            private_key=self.private_key,
        )

    def build_search_envelope(
        self,
        security: str,
        country_code: str,
        postal_code: str,
        city: str = "",
        num_point_relais: str = "",
        latitude: str = "",
        longitude: str = "",
        taille: str = "",
        poids: str = "",
        action: str = "",
        delai_envoi: str = "",
        rayon_recherche: str = "20",
        type_activite: str = "",
        nace: str = "",
        nombre_resultats: int = 10,
    ) -> str:
        return f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <WSI4_PointRelais_Recherche
        xmlns="http://www.mondialrelay.fr/webservice/">

      <Enseigne>{self.enseigne}</Enseigne>
      <Pays>{country_code}</Pays>
      <NumPointRelais>{num_point_relais}</NumPointRelais>
      <Ville>{city}</Ville>
      <CP>{postal_code}</CP>
      <Latitude>{latitude}</Latitude>
      <Longitude>{longitude}</Longitude>
      <Taille>{taille}</Taille>
      <Poids>{poids}</Poids>
      <Action>{action}</Action>
      <DelaiEnvoi>{delai_envoi}</DelaiEnvoi>
      <RayonRecherche>{rayon_recherche}</RayonRecherche>
      <TypeActivite>{type_activite}</TypeActivite>
      <NACE>{nace}</NACE>
      <NombreResultats>{nombre_resultats}</NombreResultats>
      <Security>{security}</Security>

    </WSI4_PointRelais_Recherche>
  </soap:Body>
</soap:Envelope>
"""


def test_generate_matches_official_documentation_example():
    result = MondialRelaySecurity.generate(
        "BDTEST13",
        "12345678",
        "FR",
        private_key="PrivateK",
    )

    assert (
        result
        == "33DA5F122DAA40241087CC7845BEA4B1"
    )