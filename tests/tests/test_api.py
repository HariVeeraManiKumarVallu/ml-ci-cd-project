import requests

def test_predict_endpoint():
    url = "http://127.0.0.1:8000/predict"
    data = {"data": [5.1, 3.5, 1.4, 0.2]}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()