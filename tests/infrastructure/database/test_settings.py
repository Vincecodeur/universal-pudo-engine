from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)


def test_settings_can_be_created_without_env():
    settings = DatabaseSettings()

    assert settings.database_url == ""