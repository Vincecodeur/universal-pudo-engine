import requests

from xml.sax.saxutils import escape

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
        nombre_resultats: int = 10,
    ) -> str:
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
      <Enseigne>{escape(self.enseigne)}</Enseigne>
      <Pays>{escape(country_code)}</Pays>
      <NumPointRelais>{escape(num_point_relais)}</NumPointRelais>
      <Ville>{escape(city)}</Ville>
      <CP>{escape(postal_code)}</CP>
      <Latitude>{escape(latitude)}</Latitude>
      <Longitude>{escape(longitude)}</Longitude>
      <Taille>{escape(taille)}</Taille>
      <Poids>{escape(poids)}</Poids>
      <Action>{escape(action)}</Action>
      <DelaiEnvoi>{escape(delai_envoi)}</DelaiEnvoi>
      <RayonRecherche>{escape(rayon_recherche)}</RayonRecherche>
      <TypeActivite>{escape(type_activite)}</TypeActivite>
      <NACE>{escape(nace)}</NACE>
      <NombreResultats>{nombre_resultats}</NombreResultats>
      <Security>{escape(security)}</Security>
    </WSI4_PointRelais_Recherche>
  </soap:Body>
</soap:Envelope>
"""

    def search_pickup_points(
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
        security = self.generate_search_security(
            country_code=country_code,
            postal_code=postal_code,
            city=city,
            num_point_relais=num_point_relais,
            latitude=latitude,
            longitude=longitude,
            taille=taille,
            poids=poids,
            action=action,
            delai_envoi=delai_envoi,
            rayon_recherche=rayon_recherche,
            type_activite=type_activite,
            nombre_resultats=nombre_resultats,
        )

        envelope = self.build_search_envelope(
            security=security,
            country_code=country_code,
            postal_code=postal_code,
            city=city,
            num_point_relais=num_point_relais,
            latitude=latitude,
            longitude=longitude,
            taille=taille,
            poids=poids,
            action=action,
            delai_envoi=delai_envoi,
            rayon_recherche=rayon_recherche,
            type_activite=type_activite,
            nace=nace,
            nombre_resultats=nombre_resultats,
        )

        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": f'"{self.SOAP_ACTION}"',
        }

        response = requests.post(
            self.ENDPOINT,
            data=envelope.encode("utf-8"),
            headers=headers,
            timeout=30,
        )

        response.raise_for_status()

        return response.text