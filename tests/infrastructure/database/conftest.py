from collections.abc import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)


@pytest.fixture
def session() -> Generator[Session, None, None]:
    settings = DatabaseSettings()

    engine = create_engine(
        settings.database_url,
    )

    connection = engine.connect()

    transaction = connection.begin()

    SessionLocal = sessionmaker(
        bind=connection,
    )

    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()
        transaction.rollback()
        connection.close()