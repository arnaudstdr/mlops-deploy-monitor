import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os
import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import pandas as pd

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
with mlflow.start_run():
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    mlflow.log_param("model_type", "RandomForestRegressor")
    mlflow.log_param("n_estimators", 100)

    model.fit(X_train, y_train)
    print("✅ Modèle entraîné")

    y_pred_model = model.predict(X_test)
    y_train_pred = model.predict(X_train)

# Évaluation du modèle
    mae_test = mean_absolute_error(y_test, y_pred_model)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_model))
    mae_train = mean_absolute_error(y_train, y_train_pred)

    print("Random Forest - MAE : ", mae_test)
    print("Random Forest - RMSE : ", rmse_test)
    print("Train MAE : ", mae_train)
    print("Test MAE : ", mae_test)

    mlflow.log_metric("mae_test", mae_test)
    mlflow.log_metric("rmse_test", rmse_test)
    mlflow.log_metric("mae_train", mae_train)

    input_example = X_test.iloc[[0]].to_dict(orient="records")[0]
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        input_example=input_example,
        registered_model_name="CaloriesPredictor"
    )

    # Sauvegarde locale du modèle
    joblib.dump(model, os.path.join(PROJECT_ROOT, 'model', 'model_calories.pkl'))
    print("✅ Modèle entraîné et sauvegardé dans model/model_calories.pkl")

# Visualisation des résultats
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred_model, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--')
plt.xlabel("Valeurs réelles")
plt.ylabel("Prédictiopns")
plt.title("Prédictions Random Forest vs Réalité")
plt.grid(True)
plt.show()
