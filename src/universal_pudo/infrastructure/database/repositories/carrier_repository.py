from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)


class CarrierRepository:
    """
    Repository for CarrierModel operations.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        carrier_id: str,
    ) -> CarrierModel | None:
        return self.session.get(
            CarrierModel,
            carrier_id,
        )

    def get_by_code(
        self,
        code: str,
    ) -> CarrierModel | None:
        return (
            self.session.query(CarrierModel)
            .filter(CarrierModel.code == code)
            .first()
        )

    def list_all(self) -> list[CarrierModel]:
        return (
            self.session.query(CarrierModel)
            .order_by(CarrierModel.name)
            .all()
        )

    def save(
        self,
        carrier: CarrierModel,
    ) -> None:
        self.session.add(carrier)

    def delete(
        self,
        carrier: CarrierModel,
    ) -> None:
        self.session.delete(carrier)