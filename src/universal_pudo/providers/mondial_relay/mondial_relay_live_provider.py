from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)
from universal_pudo.providers.base.pickup_provider import (
    PickupProvider,
)
from universal_pudo.providers.mondial_relay.client import (
    MondialRelayClient,
)
from universal_pudo.providers.mondial_relay.mapper import (
    MondialRelayMapper,
)
from universal_pudo.providers.mondial_relay.response_parser import (
    MondialRelayResponseParser,
)


class MondialRelayLiveProvider(PickupProvider):
    def __init__(
        self,
        client: MondialRelayClient,
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
            and carrier_id != "mondial-relay"
        ):
            return []

        if country_code is None:
            return []

        if postal_code is None:
            return []

        xml_response = self.client.search_pickup_points(
            country_code=country_code,
            postal_code=postal_code,
            city=city or "",
        )

        payloads = (
            MondialRelayResponseParser
            .extract_pickup_points(
                xml_response
            )
        )

        return [
            MondialRelayMapper.to_pickup_point(
                payload
            )
            for payload in payloads
        ]

    def get_pickup_point_details(
        self,
        pickup_point_id: str,
    ) -> PickupPointModel | None:
        return None