from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)
from universal_pudo.providers.base.pickup_provider import (
    PickupProvider,
)


class MockPickupProvider(PickupProvider):
    def __init__(
        self,
        session: Session,
    ) -> None:
        self.repository = PickupPointRepository(
            session
        )

    def search_pickup_points(
        self,
        *,
        carrier_id: str | None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
    ):
        return self.repository.search(
            carrier_id=carrier_id,
            country_code=country_code,
            postal_code=postal_code,
            city=city,
        )

    def get_pickup_point_details(
        self,
        pickup_point_id: str,
    ):
        return self.repository.get_by_id(
            pickup_point_id
        )