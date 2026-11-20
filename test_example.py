import requests

def test_example_status():
    response = requests.get("https://httpbin.org/status/200")
    assert response.status_code == 200
