from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.models.carrier_account_model import (
    CarrierAccountModel,
)
from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)
from universal_pudo.infrastructure.database.repositories.carrier_account_repository import (
    CarrierAccountRepository,
)


def test_repository_creation(session: Session) -> None:
    repository = CarrierAccountRepository(session)

    assert repository.session is session


def test_save_and_get_carrier_account_by_id(session: Session) -> None:
    carrier = CarrierModel(
        id="carrier-account-test-carrier-001",
        code="carrier_account_test_carrier_001",
        name="Carrier Account Test Carrier 001",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(carrier)
    session.flush()

    repository = CarrierAccountRepository(session)

    account = CarrierAccountModel(
        id="account-test-001",
        carrier_id="carrier-account-test-carrier-001",
        account_name="Test Account 001",
        status="ACTIVE",
    )

    repository.save(account)
    session.flush()

    result = repository.get_by_id("account-test-001")

    assert result is not None
    assert result.id == "account-test-001"
    assert result.carrier_id == "carrier-account-test-carrier-001"
    assert result.account_name == "Test Account 001"


def test_list_accounts_by_carrier(session: Session) -> None:
    carrier = CarrierModel(
        id="carrier-account-test-carrier-002",
        code="carrier_account_test_carrier_002",
        name="Carrier Account Test Carrier 002",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(carrier)
    session.flush()

    repository = CarrierAccountRepository(session)

    account_a = CarrierAccountModel(
        id="account-test-002",
        carrier_id="carrier-account-test-carrier-002",
        account_name="Test Account A",
        status="ACTIVE",
    )

    account_b = CarrierAccountModel(
        id="account-test-003",
        carrier_id="carrier-account-test-carrier-002",
        account_name="Test Account B",
        status="ACTIVE",
    )

    repository.save(account_a)
    repository.save(account_b)
    session.flush()

    results = repository.list_by_carrier(
        "carrier-account-test-carrier-002"
    )

    account_names = [
        account.account_name
        for account in results
    ]

    assert "Test Account A" in account_names
    assert "Test Account B" in account_names


def test_delete_carrier_account(session: Session) -> None:
    carrier = CarrierModel(
        id="carrier-account-test-carrier-003",
        code="carrier_account_test_carrier_003",
        name="Carrier Account Test Carrier 003",
        lifecycle="ACTIVE",
        supported_countries=["FR"],
        capabilities=["SEARCH_PICKUP_POINTS"],
    )

    session.add(carrier)
    session.flush()

    repository = CarrierAccountRepository(session)

    account = CarrierAccountModel(
        id="account-test-004",
        carrier_id="carrier-account-test-carrier-003",
        account_name="Test Account 004",
        status="ACTIVE",
    )

    repository.save(account)
    session.flush()

    repository.delete(account)
    session.flush()

    result = repository.get_by_id("account-test-004")

    assert result is None