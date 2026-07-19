from pydantic import BaseModel


class CarrierResponse(BaseModel):
    id: str
    code: str
    name: str
    lifecycle: str

    model_config = {
        "from_attributes": True,
    }