from fastapi import APIRouter

router = APIRouter(
    prefix="/pickup-points",
    tags=["pickup-points"],
)


@router.get("/")
def list_pickup_points():
    return {
        "message": "pickup points endpoint ready"
    }