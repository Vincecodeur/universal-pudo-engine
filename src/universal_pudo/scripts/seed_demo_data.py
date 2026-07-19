from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from universal_pudo.infrastructure.database.models.carrier_model import (
    CarrierModel,
)
from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
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

        pickup_points = [
            PickupPointModel(
                id="pickup-colissimo-paris-rivoli",
                carrier_id="carrier-colissimo",
                carrier_pickup_id="COL-001",
                name="Paris Rivoli Pickup",
                pickup_type="STORE",
                street_line_1="10 Rue de Rivoli",
                street_line_2=None,
                postal_code="75001",
                city="Paris",
                state_or_region="Ile-de-France",
                country_code="FR",
                latitude=48.8566,
                longitude=2.3522,
                opening_hours="Mon-Sat 08:00-19:00",
                active=True,
            ),
            PickupPointModel(
                id="pickup-mondial-relay-lyon",
                carrier_id="carrier-mondial-relay",
                carrier_pickup_id="MR-001",
                name="Lyon Bellecour Relay",
                pickup_type="STORE",
                street_line_1="5 Place Bellecour",
                street_line_2=None,
                postal_code="69002",
                city="Lyon",
                state_or_region="Auvergne-Rhone-Alpes",
                country_code="FR",
                latitude=45.7578,
                longitude=4.8320,
                opening_hours="Mon-Sat 09:00-20:00",
                active=True,
            ),
            PickupPointModel(
                id="pickup-inpost-defense-locker",
                carrier_id="carrier-inpost",
                carrier_pickup_id="INP-001",
                name="La Defense Locker",
                pickup_type="LOCKER",
                street_line_1="Parvis de La Defense",
                street_line_2=None,
                postal_code="92800",
                city="Puteaux",
                state_or_region="Ile-de-France",
                country_code="FR",
                latitude=48.8919,
                longitude=2.2381,
                opening_hours="24/7",
                active=True,
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

        for pickup_point in pickup_points:
            existing = (
                session.query(PickupPointModel)
                .filter(
                    PickupPointModel.id
                    == pickup_point.id
                )
                .first()
            )

            if existing is None:
                session.add(pickup_point)

        session.commit()

        print(
            "Demo carriers and pickup points seeded successfully."
        )

    finally:
        session.close()


if __name__ == "__main__":
    main()