from app import app

def test_add():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    assert response.get_json()["result"] == 5

def test_subtract():
    client = app.test_client()
    response = client.get("/subtract?a=5&b=2")
    assert response.get_json()["result"] == 3
