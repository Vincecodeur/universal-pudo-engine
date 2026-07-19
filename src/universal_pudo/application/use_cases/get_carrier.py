from universal_pudo.infrastructure.database.repositories.carrier_repository import (
    CarrierRepository,
)


class GetCarrierUseCase:
    def __init__(
        self,
        repository: CarrierRepository,
    ) -> None:
        self.repository = repository

    def execute(
        self,
        carrier_id: str,
    ):
        return self.repository.get_by_id(
            carrier_id,
        )