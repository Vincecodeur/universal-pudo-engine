from universal_pudo.infrastructure.database.session import (
    get_engine,
)


def test_get_engine_function_exists() -> None:
    assert callable(get_engine)