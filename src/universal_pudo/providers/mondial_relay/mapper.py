from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)


class MondialRelayMapper:
    @staticmethod
    def to_pickup_point(
        payload: dict,
    ) -> PickupPointModel:
        return PickupPointModel(
            id=f"mondial-relay-{payload['Num']}",
            carrier_id="mondial-relay",
            carrier_pickup_id=payload["Num"],
            name=payload["LgAdr1"],
            pickup_type=payload.get(
                "TypeActivite",
                "RELAY",
            ),
            street_line_1=payload["LgAdr3"],
            street_line_2=payload.get(
                "LgAdr4"
            ) or None,
            postal_code=payload["CP"],
            city=payload["Ville"],
            state_or_region=None,
            country_code=payload["Pays"],
            latitude=float(
                payload["Latitude"]
            ),
            longitude=float(
                payload["Longitude"]
            ),
            opening_hours=str(
                payload.get(
                    "Horaire_Lundi",
                    "",
                )
            ),
            active=True,
        )