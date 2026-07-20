from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class DatabaseSettings(BaseSettings):
    database_url: str

    hybrid_search_cache_ttl_days: int = 7

    colissimo_api_key: str

    mondial_relay_enseigne: str

    mondial_relay_private_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )