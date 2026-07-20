from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from universal_pudo.api.dependencies import get_db
from universal_pudo.api.schemas.pickup_point import (
    PickupPointResponse,
)
from universal_pudo.application.use_cases.get_pickup_point import (
    GetPickupPointUseCase,
)
from universal_pudo.application.use_cases.list_pickup_points import (
    ListPickupPointsUseCase,
)
from universal_pudo.application.use_cases.search_pickup_points import (
    SearchPickupPointsUseCase,
)
from universal_pudo.infrastructure.database.repositories.pickup_point_repository import (
    PickupPointRepository,
)


from universal_pudo.application.use_cases.search_pickup_points_by_radius import (
    SearchPickupPointsByRadiusUseCase,
)

from universal_pudo.api.dependencies import (
    get_provider_factory,
)

from universal_pudo.application.use_cases.search_hybrid_pickup_points import (
    SearchHybridPickupPointsUseCase,
)

from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)

router = APIRouter(
    prefix="/pickup-points",
    tags=["pickup-points"],
)


@router.get(
    "/search",
    response_model=list[PickupPointResponse],
)
def search_pickup_points(
    db: Annotated[Session, Depends(get_db)],
    provider_factory: Annotated[
        ProviderFactory,
        Depends(get_provider_factory),
    ],
    carrier_id: str | None = None,
    country_code: str | None = None,
    postal_code: str | None = None,
    city: str | None = None,
    pickup_type: str | None = None,
    active: bool | None = True,
):
    repository = PickupPointRepository(
        db
    )

    use_case = SearchHybridPickupPointsUseCase(
        repository=repository,
        provider_factory=provider_factory,
    )

    return use_case.execute(
        carrier_id=carrier_id,
        country_code=country_code,
        postal_code=postal_code,
        city=city,
        pickup_type=pickup_type,
        active=active,
    )


@router.get(
    "/details/{pickup_point_id}",
    response_model=PickupPointResponse,
)
def get_pickup_point(
    pickup_point_id: str,
    db: Annotated[Session, Depends(get_db)],
):
    repository = PickupPointRepository(db)

    use_case = GetPickupPointUseCase(
        repository,
    )

    pickup_point = use_case.execute(
        pickup_point_id,
    )

    if pickup_point is None:
        raise HTTPException(
            status_code=404,
            detail="Pickup point not found",
        )

    return pickup_point

@router.get(
    "/search-radius",
    response_model=list[
        PickupPointResponse
    ],
)
def search_pickup_points_by_radius(
    latitude: float,
    longitude: float,
    radius_km: float,
    db: Annotated[
        Session,
        Depends(get_db),
    ],
):
    repository = PickupPointRepository(
        db
    )

    use_case = (
        SearchPickupPointsByRadiusUseCase(
            repository
        )
    )

    return use_case.execute(
        latitude=latitude,
        longitude=longitude,
        radius_km=radius_km,
    )

@router.get(
    "/{carrier_id}",
    response_model=list[PickupPointResponse],
)
def list_pickup_points(
    carrier_id: str ,
    db: Annotated[Session, Depends(get_db)],
):
    repository = PickupPointRepository(db)

    use_case = ListPickupPointsUseCase(
        repository,
    )

    return use_case.execute(
        carrier_id,
    )