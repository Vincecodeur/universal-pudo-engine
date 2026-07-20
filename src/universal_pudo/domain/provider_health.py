from dataclasses import dataclass


@dataclass(slots=True)
class ProviderHealth:
    provider_name: str
    status: str
    response_time_ms: int | None = None