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

def test_missing_fields():
    response = client.post("/predict", json={
        "poids_kg": 75,
        "duree_min": 60,
        # champs manquants
    })

    assert response.status_code == 422 # Erreur de validation

def test_extreme_values():
    response = client.post("/predict", json={
        "poids_kg": 300,
        "duree_min": 0,
        "vitesse_moyenne": -10,
        "distance_km": 9999,
        "fc_moyenne": 10
    })

    assert response.status_code == 200
    assert isinstance(response.json()["calories_brulees"], float)

def test_response_format():
    response = client.post("/predict", json={
        "poids_kg": 80,
        "duree_min": 45,
        "vitesse_moyenne": 20,
        "distance_km": 15,
        "fc_moyenne": 130
    })

    data = response.json()
    assert isinstance(data, dict)
    assert "calories_brulees" in data
    assert isinstance(data["calories_brulees"], float)

import time

def test_response_time():
    start = time.time()
    response = client.post("/predict", json={
        "poids_kg": 70,
        "duree_min": 30,
        "vitesse_moyenne": 22,
        "distance_km": 20,
        "fc_moyenne": 150
    })
    duration = time.time() - start
    assert response.status_code == 200
    assert duration < 1.0 # Temps de réponse raisonnable