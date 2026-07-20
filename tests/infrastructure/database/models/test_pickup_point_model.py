from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)


def test_pickup_point_table_name() -> None:
    assert PickupPointModel.__tablename__ == "pickup_points"


def test_pickup_point_has_expected_columns() -> None:
    columns = PickupPointModel.__table__.columns

    assert "id" in columns
    assert "carrier_id" in columns
    assert "carrier_pickup_id" in columns

    assert "name" in columns
    assert "pickup_type" in columns

    assert "street_line_1" in columns
    assert "street_line_2" in columns
    assert "postal_code" in columns
    assert "city" in columns
    assert "state_or_region" in columns
    assert "country_code" in columns

    assert "latitude" in columns
    assert "longitude" in columns

    assert "opening_hours" in columns
    assert "active" in columns
    assert "last_synced_at" in columns


def test_pickup_point_primary_key() -> None:
    primary_keys = [
        column.name
        for column in PickupPointModel.__table__.primary_key.columns
    ]

    assert primary_keys == ["id"]