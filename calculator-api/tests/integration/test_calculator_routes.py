from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add():
    payload = {"num1": 2, "num2": 3}
    response = client.post("/calculator/add", json=payload)
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_subtract():
    payload = {"num1": 5, "num2": 3}
    response = client.post("/calculator/subtract", json=payload)
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_multiply():
    payload = {"num1": 2, "num2": 3}
    response = client.post("/calculator/multiply", json=payload)
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_divide():
    payload = {"num1": 10, "num2": 2}
    response = client.post("/calculator/divide", json=payload)
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_divide_by_zero():
    payload = {"num1": 10, "num2": 0}
    response = client.post("/calculator/divide", json=payload)
    assert response.status_code == 422
    assert "num2 cannot be zero for division" in response.json()["detail"][0]["msg"]
