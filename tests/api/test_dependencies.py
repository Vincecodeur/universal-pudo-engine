from collections.abc import Generator

from sqlalchemy.orm import Session

from universal_pudo.api.dependencies import get_db


def test_get_db_returns_session_generator() -> None:
    generator = get_db()

    assert isinstance(generator, Generator)


def test_get_db_yields_database_session() -> None:
    generator = get_db()

    session = next(generator)

    try:
        assert isinstance(session, Session)
    finally:
        try:
            next(generator)
        except StopIteration:
            pass