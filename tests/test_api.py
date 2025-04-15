from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_predict_calories():
    response = client.post("/predict", json={
        "poids_kg": 75,
        "duree_min": 60,
        "vitesse_moyenne": 25,
        "distance_km": 30,
        "fc_moyenne": 145
    })

    assert response.status_code == 200
    data = response.json()
    assert "calories_brulees" in data
    assert isinstance(data["calories_brulees"], float)