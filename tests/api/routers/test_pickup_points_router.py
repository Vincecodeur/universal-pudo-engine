from fastapi import APIRouter

from universal_pudo.api.routers.pickup_points import (
    router,
)


def test_pickup_points_router_is_api_router() -> None:
    assert isinstance(router, APIRouter)


def test_pickup_points_router_prefix() -> None:
    assert router.prefix == "/pickup-points"


def test_pickup_points_router_has_routes() -> None:
    assert len(router.routes) > 0