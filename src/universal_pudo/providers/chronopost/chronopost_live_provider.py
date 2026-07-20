from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)
from universal_pudo.providers.base.pickup_provider import (
    PickupProvider,
)
from universal_pudo.providers.chronopost.client import (
    ChronopostClient,
)
from universal_pudo.providers.chronopost.mapper import (
    ChronopostMapper,
)
from universal_pudo.providers.chronopost.response_parser import (
    ChronopostResponseParser,
)


class ChronopostLiveProvider(
    PickupProvider
):
    def __init__(
        self,
        client: ChronopostClient,
    ) -> None:
        self.client = client

    def search_pickup_points(
        self,
        *,
        carrier_id: str | None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
    ) -> list[PickupPointModel]:
        if (
            carrier_id is not None
            and carrier_id != "chronopost"
        ):
            return []

        if postal_code is None:
            return []

        xml_response = self.client.search_pickup_points(
            address="",
            zip_code=postal_code,
            city=city or "",
            country_code=country_code or "FR",
            shipping_date="20/07/2026",
        )

        payloads = (
            ChronopostResponseParser
            .extract_pickup_points(
                xml_response
            )
        )

        return [
            ChronopostMapper.to_pickup_point(
                payload
            )
            for payload in payloads
        ]

    def get_pickup_point_details(
        self,
        pickup_point_id: str,
    ) -> PickupPointModel | None:
        return None