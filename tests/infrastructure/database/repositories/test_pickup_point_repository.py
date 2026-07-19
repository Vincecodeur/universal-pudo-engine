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


def test_repository_creation(session: Session) -> None:
    repository = PickupPointRepository(session)

    assert repository.session is session


def test_save_and_get_pickup_point_by_id(session: Session) -> None:
    carrier = CarrierModel(
        id="pickup-point-test-carrier-001",
        code="pickup_point_test_carrier_001",
        name="Pickup Point Test Carrier 001",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(carrier)
    session.flush()

    repository = PickupPointRepository(session)

    pickup_point = PickupPointModel(
        id="pickup-point-test-001",
        carrier_id="pickup-point-test-carrier-001",
        carrier_pickup_id="CARRIER-PUDO-001",
        name="Test Pickup Point 001",
        pickup_type="STORE",
        street_line_1="10 Rue de Rivoli",
        street_line_2=None,
        postal_code="75001",
        city="Paris",
        state_or_region="Ile-de-France",
        country_code="FR",
        latitude=48.8566,
        longitude=2.3522,
        opening_hours="Monday to Friday",
        active=True,
    )

    repository.save(pickup_point)
    session.flush()

    result = repository.get_by_id("pickup-point-test-001")

    assert result is not None
    assert result.id == "pickup-point-test-001"
    assert result.carrier_pickup_id == "CARRIER-PUDO-001"
    assert result.pickup_type == "STORE"


def test_list_pickup_points_by_carrier(session: Session) -> None:
    carrier = CarrierModel(
        id="pickup-point-test-carrier-002",
        code="pickup_point_test_carrier_002",
        name="Pickup Point Test Carrier 002",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(carrier)
    session.flush()

    repository = PickupPointRepository(session)

    pickup_point_a = PickupPointModel(
        id="pickup-point-test-002",
        carrier_id="pickup-point-test-carrier-002",
        carrier_pickup_id="CARRIER-PUDO-002",
        name="Pickup Point A",
        pickup_type="STORE",
        street_line_1="1 Test Street",
        street_line_2=None,
        postal_code="75001",
        city="Paris",
        state_or_region=None,
        country_code="FR",
        latitude=48.8566,
        longitude=2.3522,
        opening_hours=None,
        active=True,
    )

    pickup_point_b = PickupPointModel(
        id="pickup-point-test-003",
        carrier_id="pickup-point-test-carrier-002",
        carrier_pickup_id="CARRIER-PUDO-003",
        name="Pickup Point B",
        pickup_type="LOCKER",
        street_line_1="2 Test Street",
        street_line_2=None,
        postal_code="75002",
        city="Paris",
        state_or_region=None,
        country_code="FR",
        latitude=48.8666,
        longitude=2.3622,
        opening_hours="24/7",
        active=True,
    )

    repository.save(pickup_point_a)
    repository.save(pickup_point_b)
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


def test_delete_pickup_point(session: Session) -> None:
    carrier = CarrierModel(
        id="pickup-point-test-carrier-003",
        code="pickup_point_test_carrier_003",
        name="Pickup Point Test Carrier 003",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(carrier)
    session.flush()

    repository = PickupPointRepository(session)

    pickup_point = PickupPointModel(
        id="pickup-point-test-004",
        carrier_id="pickup-point-test-carrier-003",
        carrier_pickup_id="CARRIER-PUDO-004",
        name="Pickup Point To Delete",
        pickup_type="STORE",
        street_line_1="3 Test Street",
        street_line_2=None,
        postal_code="75003",
        city="Paris",
        state_or_region=None,
        country_code="FR",
        latitude=48.8766,
        longitude=2.3722,
        opening_hours=None,
        active=True,
    )

    repository.save(pickup_point)
    session.flush()

    repository.delete(pickup_point)
    session.flush()

    result = repository.get_by_id("pickup-point-test-004")

    assert result is None

from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)
from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)
from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)


def test_repository_creation(session: Session) -> None:
    repository = PickupPointRepository(session)

    assert repository.session is session


def test_save_and_get_pickup_point_by_id(session: Session) -> None:
    carrier = CarrierModel(
        id="pickup-point-test-carrier-001",
        code="pickup_point_test_carrier_001",
        name="Pickup Point Test Carrier 001",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(carrier)
    session.flush()

    repository = PickupPointRepository(session)

    pickup_point = PickupPointModel(
        id="pickup-point-test-001",
        carrier_id="pickup-point-test-carrier-001",
        carrier_pickup_id="CARRIER-PUDO-001",
        name="Test Pickup Point 001",
        pickup_type="STORE",
        street_line_1="10 Rue de Rivoli",
        street_line_2=None,
        postal_code="75001",
        city="Paris",
        state_or_region="Ile-de-France",
        country_code="FR",
        latitude=48.8566,
        longitude=2.3522,
        opening_hours="Monday to Friday",
        active=True,
    )

    repository.save(pickup_point)
    session.flush()

    result = repository.get_by_id("pickup-point-test-001")

    assert result is not None
    assert result.id == "pickup-point-test-001"
    assert result.carrier_pickup_id == "CARRIER-PUDO-001"
    assert result.pickup_type == "STORE"


def test_list_pickup_points_by_carrier(session: Session) -> None:
    carrier = CarrierModel(
        id="pickup-point-test-carrier-002",
        code="pickup_point_test_carrier_002",
        name="Pickup Point Test Carrier 002",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(carrier)
    session.flush()

    repository = PickupPointRepository(session)

    pickup_point_a = PickupPointModel(
        id="pickup-point-test-002",
        carrier_id="pickup-point-test-carrier-002",
        carrier_pickup_id="CARRIER-PUDO-002",
        name="Pickup Point A",
        pickup_type="STORE",
        street_line_1="1 Test Street",
        street_line_2=None,
        postal_code="75001",
        city="Paris",
        state_or_region=None,
        country_code="FR",
        latitude=48.8566,
        longitude=2.3522,
        opening_hours=None,
        active=True,
    )

    pickup_point_b = PickupPointModel(
        id="pickup-point-test-003",
        carrier_id="pickup-point-test-carrier-002",
        carrier_pickup_id="CARRIER-PUDO-003",
        name="Pickup Point B",
        pickup_type="LOCKER",
        street_line_1="2 Test Street",
        street_line_2=None,
        postal_code="75002",
        city="Paris",
        state_or_region=None,
        country_code="FR",
        latitude=48.8666,
        longitude=2.3622,
        opening_hours="24/7",
        active=True,
    )

    repository.save(pickup_point_a)
    repository.save(pickup_point_b)
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


def test_delete_pickup_point(session: Session) -> None:
    carrier = CarrierModel(
        id="pickup-point-test-carrier-003",
        code="pickup_point_test_carrier_003",
        name="Pickup Point Test Carrier 003",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(carrier)
    session.flush()

    repository = PickupPointRepository(session)

    pickup_point = PickupPointModel(
        id="pickup-point-test-004",
        carrier_id="pickup-point-test-carrier-003",
        carrier_pickup_id="CARRIER-PUDO-004",
        name="Pickup Point To Delete",
        pickup_type="STORE",
        street_line_1="3 Test Street",
        street_line_2=None,
        postal_code="75003",
        city="Paris",
        state_or_region=None,
        country_code="FR",
        latitude=48.8766,
        longitude=2.3722,
        opening_hours=None,
        active=True,
    )

    repository.save(pickup_point)
    session.flush()

    repository.delete(pickup_point)
    session.flush()

    result = repository.get_by_id("pickup-point-test-004")

    assert result is None