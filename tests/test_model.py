import os
import joblib
import numpy as np

# Chemin vers le modèle
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../model/model_calories.pkl")

def test_model_load_and_predict():
    # Charger le modèle
    model = joblib.load(MODEL_PATH)

    # Exemple d'entrée : poids, durée, vitesse moyenne, distance, FC moyenne
    example_input = np.array([
        [75, 60, 25, 30, 140]
    ])

    # Prédiction
    prediction = model.predict(example_input)
    
    # Vérifications

    assert isinstance(prediction[0], float)
    assert prediction[0] > 0

    print(f"Prédiction : {prediction[0]} calories")

if __name__ == "__main__":
    test_model_load_and_predict()