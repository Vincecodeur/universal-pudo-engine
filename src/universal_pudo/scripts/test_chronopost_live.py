from datetime import datetime
from datetime import timedelta
from pathlib import Path
from pprint import pprint

from universal_pudo.infrastructure.database.settings import (
    DatabaseSettings,
)

from universal_pudo.providers.chronopost.client import (
    ChronopostClient,
)

from universal_pudo.providers.chronopost.response_parser import (
    ChronopostResponseParser,
)

from universal_pudo.providers.chronopost.mapper import (
    ChronopostMapper,
)


def pickup_point_to_dict(
    pickup_point,
) -> dict:
    return {
        "id": pickup_point.id,
        "carrier_id": pickup_point.carrier_id,
        "carrier_pickup_id": pickup_point.carrier_pickup_id,
        "name": pickup_point.name,
        "pickup_type": pickup_point.pickup_type,
        "street_line_1": pickup_point.street_line_1,
        "street_line_2": pickup_point.street_line_2,
        "postal_code": pickup_point.postal_code,
        "city": pickup_point.city,
        "state_or_region": pickup_point.state_or_region,
        "country_code": pickup_point.country_code,
        "latitude": pickup_point.latitude,
        "longitude": pickup_point.longitude,
        "opening_hours": pickup_point.opening_hours,
        "active": pickup_point.active,
    }


def main() -> None:
    settings = DatabaseSettings()

    client = ChronopostClient(
        account_number=settings.chronopost_account_number,
        password=settings.chronopost_password,
    )

    shipping_date = (
        datetime.now()
        + timedelta(days=1)
    ).strftime(
        "%d/%m/%Y"
    )

    xml_response = client.search_pickup_points(
        address="38 grande rue",
        zip_code="92130",
        city="ISSY LES MOULINEAUX",
        country_code="FR",
        shipping_date=shipping_date,
        product_code="86",
        weight="1",
        max_point_chronopost="10",
        max_distance_search="10",

    )

    fixture_path = Path(
        "tests/fixtures/chronopost/"
        "recherchePointChronopostInter_live_response.xml"
    )

    fixture_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    fixture_path.write_text(
        xml_response,
        encoding="utf-8",
    )

    payloads = (
        ChronopostResponseParser.extract_pickup_points(
            xml_response
        )
    )

    print(
        f"Found {len(payloads)} Chronopost pickup points"
    )

    if not payloads:
        print("No pickup points returned")
        return

    pickup_point = (
        ChronopostMapper.to_pickup_point(
            payloads[0]
        )
    )

    print("First mapped PickupPointModel:")

    pprint(
        pickup_point_to_dict(
            pickup_point
        )
    )


if __name__ == "__main__":
    main()