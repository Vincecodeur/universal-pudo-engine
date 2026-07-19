from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from universal_pudo.api.dependencies import get_db
from universal_pudo.api.schemas.carrier import CarrierResponse
from universal_pudo.application.use_cases.list_carriers import (
    ListCarriersUseCase,
)
from universal_pudo.infrastructure.database.repositories.carrier_repository import (
    CarrierRepository,
)

router = APIRouter(
    prefix="/carriers",
    tags=["carriers"],
)


@router.get(
    "/",
    response_model=list[CarrierResponse],
)
def list_carriers(
    db: Annotated[Session, Depends(get_db)],
):
    repository = CarrierRepository(db)

    use_case = ListCarriersUseCase(
        repository,
    )

    return use_case.execute()