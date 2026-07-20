from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from universal_pudo.api.dependencies import (
    get_provider_factory,
)
from universal_pudo.api.schemas.provider_health import (
    ProviderHealthResponse,
)
from universal_pudo.application.use_cases.get_provider_health import (
    GetProviderHealthUseCase,
)
from universal_pudo.providers.factory.provider_factory import (
    ProviderFactory,
)

router = APIRouter(
    prefix="/health",
    tags=["health"],
)


@router.get(
    "/providers",
    response_model=list[
        ProviderHealthResponse
    ],
)
def get_provider_health(
    provider_factory: Annotated[
        ProviderFactory,
        Depends(get_provider_factory),
    ],
):
    use_case = GetProviderHealthUseCase(
        provider_factory,
    )

    return use_case.execute()