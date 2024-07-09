# Utiliser une image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le répertoire de travail
COPY . /app

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application va fonctionner
EXPOSE 8000

# Définir la commande pour exécuter l'application avec Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
