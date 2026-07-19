from fastapi.testclient import TestClient

from universal_pudo.main import app


client = TestClient(app)


def test_root_endpoint() -> None:
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok",
    }


def test_carriers_endpoint() -> None:
    response = client.get("/carriers/")

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list,
    )

def test_pickup_points_endpoint() -> None:
    response = client.get(
        "/pickup-points/carrier-colissimo"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list,
    )
    
def test_get_carrier_by_id() -> None:
    response = client.get(
        "/carriers/carrier-colissimo"
    )

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == "carrier-colissimo"
    assert body["code"] == "colissimo_pickup"
    assert body["name"] == "Colissimo Pickup"
    
def test_get_unknown_carrier_returns_404() -> None:
    response = client.get(
        "/carriers/unknown-carrier"
    )

    assert response.status_code == 404
    
def test_get_pickup_point_by_id() -> None:
    response = client.get(
        "/pickup-points/details/pickup-colissimo-paris-rivoli"
    )

    assert response.status_code == 200

    body = response.json()

    assert (
        body["id"]
        == "pickup-colissimo-paris-rivoli"
    )

    assert (
        body["carrier_id"]
        == "carrier-colissimo"
    )

    assert (
        body["carrier_pickup_id"]
        == "COL-001"
    )

    assert (
        body["name"]
        == "Paris Rivoli Pickup"
    )

def test_get_unknown_pickup_point_returns_404() -> None:
    response = client.get(
        "/pickup-points/details/unknown-pickup-point"
    )

    assert response.status_code == 404
    

def test_search_pickup_points_without_filters() -> None:
    response = client.get(
        "/pickup-points/search"
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(
        body,
        list,
    )


def test_search_pickup_points_by_carrier_id() -> None:
    response = client.get(
        "/pickup-points/search?carrier_id=carrier-colissimo"
    )

    assert response.status_code == 200

    body = response.json()

    assert any(
        pickup_point["carrier_id"] == "carrier-colissimo"
        for pickup_point in body
    )


def test_search_pickup_points_by_country_code() -> None:
    response = client.get(
        "/pickup-points/search?country_code=FR"
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(
        body,
        list,
    )

    assert all(
        pickup_point["country_code"] == "FR"
        for pickup_point in body
    )


def test_search_pickup_points_by_postal_code() -> None:
    response = client.get(
        "/pickup-points/search?postal_code=75001"
    )

    assert response.status_code == 200

    body = response.json()

    assert any(
        pickup_point["id"]
        == "pickup-colissimo-paris-rivoli"
        for pickup_point in body
    )


def test_search_pickup_points_by_city() -> None:
    response = client.get(
        "/pickup-points/search?city=Paris"
    )

    assert response.status_code == 200

    body = response.json()

    assert any(
        pickup_point["city"] == "Paris"
        for pickup_point in body
    )


def test_search_pickup_points_by_pickup_type() -> None:
    response = client.get(
        "/pickup-points/search?pickup_type=LOCKER"
    )

    assert response.status_code == 200

    body = response.json()

    assert any(
        pickup_point["pickup_type"] == "LOCKER"
        for pickup_point in body
    )
    
def test_search_pickup_points_by_radius() -> None:
    response = client.get(
        "/pickup-points/search-radius"
        "?latitude=48.8566"
        "&longitude=2.3522"
        "&radius_km=15"
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(
        body,
        list,
    )

    assert len(body) >= 1