from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from universal_pudo.api.dependencies import get_db
from universal_pudo.api.schemas.pickup_point import (
    PickupPointResponse,
)
from universal_pudo.application.use_cases.list_pickup_points import (
    ListPickupPointsUseCase,
)
from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)

router = APIRouter(
    prefix="/pickup-points",
    tags=["pickup-points"],
)


@router.get(
    "/{carrier_id}",
    response_model=list[PickupPointResponse],
)
def list_pickup_points(
    carrier_id: str,
    db: Annotated[Session, Depends(get_db)],
):
    repository = PickupPointRepository(db)

    use_case = ListPickupPointsUseCase(
        repository,
    )

    return use_case.execute(
        carrier_id,
    )