from pydantic import BaseModel


class ProviderHealthResponse(BaseModel):
    provider_name: str
    status: str
    response_time_ms: int | None

    model_config = {
        "from_attributes": True,
    }