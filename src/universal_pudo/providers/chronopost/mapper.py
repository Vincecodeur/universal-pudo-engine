from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)


class ChronopostMapper:
    @staticmethod
    def to_pickup_point(
        payload: dict,
    ) -> PickupPointModel:
        street_line_2_parts = [
            payload.get(
                "adresse2"
            ),
            payload.get(
                "adresse3"
            ),
        ]

        street_line_2 = " ".join(
            part
            for part in street_line_2_parts
            if part
        ) or None

        return PickupPointModel(
            id=f"chronopost-{payload['identifiant']}",
            carrier_id="chronopost",
            carrier_pickup_id=payload["identifiant"],
            name=payload["nom"],
            pickup_type=ChronopostMapper._map_pickup_type(
                payload.get(
                    "typeDePoint",
                    "P",
                )
            ),
            street_line_1=payload["adresse1"],
            street_line_2=street_line_2,
            postal_code=payload["codePostal"],
            city=payload["localite"],
            state_or_region=None,
            country_code=payload["codePays"],
            latitude=float(
                payload[
                    "coordGeolocalisationLatitude"
                ]
            ),
            longitude=float(
                payload[
                    "coordGeolocalisationLongitude"
                ]
            ),
            opening_hours=payload.get(
                "opening_hours"
            ),
            active=(
                str(
                    payload.get(
                        "actif",
                        "true",
                    )
                ).lower()
                == "true"
            ),
        )

    @staticmethod
    def _map_pickup_type(
        chronopost_type: str,
    ) -> str:
        if chronopost_type in {
            "P",
            "C",
        }:
            return "STORE"

        return "STORE"