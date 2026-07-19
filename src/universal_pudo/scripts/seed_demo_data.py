from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)
from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)


def main() -> None:
    settings = DatabaseSettings()

    engine = create_engine(
        settings.database_url,
    )

    SessionLocal = sessionmaker(
        bind=engine,
    )

    session = SessionLocal()

    try:
        carriers = [
            CarrierModel(
                id="carrier-colissimo",
                code="colissimo_pickup",
                name="Colissimo Pickup",
                lifecycle="ACTIVE",
                supported_countries=["FR"],
                capabilities=[
                    "SEARCH_PICKUP_POINTS",
                    "GET_PICKUP_DETAILS",
                ],
            ),
            CarrierModel(
                id="carrier-mondial-relay",
                code="mondial_relay",
                name="Mondial Relay",
                lifecycle="ACTIVE",
                supported_countries=[
                    "FR",
                    "BE",
                    "ES",
                ],
                capabilities=[
                    "SEARCH_PICKUP_POINTS",
                    "GET_PICKUP_DETAILS",
                ],
            ),
            CarrierModel(
                id="carrier-inpost",
                code="inpost_fr",
                name="InPost France",
                lifecycle="ACTIVE",
                supported_countries=["FR"],
                capabilities=[
                    "SEARCH_PICKUP_POINTS",
                    "GET_PICKUP_DETAILS",
                ],
            ),
        ]

        for carrier in carriers:
            existing = (
                session.query(CarrierModel)
                .filter(
                    CarrierModel.id == carrier.id
                )
                .first()
            )

            if existing is None:
                session.add(carrier)

        session.commit()

        print("Demo carriers seeded successfully.")

    finally:
        session.close()


if __name__ == "__main__":
    main()