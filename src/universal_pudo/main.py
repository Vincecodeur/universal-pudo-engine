from fastapi import FastAPI

from universal_pudo.api.routers.carriers import (
    router as carriers_router,
)
from universal_pudo.api.routers.pickup_points import (
    router as pickup_points_router,
)
from universal_pudo.api.routers.health import (
    router as health_router,
)

app = FastAPI(
    title="Universal PUDO Engine",
    version="0.1.0",
)

app.include_router(
    carriers_router,
)

app.include_router(
    pickup_points_router,
)

app.include_router(
    health_router,
)


@app.get("/")
def healthcheck() -> dict[str, str]:
    return {
        "status": "ok",
    }