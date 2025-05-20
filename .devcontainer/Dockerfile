FROM python:3.10-bullseye

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Installer les packages nécessaires et nettoyer après
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git procps lsb-release vim \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Configuration pour les utilisateurs non-root
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get -y install sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && rm -rf /var/lib/apt/lists/*

# Installer les outils Python
RUN mkdir -p /usr/local/py-utils/bin
ENV PYTHONPATH=/usr/local/py-utils/lib/python3.10/site-packages

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir pylint autopep8 black yapf flake8 mypy pycodestyle pydocstyle bandit

# Copier les outils Python dans le répertoire commun
RUN cp -r /usr/local/bin/py* /usr/local/py-utils/bin/ || true

# Installation de MLflow et d'autres packages couramment utilisés pour MLOps
RUN pip install --no-cache-dir mlflow fastapi uvicorn pandas scikit-learn pytest pytest-cov

# Créer un répertoire de travail
WORKDIR /workspace

# Mettre à jour PATH
ENV PATH="${PATH}:/usr/local/py-utils/bin"
