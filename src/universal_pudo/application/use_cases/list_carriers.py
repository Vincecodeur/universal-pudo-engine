from universal_pudo.infrastructure.database.repositories.carrier_repository import (
    CarrierRepository,
)


class ListCarriersUseCase:
    def __init__(
        self,
        repository: CarrierRepository,
    ) -> None:
        self.repository = repository

    def execute(self):
        return self.repository.list_all()