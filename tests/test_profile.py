def test_update_profile(client):
    response = client.post("/profile", json={"name": "John"})
    assert response.status_code == 200
    assert response.json["message"] == "Profile updated successfully"

def test_missing_name(client):
    response = client.post("/profile", json={})
    assert response.status_code == 400
    assert "error" in response.json

