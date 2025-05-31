import requests

def test_predict_endpoint():
    url = "http://127.0.0.1:8000/predict"
    data = {"data": [5.1, 3.5, 1.4, 0.2]}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_invalid_input():
    url = "http://127.0.0.1:8000/predict"
    data = {"data": [1.0, 2.0]}  # Wrong shape
    response = requests.post(url, json=data)
    assert response.status_code == 422

def test_predict_non_numeric():
    url = "http://127.0.0.1:8000/predict"
    data = {"data": ["a", "b", "c", "d"]}
    response = requests.post(url, json=data)
    assert response.status_code == 422

def test_health_endpoint():
    url = "http://127.0.0.1:8000/health"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}