from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)

from universal_pudo.providers.base.pickup_provider import (
    PickupProvider,
)

from universal_pudo.providers.colissimo.client import (
    ColissimoClient,
)

from universal_pudo.providers.colissimo.mapper import (
    ColissimoMapper,
)

class ColissimoLiveProvider(PickupProvider):
    def __init__(
        self,
        client: ColissimoClient,
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
            and carrier_id != "colissimo"
        ):
            return []

        if postal_code is None:
            return []

        if city is None:
            return []

        payload = self.client.search_pickup_points(
            address="",
            zip_code=postal_code,
            city=city,
            shipping_date="20/07/2026",
            country_code=country_code or "FR",
        )

        pickup_points = payload.get(
            "listePointRetraitAcheminement",
            [],
        )

        return [
            ColissimoMapper.to_pickup_point(
                point
            )
            for point in pickup_points
        ]

    def get_pickup_point_details(
        self,
        pickup_point_id: str,
    ) -> PickupPointModel | None:
        return None