from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)

from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)

from universal_pudo.providers.colissimo.client import (
    ColissimoClient,
)

from universal_pudo.providers.colissimo.colissimo_live_provider import (
    ColissimoLiveProvider,
)

from universal_pudo.providers.mondial_relay.client import (
    MondialRelayClient,
)

from universal_pudo.providers.mondial_relay.mondial_relay_live_provider import (
    MondialRelayLiveProvider,
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


def get_provider_factory() -> ProviderFactory:
    colissimo_provider = (
        ColissimoLiveProvider(
            ColissimoClient(
                api_key=settings.colissimo_api_key,
            )
        )
    )

    mondial_relay_provider = (
        MondialRelayLiveProvider(
            MondialRelayClient(
                enseigne=settings.mondial_relay_enseigne,
                private_key=settings.mondial_relay_private_key,
            )
        )
    )

    return ProviderFactory(
        {
            "colissimo": colissimo_provider,
            "mondial-relay": mondial_relay_provider,
        }
    )