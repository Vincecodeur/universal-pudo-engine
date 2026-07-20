from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class DatabaseSettings(BaseSettings):
    database_url: str

    hybrid_search_cache_ttl_days: int = 7

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )