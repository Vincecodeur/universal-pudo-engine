from math import atan2
from math import cos
from math import radians
from math import sin
from math import sqrt

from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)


class PickupPointRepository:
    """
    Repository for PickupPointModel operations.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        pickup_id: str,
    ) -> PickupPointModel | None:
        return self.session.get(
            PickupPointModel,
            pickup_id,
        )

    def find_by_carrier_pickup_id(
        self,
        carrier_id: str,
        carrier_pickup_id: str,
    ) -> PickupPointModel | None:
        return (
            self.session.query(
                PickupPointModel
            )
            .filter(
                PickupPointModel.carrier_id
                == carrier_id,
                PickupPointModel.carrier_pickup_id
                == carrier_pickup_id,
            )
            .first()
        )

    def list_by_carrier(
        self,
        carrier_id: str,
    ) -> list[PickupPointModel]:
        return (
            self.session.query(
                PickupPointModel
            )
            .filter(
                PickupPointModel.carrier_id
                == carrier_id
            )
            .all()
        )

    def search(
        self,
        carrier_id: str | None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
        active: bool | None = None,
    ) -> list[PickupPointModel]:
        query = self.session.query(
            PickupPointModel
        )

        if carrier_id is not None:
            query = query.filter(
                PickupPointModel.carrier_id
                == carrier_id
            )

        if country_code is not None:
            query = query.filter(
                PickupPointModel.country_code
                == country_code
            )

        if postal_code is not None:
            query = query.filter(
                PickupPointModel.postal_code
                == postal_code
            )

        if city is not None:
            query = query.filter(
                PickupPointModel.city.ilike(
                    city
                )
            )

        if pickup_type is not None:
            query = query.filter(
                PickupPointModel.pickup_type
                == pickup_type
            )

        if active is not None:
            query = query.filter(
                PickupPointModel.active
                == active
            )

        return query.all()

    def search_by_radius(
        self,
        latitude: float,
        longitude: float,
        radius_km: float,
    ) -> list[PickupPointModel]:
        pickup_points = (
            self.session.query(
                PickupPointModel
            )
            .filter(
                PickupPointModel.active.is_(True)
            )
            .all()
        )

        results: list[
            PickupPointModel
        ] = []

        for pickup_point in pickup_points:
            distance = self._distance_km(
                latitude,
                longitude,
                pickup_point.latitude,
                pickup_point.longitude,
            )

            if distance <= radius_km:
                results.append(
                    pickup_point
                )

        return results

    def save(
        self,
        pickup_point: PickupPointModel,
    ) -> None:
        self.session.add(
            pickup_point
        )

    def upsert(
        self,
        pickup_point: PickupPointModel,
    ) -> None:
        existing = (
            self.find_by_carrier_pickup_id(
                carrier_id=pickup_point.carrier_id,
                carrier_pickup_id=pickup_point.carrier_pickup_id,
            )
        )

        if existing is None:
            self.save(
                pickup_point
            )
            return

        existing.name = (
            pickup_point.name
        )
        existing.pickup_type = (
            pickup_point.pickup_type
        )
        existing.street_line_1 = (
            pickup_point.street_line_1
        )
        existing.street_line_2 = (
            pickup_point.street_line_2
        )
        existing.postal_code = (
            pickup_point.postal_code
        )
        existing.city = (
            pickup_point.city
        )
        existing.state_or_region = (
            pickup_point.state_or_region
        )
        existing.country_code = (
            pickup_point.country_code
        )
        existing.latitude = (
            pickup_point.latitude
        )
        existing.longitude = (
            pickup_point.longitude
        )
        existing.opening_hours = (
            pickup_point.opening_hours
        )
        existing.active = (
            pickup_point.active
        )

        
        if (
            hasattr(
                pickup_point,
                "last_synced_at",
            )
            and pickup_point.last_synced_at
            is not None
        ):
            existing.last_synced_at = (
                pickup_point.last_synced_at
            )


    def delete(
        self,
        pickup_point: PickupPointModel,
    ) -> None:
        self.session.delete(
            pickup_point
        )

    def _distance_km(
        self,
        latitude_a: float,
        longitude_a: float,
        latitude_b: float,
        longitude_b: float,
    ) -> float:
        earth_radius_km = 6371.0

        delta_latitude = radians(
            latitude_b - latitude_a
        )

        delta_longitude = radians(
            longitude_b - longitude_a
        )

        haversine_value = (
            sin(delta_latitude / 2) ** 2
            + cos(
                radians(latitude_a)
            )
            * cos(
                radians(latitude_b)
            )
            * sin(
                delta_longitude / 2
            )
            ** 2
        )

        angular_distance = (
            2
            * atan2(
                sqrt(haversine_value),
                sqrt(
                    1
                    - haversine_value
                ),
            )
        )

        return (
            earth_radius_km
            * angular_distance
        )