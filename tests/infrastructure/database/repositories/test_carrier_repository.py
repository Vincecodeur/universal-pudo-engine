from sqlalchemy.orm import Session

from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)
from universal_pudo.infrastructure.database.repositories.carrier_repository import (
    CarrierRepository,
)


def test_repository_creation() -> None:
    session = Session()

    repository = CarrierRepository(session)

    assert repository.session is session


def test_repository_has_expected_methods() -> None:
    session = Session()

    repository = CarrierRepository(session)

    assert callable(repository.get_by_id)
    assert callable(repository.get_by_code)
    assert callable(repository.list_all)
    assert callable(repository.save)
    assert callable(repository.delete)