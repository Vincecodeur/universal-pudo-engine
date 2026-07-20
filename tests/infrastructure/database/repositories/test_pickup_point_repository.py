from datetime import datetime
from datetime import timezone

from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)
from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)
from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)


def create_carrier(
    session: Session,
    carrier_id: str,
    code: str,
) -> None:
    carrier = CarrierModel(
        id=carrier_id,
        code=code,
        name=code,
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(
        carrier
    )
    session.flush()


def create_pickup_point(
    pickup_id: str,
    carrier_id: str,
    carrier_pickup_id: str,
    name: str = "Test Pickup Point",
    pickup_type: str = "STORE",
    postal_code: str = "75001",
    city: str = "Paris",
    active: bool = True,
    last_synced_at: datetime | None = None,
) -> PickupPointModel:
    return PickupPointModel(
        id=pickup_id,
        carrier_id=carrier_id,
        carrier_pickup_id=carrier_pickup_id,
        name=name,
        pickup_type=pickup_type,
        street_line_1="1 Test Street",
        street_line_2=None,
        postal_code=postal_code,
        city=city,
        state_or_region=None,
        country_code="FR",
        latitude=48.8566,
        longitude=2.3522,
        opening_hours=None,
        active=active,
        last_synced_at=last_synced_at,
    )


def test_repository_creation(
    session: Session,
) -> None:
    repository = PickupPointRepository(
        session
    )

    assert repository.session is session


def test_save_and_get_pickup_point_by_id(
    session: Session,
) -> None:
    create_carrier(
        session,
        "pickup-point-test-carrier-001",
        "pickup_point_test_carrier_001",
    )

    repository = PickupPointRepository(
        session
    )

    pickup_point = create_pickup_point(
        pickup_id="pickup-point-test-001",
        carrier_id="pickup-point-test-carrier-001",
        carrier_pickup_id="CARRIER-PUDO-001",
        name="Test Pickup Point 001",
    )

    repository.save(
        pickup_point
    )
    session.flush()

    result = repository.get_by_id(
        "pickup-point-test-001"
    )

    assert result is not None
    assert result.id == "pickup-point-test-001"
    assert result.carrier_pickup_id == "CARRIER-PUDO-001"
    assert result.pickup_type == "STORE"


def test_list_pickup_points_by_carrier(
    session: Session,
) -> None:
    create_carrier(
        session,
        "pickup-point-test-carrier-002",
        "pickup_point_test_carrier_002",
    )

    repository = PickupPointRepository(
        session
    )

    pickup_point_a = create_pickup_point(
        pickup_id="pickup-point-test-002",
        carrier_id="pickup-point-test-carrier-002",
        carrier_pickup_id="CARRIER-PUDO-002",
        name="Pickup Point A",
    )

    pickup_point_b = create_pickup_point(
        pickup_id="pickup-point-test-003",
        carrier_id="pickup-point-test-carrier-002",
        carrier_pickup_id="CARRIER-PUDO-003",
        name="Pickup Point B",
        pickup_type="LOCKER",
        postal_code="75002",
    )

    repository.save(
        pickup_point_a
    )
    repository.save(
        pickup_point_b
    )
    session.flush()

    results = repository.list_by_carrier(
        "pickup-point-test-carrier-002"
    )

    names = [
        pickup_point.name
        for pickup_point in results
    ]

    assert "Pickup Point A" in names
    assert "Pickup Point B" in names


def test_delete_pickup_point(
    session: Session,
) -> None:
    create_carrier(
        session,
        "pickup-point-test-carrier-003",
        "pickup_point_test_carrier_003",
    )

    repository = PickupPointRepository(
        session
    )

    pickup_point = create_pickup_point(
        pickup_id="pickup-point-test-004",
        carrier_id="pickup-point-test-carrier-003",
        carrier_pickup_id="CARRIER-PUDO-004",
        name="Pickup Point To Delete",
    )

    repository.save(
        pickup_point
    )
    session.flush()

    repository.delete(
        pickup_point
    )
    session.flush()

    result = repository.get_by_id(
        "pickup-point-test-004"
    )

    assert result is None


def test_search_pickup_points_by_filters(
    session: Session,
) -> None:
    create_carrier(
        session,
        "pickup-point-search-carrier-001",
        "pickup_point_search_carrier_001",
    )

    repository = PickupPointRepository(
        session
    )

    pickup_point = create_pickup_point(
        pickup_id="pickup-point-search-001",
        carrier_id="pickup-point-search-carrier-001",
        carrier_pickup_id="SEARCH-PUDO-001",
        name="Search Pickup Point",
        pickup_type="LOCKER",
        postal_code="75009",
        city="Paris",
    )

    repository.save(
        pickup_point
    )
    session.flush()

    results = repository.search(
        carrier_id="pickup-point-search-carrier-001",
        country_code="FR",
        postal_code="75009",
        city="Paris",
        pickup_type="LOCKER",
        active=True,
    )

    assert len(results) == 1
    assert results[0].id == "pickup-point-search-001"


def test_find_by_carrier_pickup_id(
    session: Session,
) -> None:
    create_carrier(
        session,
        "carrier-find-001",
        "carrier_find_001",
    )

    repository = PickupPointRepository(
        session
    )

    pickup_point = create_pickup_point(
        pickup_id="pickup-find-001",
        carrier_id="carrier-find-001",
        carrier_pickup_id="FIND-001",
        name="Find Pickup Point",
    )

    repository.save(
        pickup_point
    )
    session.flush()

    result = repository.find_by_carrier_pickup_id(
        "carrier-find-001",
        "FIND-001",
    )

    assert result is not None
    assert result.id == "pickup-find-001"


def test_upsert_updates_existing_pickup_point(
    session: Session,
) -> None:
    create_carrier(
        session,
        "carrier-upsert-001",
        "carrier_upsert_001",
    )

    repository = PickupPointRepository(
        session
    )

    original = create_pickup_point(
        pickup_id="pickup-upsert-original",
        carrier_id="carrier-upsert-001",
        carrier_pickup_id="UPSERT-001",
        name="Original Name",
    )

    repository.save(
        original
    )
    session.flush()

    updated = create_pickup_point(
        pickup_id="pickup-upsert-new",
        carrier_id="carrier-upsert-001",
        carrier_pickup_id="UPSERT-001",
        name="Updated Name",
        pickup_type="LOCKER",
        postal_code="75009",
    )

    repository.upsert(
        updated
    )
    session.flush()

    result = repository.find_by_carrier_pickup_id(
        "carrier-upsert-001",
        "UPSERT-001",
    )

    assert result is not None
    assert result.name == "Updated Name"
    assert result.pickup_type == "LOCKER"
    assert result.postal_code == "75009"

    count = (
        session.query(
            PickupPointModel
        )
        .filter(
            PickupPointModel.carrier_id
            == "carrier-upsert-001",
            PickupPointModel.carrier_pickup_id
            == "UPSERT-001",
        )
        .count()
    )

    assert count == 1


def test_find_stale_pickup_points(
    session: Session,
) -> None:
    create_carrier(
        session,
        "carrier-stale-001",
        "carrier_stale_001",
    )

    repository = PickupPointRepository(
        session
    )

    stale_date = datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )

    recent_date = datetime(
        2026,
        7,
        1,
        tzinfo=timezone.utc,
    )

    cutoff_date = datetime(
        2026,
        6,
        1,
        tzinfo=timezone.utc,
    )

    stale_pickup_point = create_pickup_point(
        pickup_id="pickup-stale-001",
        carrier_id="carrier-stale-001",
        carrier_pickup_id="STALE-001",
        name="Stale Pickup Point",
        last_synced_at=stale_date,
    )

    recent_pickup_point = create_pickup_point(
        pickup_id="pickup-recent-001",
        carrier_id="carrier-stale-001",
        carrier_pickup_id="RECENT-001",
        name="Recent Pickup Point",
        last_synced_at=recent_date,
    )

    inactive_stale_pickup_point = create_pickup_point(
        pickup_id="pickup-inactive-stale-001",
        carrier_id="carrier-stale-001",
        carrier_pickup_id="INACTIVE-STALE-001",
        name="Inactive Stale Pickup Point",
        active=False,
        last_synced_at=stale_date,
    )

    repository.save(
        stale_pickup_point
    )
    repository.save(
        recent_pickup_point
    )
    repository.save(
        inactive_stale_pickup_point
    )

    session.flush()

    results = repository.find_stale_pickup_points(
        cutoff_date
    )

    ids = [
        pickup_point.id
        for pickup_point in results
    ]

    assert ids == [
        "pickup-stale-001",
    ]