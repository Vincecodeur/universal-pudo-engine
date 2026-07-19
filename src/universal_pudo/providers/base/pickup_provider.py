from abc import ABC
from abc import abstractmethod


class PickupProvider(ABC):

    @abstractmethod
    def search_pickup_points(
        self,
        *,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
    ):
        pass

    @abstractmethod
    def get_pickup_point_details(
        self,
        pickup_point_id: str,
    ):
        pass