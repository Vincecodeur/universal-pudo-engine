from dataclasses import dataclass


@dataclass(slots=True)
class CarrierAccount:
    """
    Represents customer-owned carrier credentials.

    Universal PUDO Engine never owns carrier accounts.
    """

    account_id: str
    carrier_id: str

    account_name: str

    status: str = "ACTIVE"