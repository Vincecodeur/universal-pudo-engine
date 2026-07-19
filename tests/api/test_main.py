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