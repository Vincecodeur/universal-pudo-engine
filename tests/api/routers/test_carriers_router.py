from fastapi import APIRouter

from universal_pudo.api.routers.carriers import (
    router,
)


def test_carriers_router_is_api_router() -> None:
    assert isinstance(router, APIRouter)


def test_carriers_router_prefix() -> None:
    assert router.prefix == "/carriers"


def test_carriers_router_has_routes() -> None:
    assert len(router.routes) > 0