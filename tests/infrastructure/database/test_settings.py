from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)


def test_settings_can_be_loaded() -> None:
    settings = DatabaseSettings()

    assert settings.database_url.startswith(
        "postgresql+psycopg://"
    )

    assert (
        settings.hybrid_search_cache_ttl_days
        > 0
    )