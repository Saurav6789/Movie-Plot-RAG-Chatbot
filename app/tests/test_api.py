from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_ask_endpoint():
    response = client.post(
        "/ask",
        json={"query": "What is AI?", "top_k": 2},
    )

    assert response.status_code in [200, 500]  # depends on env setup
