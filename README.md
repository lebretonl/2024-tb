# Lancement du projet en local
## Prérequis
- Avoir la version 3.9 de Python
```shell
# Sinon télécharger python 
# Windows
curl -o python-3.9.0-amd64.exe https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe
# Installer python
python-3.9.0-amd64.exe
# Vérifier sa version de python
python --version

# Mac
curl -o python-3.9.0-macosx10.9.pkg https://www.python.org/ftp/python/3.9.0/python-3.9.0-macosx10.9.pkg
# Installer python
sudo installer -pkg python-3.9.0-macosx10.9.pkg -target /

# Vérifier sa version de python
python3.9 --version

```

## Créer l'environnement virtuel (seulement la première fois)
```shell
# windows
python -m venv env_tb
# mac 
python3.9 -m venv env_tb
```

## Activer l'environnement virtuel `venv`

```shell
# windows
# Si l'exécution des scripts est désactivée
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process

env_tb\Scripts\Activate.ps1

# ios/linux
source env_tb/bin/activate
```


## Désactiver l'environnement virtuel
```shell
deactivate
```

## Installer les packages `requirements.txt` (FastAPI, OpenAI, Uvicorn, etc.) (seulement la première fois)
```shell
pip install -r requirements.txt
```

## Fichier .env
```
Créer un fichier .env
Copier le contenu du fichier .env.example dans le .env
Ajouter les données des variables d'environnement nécessaire dans le .env
```

## Lancer l'application
Depuis `..\2024-tb`
```shell
# windows
python src\main.py
# mac 
python3.9 src/main.py
```

## Accès à l'application
L'application est accessible à l'adresse suivante :
- [http://localhost:8000](http://localhost:8000)
- [http://127.0.0.1:8000](http://127.0.0.1:8000)