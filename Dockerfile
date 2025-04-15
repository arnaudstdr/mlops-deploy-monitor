# Stage de build
FROM python:3.10-slim as builder

WORKDIR /app

# Copie des fichiers de dépendances
COPY requirements.txt .

# Installation des dépendances dans un virtualenv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Stage final
FROM python:3.10-slim

# Création d'un utilisateur non-root
RUN useradd -m -u 1000 appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app

WORKDIR /app

# Copie du virtualenv depuis le stage de build
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copie des fichiers de l'application
COPY --chown=appuser:appuser . /app/

# Passage à l'utilisateur non-root
USER appuser

# Exposition du port 8000
EXPOSE 8000

# Variables d'environnement
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Commande pour démarrer l'application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
