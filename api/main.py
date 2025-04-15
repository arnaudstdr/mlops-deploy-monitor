from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from deployment.inference import CaloriesPredictor
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="API de Prédiction de Calories",
    description="API pour prédire les calories brûlées lors d'une sortie Vélo",
    version="1.0.0"
)

# Initialisation du modèle
try:
    model = CaloriesPredictor()
    logger.info("Modèle chargé avec succès")
except Exception as e:
    logger.error(f"Erreur lors du chargement du modèle : {str(e)}")
    raise

class InputData(BaseModel):
    poids_kg: float = Field(..., gt=0, description="Poids en kilogrammes")
    duree_min: float = Field(..., gt=0, description="Durée en minutes")
    vitesse_moyenne: float = Field(..., ge=0, description="Vitesse moyenne en km/h")
    distance_km: float = Field(..., ge=0, description="Distance en kilomètres")
    fc_moyenne: float = Field(..., gt=0, description="Fréquence cardiaque moyenne")

    class Config:
        schema_extra = {
            "example": {
                "poids_kg": 70,
                "duree_min": 30,
                "vitesse_moyenne": 10,
                "distance_km": 5,
                "fc_moyenne": 120
            }
        }

@app.post("/predict", 
          response_model=dict,
          summary="Prédire les calories brûlées",
          description="Calcule le nombre de calories brûlées en fonction des paramètres d'entrée")
async def predict(data: InputData):
    try:
        prediction = model.predict(
            poids_kg=data.poids_kg,
            duree_min=data.duree_min,
            vitesse_moyenne=data.vitesse_moyenne,
            distance_km=data.distance_km,
            fc_moyenne=data.fc_moyenne
        )
        logger.info(f"Prédiction réussie pour les données : {data.dict()}")
        return {"calories_brulees": round(prediction, 2)}
    except Exception as e:
        logger.error(f"Erreur lors de la prédiction : {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health", 
         summary="Vérifier l'état de l'API",
         description="Endpoint pour vérifier que l'API est opérationnelle")
async def health_check():
    return {"status": "healthy"}

