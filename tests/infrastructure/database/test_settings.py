from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)


def test_settings_can_be_loaded() -> None:
    settings = DatabaseSettings()

    assert settings.database_url.startswith(
        "postgresql+psycopg://"
    )