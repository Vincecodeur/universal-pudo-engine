from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)


class PickupPointRepository:
    """
    Repository for PickupPointModel operations.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        pickup_id: str,
    ) -> PickupPointModel | None:
        return self.session.get(
            PickupPointModel,
            pickup_id,
        )

    def list_by_carrier(
        self,
        carrier_id: str,
    ) -> list[PickupPointModel]:
        return (
            self.session.query(PickupPointModel)
            .filter(
                PickupPointModel.carrier_id == carrier_id
            )
            .all()
        )

    def save(
        self,
        pickup_point: PickupPointModel,
    ) -> None:
        self.session.add(pickup_point)

    def delete(
        self,
        pickup_point: PickupPointModel,
    ) -> None:
        self.session.delete(pickup_point)