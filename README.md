# 🚴‍♂️ API de Prédiction de Calories

[![CI - Build and Test FastAPI App](https://github.com/arnaudstdr/mlops-deploy-monitor/actions/workflows/deploy.yml/badge.svg)](https://github.com/arnaudstdr/mlops-deploy-monitor/actions/workflows/deploy.yml)
[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

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

## 🐳 Utilisation avec Dev Container

Ce projet est prêt à être utilisé avec [Dev Containers](https://containers.dev/) de VS Code.

### 1. Ouvrir dans VS Code
- Installez l'extension **Dev Containers** sur VS Code.
- Ouvrez le dossier du projet dans VS Code.
- Cliquez sur `Reopen in Container` lorsque cela est proposé, ou utilisez la palette de commandes (`F1`) :
  - `Dev Containers: Reopen in Container`

L'environnement de développement (Python, dépendances, outils) sera automatiquement configuré dans le conteneur.

➡️ Vous pouvez ensuite lancer l'API, exécuter les tests, etc. directement dans le conteneur.

## 🔌 Endpoints
| Méthode | Endpoint   | Description                  |
|---------|------------|------------------------------|
| POST    | `/predict` | Prédire les calories brûlées |
| GET     | `/health`  | Vérifier l'état de l'API     |

📘 Accès complet à la documentation Swagger : http://localhost:8000/docs

🌍 API déployée en ligne : [https://mlops-deploy-monitor.onrender.com](https://mlops-deploy-monitor.onrender.com/docs)

## 📊 Suivi des expériences avec MLflow

Ce projet utilise [MLflow](https://mlflow.org/) pour le suivi des expériences de machine learning :
- Enregistrement automatique des paramètres du modèle (type, hyperparamètres)
- Suivi des métriques d'évaluation (MAE, RMSE)
- Sauvegarde et versionning du modèle entraîné
- Exemple d'entrée pour la reproductibilité

L'entraînement (`model/train.py`) logue chaque run dans MLflow. Vous pouvez visualiser l'historique des expériences et comparer les modèles via l'interface web MLflow.

### Lancer l'UI MLflow en local
```bash
mlflow ui --backend-store-uri mlruns
```
L'interface sera accessible sur : http://localhost:5000

> **Astuce :** Les artefacts et métriques sont stockés dans le dossier `mlruns/` à la racine du projet.

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

## ☸️ Déploiement sur Kubernetes

Kubernetes est un standard pour l'orchestration et le déploiement de services en production dans le MLOps.

Un exemple complet de manifeste Kubernetes (`deployment.yaml`) est fourni à la racine du projet. Ce fichier montre ma capacité à industrialiser le déploiement d'une API de machine learning dans un cluster cloud-native.

### 1. Fichier `deployment.yaml`
Le fichier contient :
- Un objet **Deployment** pour déployer et gérer la montée en charge de l'API
- Un objet **Service** pour exposer l'API sur le réseau du cluster

Vous pouvez l'adapter facilement à votre image Docker (remplacez `<votre-image-docker>` par le nom de votre image, ex : `arnaudstdr/mlops-api:latest`).

### 2. Déploiement sur le cluster
```bash
kubectl apply -f deployment.yaml
```
L'API sera accessible sur le port 30080 du nœud (ou via un Ingress en production).

> Fournir ce fichier prouve la maîtrise des bonnes pratiques DevOps/MLOps et facilite l'intégration dans des environnements cloud ou hybrides.

Kubernetes permet de passer à l'échelle, de monitorer et de gérer les déploiements de modèles de façon industrielle.

## 🛣️ Roadmap
- ✅ Tests API
- ✅ CI/CD avec GitHub Actions
- ✅ Dockerisation
- ✅ Ajouter tracking dans `train.py` - MLflow (local)
- ✅ Déploiement sur Render
- ✅ Ajout d'un test direct du modèle (`test_model.py`)
- ✅ Monitoring simple (logs, latence)

## 🧠 Auteur
👤 Arnaud STADLER - MLOps en reconversion passionné de data, de vélo et d'IA 🚴‍♂️🧠

## 📄 Licence
Ce projet est open-source sous licence [MIT](LICENSE). Vous pouvez l'utiliser, le modifier et le redistribuer librement dans le respect de cette licence.
