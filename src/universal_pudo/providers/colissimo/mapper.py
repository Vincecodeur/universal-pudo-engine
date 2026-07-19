from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)


class ColissimoMapper:
    @staticmethod
    def to_pickup_point(
        payload: dict,
    ) -> PickupPointModel:
        return PickupPointModel(
            id=f"colissimo-{payload['identifiant']}",
            carrier_id="colissimo",
            carrier_pickup_id=payload["identifiant"],
            name=payload["nom"],
            pickup_type=payload["typeDePoint"],
            street_line_1=payload["adresse1"],
            street_line_2=payload.get("adresse2") or None,
            postal_code=payload["codePostal"],
            city=payload["localite"],
            state_or_region=None,
            country_code=payload["codePays"],
            latitude=float(
                payload["coordGeolocalisationLatitude"]
            ),
            longitude=float(
                payload["coordGeolocalisationLongitude"]
            ),
            opening_hours=payload.get(
                "horairesOuvertureLundi"
            ),
            active=not payload.get(
                "congesTotal",
                False,
            ),
        )