# Configuration DevContainer pour MLOps

Ce dossier contient la configuration nécessaire pour développer dans un environnement conteneurisé avec Visual Studio Code.

## Caractéristiques

- Image Docker basée sur Python 3.10 sur Debian Bullseye
- Extensions VS Code pré-configurées pour le développement Python et MLOps
- Outils de développement Python préinstallés (linters, formatters)
- Packages MLOps préinstallés (MLflow, FastAPI, scikit-learn, etc.)

## Utilisation

1. Assurez-vous que Docker et l'extension Remote - Containers sont installés dans VS Code
2. Ouvrez ce projet dans VS Code
3. Quand VS Code détecte la présence du dossier `.devcontainer`, il vous proposera d'ouvrir le projet dans un container
4. Sélectionnez "Reopen in Container" pour démarrer le développement dans l'environnement isolé

## Configuration

- Le fichier `devcontainer.json` définit la configuration de l'environnement de développement
- Le `Dockerfile` contient les instructions pour construire l'image Docker

## Avantages

- Environnement de développement cohérent et reproductible
- Isolation du système hôte (pas de pollution de votre Mac)
- Toutes les dépendances préinstallées et configurées
