import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os
import numpy as np

# Obtenir le chemin absolu du dossier du script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Création des dossiers nécessaires
os.makedirs(os.path.join(PROJECT_ROOT, 'data'), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, 'model'), exist_ok=True)

# Chargement des données
df = pd.read_csv(os.path.join(PROJECT_ROOT, 'data', 'calories.csv'))

# Sélection des features et de la target
X = df[['poids_kg', 'duree_min', 'vitesse_moyenne', 'distance_km', 'fc_moyenne']]
y = df['calories_brulees']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("✅ Modèle entraîné")

y_pred_model = model.predict(X_test)

# Évaluation du modèle
print("Random Forest - MAE : ", mean_absolute_error(y_test, y_pred_model))
print("Random Forest - RMSE : ", np.sqrt(mean_squared_error(y_test, y_pred_model)))

y_train_pred = model.predict(X_train)
print("Train MAE :", mean_absolute_error(y_train, y_train_pred))
print("Test MAE  :", mean_absolute_error(y_test, y_pred_model))

# Sauvegarde du modèle
joblib.dump(model, os.path.join(PROJECT_ROOT, 'model', 'model_calories.pkl'))

print("✅ Modèle entraîné et sauvegardé dans model/model_calories.pkl")