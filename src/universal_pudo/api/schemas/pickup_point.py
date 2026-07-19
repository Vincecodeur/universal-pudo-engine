from pydantic import BaseModel


class PickupPointResponse(BaseModel):
    id: str
    carrier_id: str
    carrier_pickup_id: str
    name: str
    pickup_type: str
    city: str
    country_code: str

    model_config = {
        "from_attributes": True,
    }