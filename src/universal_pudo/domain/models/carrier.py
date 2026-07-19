from dataclasses import dataclass, field

from universal_pudo.domain.enums.carrier_capability import (
    CarrierCapability,
)
from universal_pudo.domain.enums.carrier_lifecycle import (
    CarrierLifecycle,
)


@dataclass(slots=True)
class Carrier:
    """
    Represents a carrier integration.

    A carrier integration represents a coherent API.
    """

    carrier_id: str
    code: str
    name: str

    lifecycle: CarrierLifecycle = CarrierLifecycle.ACTIVE

    supported_countries: list[str] = field(
        default_factory=list
    )

    capabilities: list[CarrierCapability] = field(
        default_factory=list
    )