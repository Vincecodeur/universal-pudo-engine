import pytest

from universal_pudo.domain.value_objects.geolocation import GeoLocation


def test_geolocation_can_be_created() -> None:
    geolocation = GeoLocation(
        latitude=48.8566,
        longitude=2.3522,
    )

    assert geolocation.latitude == 48.8566
    assert geolocation.longitude == 2.3522


def test_geolocation_is_immutable() -> None:
    geolocation = GeoLocation(
        latitude=48.8566,
        longitude=2.3522,
    )

    with pytest.raises(AttributeError):
        geolocation.latitude = 43.6047
