from universal_pudo.domain.models.carrier_account import CarrierAccount


def test_carrier_account_can_be_created_with_required_fields() -> None:
    carrier_account = CarrierAccount(
        account_id="account-001",
        carrier_id="carrier-001",
        account_name="Demo Colissimo Account",
    )

    assert carrier_account.account_id == "account-001"
    assert carrier_account.carrier_id == "carrier-001"
    assert carrier_account.account_name == "Demo Colissimo Account"
    assert carrier_account.status == "ACTIVE"


def test_carrier_account_can_be_created_with_custom_status() -> None:
    carrier_account = CarrierAccount(
        account_id="account-002",
        carrier_id="carrier-002",
        account_name="Disabled Mondial Relay Account",
        status="DISABLED",
    )

    assert carrier_account.status == "DISABLED"