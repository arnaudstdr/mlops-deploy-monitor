import joblib
import os
import numpy as np
import pandas as pd

class CaloriesPredictor:
    def __init__(self):
        # Obtenir le chemin absolu du dossier du script
        SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
        
        # Charger le modèle
        self.model = joblib.load(os.path.join(PROJECT_ROOT, 'model', 'model_calories.pkl'))
        
    def predict(self, poids_kg, duree_min, vitesse_moyenne, distance_km, fc_moyenne):
        """
        Fait une prédiction de calories brûlées
        
        Args:
            poids_kg (float): Poids en kg
            duree_min (float): Durée en minutes
            vitesse_moyenne (float): Vitesse moyenne en km/h
            distance_km (float): Distance en km
            fc_moyenne (float): Fréquence cardiaque moyenne
            
        Returns:
            float: Prédiction des calories brûlées
        """
        # Créer un DataFrame avec les features
        data = pd.DataFrame({
            'poids_kg': [poids_kg],
            'duree_min': [duree_min],
            'vitesse_moyenne': [vitesse_moyenne],
            'distance_km': [distance_km],
            'fc_moyenne': [fc_moyenne]
        })
        
        # Faire la prédiction
        prediction = self.model.predict(data)
        
        return float(prediction[0])

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer une instance du prédicteur
    predictor = CaloriesPredictor()
    
    # Exemple de prédiction
    prediction = predictor.predict(
        poids_kg=90,
        duree_min=80,
        vitesse_moyenne=25,
        distance_km=40,
        fc_moyenne=150
    )
    
    print(f"Prédiction de calories brûlées : {prediction:.2f} kcal")
