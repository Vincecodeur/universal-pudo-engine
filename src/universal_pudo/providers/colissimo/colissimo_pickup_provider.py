from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)
from universal_pudo.providers.base.pickup_provider import (
    PickupProvider,
)


class ColissimoPickupProvider(PickupProvider):
    def __init__(self) -> None:
        self._pickup_points = [
            PickupPointModel(
                id="colissimo-paris-1",
                carrier_id="colissimo",
                carrier_pickup_id="923560",
                name="BUREAU DE POSTE PARIS",
                pickup_type="BPR",
                street_line_1="10 Rue de Rivoli",
                street_line_2=None,
                postal_code="75001",
                city="PARIS",
                state_or_region=None,
                country_code="FR",
                latitude=48.8566,
                longitude=2.3522,
                opening_hours="Mon-Fri 09:00-18:00",
                active=True,
            ),
            PickupPointModel(
                id="colissimo-paris-2",
                carrier_id="colissimo",
                carrier_pickup_id="107181",
                name="RELAIS PICKUP RIVOLI",
                pickup_type="A2P",
                street_line_1="20 Rue de Rivoli",
                street_line_2=None,
                postal_code="75001",
                city="PARIS",
                state_or_region=None,
                country_code="FR",
                latitude=48.8570,
                longitude=2.3530,
                opening_hours="Mon-Sat 08:00-20:00",
                active=True,
            ),
            PickupPointModel(
                id="colissimo-issy-1",
                carrier_id="colissimo",
                carrier_pickup_id="850010",
                name="BUREAU DE POSTE ISSY",
                pickup_type="BPR",
                street_line_1="62 Camille Desmoulins",
                street_line_2=None,
                postal_code="92130",
                city="ISSY-LES-MOULINEAUX",
                state_or_region=None,
                country_code="FR",
                latitude=48.830093,
                longitude=2.265194,
                opening_hours="Mon-Fri 09:00-18:00",
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