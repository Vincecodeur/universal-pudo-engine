import pytest

from universal_pudo.domain.value_objects.address import Address


def test_address_can_be_created_with_required_fields() -> None:
    address = Address(
        street_line_1="10 Rue de Rivoli",
        postal_code="75001",
        city="Paris",
        country_code="FR",
    )

    assert address.street_line_1 == "10 Rue de Rivoli"
    assert address.street_line_2 is None
    assert address.postal_code == "75001"
    assert address.city == "Paris"
    assert address.state_or_region is None
    assert address.country_code == "FR"
    assert address.formatted_address is None


def test_address_can_be_created_with_optional_fields() -> None:
    address = Address(
        street_line_1="10 Rue de Rivoli",
        street_line_2="Building A",
        postal_code="75001",
        city="Paris",
        state_or_region="Ile-de-France",
        country_code="FR",
        formatted_address="10 Rue de Rivoli, 75001 Paris, France",
    )

    assert address.street_line_2 == "Building A"
    assert address.state_or_region == "Ile-de-France"
    assert address.formatted_address == "10 Rue de Rivoli, 75001 Paris, France"


def test_address_is_immutable() -> None:
    address = Address(
        street_line_1="10 Rue de Rivoli",
        postal_code="75001",
        city="Paris",
        country_code="FR",
    )

    with pytest.raises(AttributeError):
        address.city = "Lyon"