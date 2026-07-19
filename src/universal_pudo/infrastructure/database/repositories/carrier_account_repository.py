from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.models.carrier_account_model import (
    CarrierAccountModel,
)


class CarrierAccountRepository:
    """
    Repository for CarrierAccountModel operations.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(
        self,
        account_id: str,
    ) -> CarrierAccountModel | None:
        return self.session.get(
            CarrierAccountModel,
            account_id,
        )

    def list_by_carrier(
        self,
        carrier_id: str,
    ) -> list[CarrierAccountModel]:
        return (
            self.session.query(CarrierAccountModel)
            .filter(
                CarrierAccountModel.carrier_id == carrier_id
            )
            .all()
        )

    def save(
        self,
        account: CarrierAccountModel,
    ) -> None:
        self.session.add(account)

    def delete(
        self,
        account: CarrierAccountModel,
    ) -> None:
        self.session.delete(account)