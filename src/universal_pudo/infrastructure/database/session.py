from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)


def get_engine():
    settings = DatabaseSettings()

    return create_engine(
        settings.database_url,
    )


def get_session_factory():
    engine = get_engine()

    return sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )