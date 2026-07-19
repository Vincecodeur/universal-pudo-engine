from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)


settings = DatabaseSettings()

engine = create_engine(
    settings.database_url,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def get_db():
    session: Session = SessionLocal()

    try:
        yield session
    finally:
        session.close()