from sqlalchemy.orm import DeclarativeBase

from universal_pudo.infrastructure.database.base import Base


def test_base_inherits_from_declarative_base() -> None:
    assert issubclass(Base, DeclarativeBase)