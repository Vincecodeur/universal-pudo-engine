from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)
from universal_pudo.providers.base.pickup_provider import (
    PickupProvider,
)


class MondialRelayPickupProvider(PickupProvider):
    def __init__(self) -> None:
        self._pickup_points = [
            PickupPointModel(
                id="mondial-relay-001001",
                carrier_id="mondial-relay",
                carrier_pickup_id="001001",
                name="MONDIAL RELAY ISSY",
                pickup_type="RELAY",
                street_line_1="12 RUE DU GENERAL LECLERC",
                street_line_2=None,
                postal_code="92130",
                city="ISSY LES MOULINEAUX",
                state_or_region=None,
                country_code="FR",
                latitude=48.823000,
                longitude=2.273000,
                opening_hours="09:00-19:00",
                active=True,
            ),
            PickupPointModel(
                id="mondial-relay-001002",
                carrier_id="mondial-relay",
                carrier_pickup_id="001002",
                name="MONDIAL RELAY PARIS",
                pickup_type="RELAY",
                street_line_1="25 RUE DE RIVOLI",
                street_line_2=None,
                postal_code="75001",
                city="PARIS",
                state_or_region=None,
                country_code="FR",
                latitude=48.856600,
                longitude=2.352200,
                opening_hours="08:30-20:00",
                active=True,
            ),
            PickupPointModel(
                id="mondial-relay-001003",
                carrier_id="mondial-relay",
                carrier_pickup_id="001003",
                name="MONDIAL RELAY BOULOGNE",
                pickup_type="RELAY",
                street_line_1="8 AVENUE JEAN JAURES",
                street_line_2=None,
                postal_code="92100",
                city="BOULOGNE BILLANCOURT",
                state_or_region=None,
                country_code="FR",
                latitude=48.842000,
                longitude=2.239000,
                opening_hours="10:00-18:00",
                active=True,
            ),
        ]

    def search_pickup_points(
        self,
        *,
        carrier_id: str | None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
    ):
        results = self._pickup_points

        if carrier_id is not None:
            results = [
                point
                for point in results
                if point.carrier_id == carrier_id
            ]

        if country_code is not None:
            results = [
                point
                for point in results
                if point.country_code == country_code
            ]

        if postal_code is not None:
            results = [
                point
                for point in results
                if point.postal_code == postal_code
            ]

        if city is not None:
            results = [
                point
                for point in results
                if point.city.lower() == city.lower()
            ]

        return results

    def get_pickup_point_details(
        self,
        pickup_point_id: str,
    ):
        for pickup_point in self._pickup_points:
            if pickup_point.id == pickup_point_id:
                return pickup_point

        return None