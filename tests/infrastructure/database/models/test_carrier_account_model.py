from universal_pudo.infrastructure.database.models.carrier_account_model import (
    CarrierAccountModel,
)


def test_carrier_account_table_name() -> None:
    assert CarrierAccountModel.__tablename__ == "carrier_accounts"


def test_carrier_account_has_expected_columns() -> None:
    columns = CarrierAccountModel.__table__.columns

    assert "id" in columns
    assert "carrier_id" in columns
    assert "account_name" in columns
    assert "status" in columns