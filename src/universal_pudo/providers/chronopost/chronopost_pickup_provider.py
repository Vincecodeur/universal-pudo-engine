from universal_pudo.infrastructure.database.models.pickup_point_model import (
    PickupPointModel,
)
from universal_pudo.providers.base.pickup_provider import (
    PickupProvider,
)
from universal_pudo.providers.chronopost.mapper import (
    ChronopostMapper,
)


class ChronopostPickupProvider(
    PickupProvider
):
    def __init__(
        self,
        payloads: list[dict],
    ) -> None:
        self.payloads = payloads

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

        filtered_payloads = self.payloads

        if country_code is not None:
            filtered_payloads = [
                payload
                for payload in filtered_payloads
                if payload.get(
                    "codePays"
                )
                == country_code
            ]

        if postal_code is not None:
            filtered_payloads = [
                payload
                for payload in filtered_payloads
                if payload.get(
                    "codePostal"
                )
                == postal_code
            ]

        if city is not None:
            filtered_payloads = [
                payload
                for payload in filtered_payloads
                if payload.get(
                    "localite",
                    "",
                ).lower()
                == city.lower()
            ]

        return [
            ChronopostMapper.to_pickup_point(
                payload
            )
            for payload in filtered_payloads
        ]

    def get_pickup_point_details(
        self,
        pickup_point_id: str,
    ) -> PickupPointModel | None:
        for payload in self.payloads:
            pickup_point = (
                ChronopostMapper.to_pickup_point(
                    payload
                )
            )

            if (
                pickup_point.id
                == pickup_point_id
            ):
                return pickup_point

        return None