from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)
from universal_pudo.infrastructure.database.repositories.carrier_repository import (
    CarrierRepository,
)


def test_repository_creation(session: Session) -> None:
    repository = CarrierRepository(session)

    assert repository.session is session


def test_save_and_get_carrier_by_id(session: Session) -> None:
    repository = CarrierRepository(session)

    carrier = CarrierModel(
        id="carrier-test-001",
        code="test_carrier_001",
        name="Test Carrier 001",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    repository.save(carrier)
    session.flush()

    result = repository.get_by_id("carrier-test-001")

    assert result is not None
    assert result.id == "carrier-test-001"
    assert result.code == "test_carrier_001"
    assert result.name == "Test Carrier 001"


def test_get_carrier_by_code(session: Session) -> None:
    repository = CarrierRepository(session)

    carrier = CarrierModel(
        id="carrier-test-002",
        code="test_carrier_002",
        name="Test Carrier 002",
        lifecycle="ACTIVE",
        supported_countries=["FR", "BE"],
        capabilities=[
            "SEARCH_PICKUP_POINTS",
            "GET_PICKUP_DETAILS",
        ],
    )

    repository.save(carrier)
    session.flush()

    result = repository.get_by_code("test_carrier_002")

    assert result is not None
    assert result.id == "carrier-test-002"
    assert result.supported_countries == ["FR", "BE"]


def test_list_all_carriers(session: Session) -> None:
    repository = CarrierRepository(session)

    carrier_a = CarrierModel(
        id="carrier-test-003",
        code="test_carrier_003",
        name="Alpha Carrier",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    carrier_b = CarrierModel(
        id="carrier-test-004",
        code="test_carrier_004",
        name="Beta Carrier",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    repository.save(carrier_b)
    repository.save(carrier_a)
    session.flush()

    results = repository.list_all()

    names = [
        carrier.name
        for carrier in results
    ]

    assert "Alpha Carrier" in names
    assert "Beta Carrier" in names


def test_delete_carrier(session: Session) -> None:
    repository = CarrierRepository(session)

    carrier = CarrierModel(
        id="carrier-test-005",
        code="test_carrier_005",
        name="Test Carrier 005",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    repository.save(carrier)
    session.flush()

    repository.delete(carrier)
    session.flush()

    result = repository.get_by_id("carrier-test-005")

    assert result is None