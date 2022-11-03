from fastapi.testclient import TestClient


def test_ping(client: TestClient):
    response = client.get("/v1/ping/app")
    assert response.status_code == 200


def test_ping_db(db, client: TestClient):
    response = client.get("/v1/ping/db")
    assert response.status_code == 200
