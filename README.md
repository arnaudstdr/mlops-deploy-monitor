# 🚴‍♂️ API de Prédiction de Calories

[![CI - Build and Test FastAPI App](https://github.com/arnaudstdr/mlops-deploy-monitor/actions/workflows/deploy.yml/badge.svg)](https://github.com/arnaudstdr/mlops-deploy-monitor/actions/workflows/deploy.yml)

API FastAPI pour prédire les **calories brûlées lors d’une sortie à vélo** à partir de données physiologiques et de performance.  
Développée dans une logique **MLOps** avec conteneurisation, CI/CD et tests automatisés.

## ✨ Fonctionnalités

- 🔮 Prédiction des calories brûlées avec un modèle Scikit-learn
- 🚀 API RESTful avec FastAPI
- 🧪 Tests utnitaires et automatisés avec `pytest` et `httpx`
- 🐳 Dockerisation complète
- 🔁 CI/CD avec GitHub Actions
- 📜 Documentation automatique (Swagger)

## 📦 Installation locale

### 1. Clone du repo
```bash
git clone https://github.com/arnaudstdr/mlops-deploy-monitor.git
cd mlops-deploy-monitor
```

### 2. Build de l'image Docker
```bash
docker build -t mlops-api .
```

### 3. Lancement du conteneur
```bash
docker run -d -p 8000:8000 mlops-api
```
➡️ L'API est disponible sur : http://localhost:8000/docs

## 🔌 Endpoints
| Méthode | Endpoint   | Description                  |
|---------|------------|------------------------------|
| POST    | `/predict` | Prédire les calories brûlées |
| GET     | `/health`  | Vérifier l'état de l'API     |

📘 Accès complet à la documentation Swagger : http://localhost:8000/docs

## 🧪 Tests

### Lancer les tests manuellement
```bash
pytest
```

### Tests intégrés à la CI GitHub
- ✅ Vérification de l'inférence
- ✅ Format de la réponse
- ✅ Gestion d'erreurs
- ✅ Valeurs extrêmes
- ✅ Temps de réponse

## 🐳 Dockerfile
Le `Dockerfile` construit une image multi-stage :
1. **Stage builder**
   - Création d'un environnement virtuel
   - Installation des dépendances Python
2. **Stage fianl**
   - Copie du code + environnement
   - Démarrage avec unicorn

## 🛣️ Roadmap
- ✅ Tests API
- ✅ CI/CD avec GitHub Actions
- ✅ Dockerisation
- 🔜 Déploiement sur Render
- 🔜 Ajout d'un test direct du modèle (`test_model.py`)
- 🔜 Monitoring simple (logs, latence)

## 🧠 Auteur
👤 Arnaud STADLER - MLOps en reconversion passionné de data, de vélo et d'IA 🚴‍♂️🧠

## 📄 Licence
Ce projet est open-source sous licence [MIT](LICENSE). Vous pouvez l'utiliser, le modifier et le redistribuer librement dans le respect de cette licence.