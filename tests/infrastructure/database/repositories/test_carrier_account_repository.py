from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.repositories.carrier_account_repository import (
    CarrierAccountRepository,
)


def test_repository_creation() -> None:
    session = Session()

    repository = CarrierAccountRepository(session)

    assert repository.session is session


def test_repository_has_expected_methods() -> None:
    session = Session()

    repository = CarrierAccountRepository(session)

    assert callable(repository.get_by_id)
    assert callable(repository.list_by_carrier)
    assert callable(repository.save)
    assert callable(repository.delete)