from fastapi import APIRouter

from universal_pudo.api.routers.health import (
    router,
)


def test_health_router_is_api_router() -> None:
    assert isinstance(router, APIRouter)


def test_health_router_prefix() -> None:
    assert router.prefix == "/health"


def test_health_router_has_routes() -> None:
    assert len(router.routes) > 0