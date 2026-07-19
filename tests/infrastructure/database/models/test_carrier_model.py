from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)


def test_carrier_table_name() -> None:
    assert CarrierModel.__tablename__ == "carriers"


def test_carrier_has_expected_columns() -> None:
    columns = CarrierModel.__table__.columns

    assert "id" in columns
    assert "code" in columns
    assert "name" in columns
    assert "lifecycle" in columns
    assert "supported_countries" in columns
    assert "capabilities" in columns
