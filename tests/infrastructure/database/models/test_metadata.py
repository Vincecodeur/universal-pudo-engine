from universal_pudo.infrastructure.database.base import Base

from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)
from universal_pudo.infrastructure.database.models.carrier_account_model import (
    CarrierAccountModel,
)
from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)


def test_all_tables_registered() -> None:
    tables = Base.metadata.tables

    assert "carriers" in tables
    assert "carrier_accounts" in tables
    assert "pickup_points" in tables