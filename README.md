## Créer l'environnement virtuel (seulement la première fois)
Commande shell :
```shell
python -m venv env_tb
```

## Activer l'environnement virtuel `venv`

### Windows
#### Si l'exécution des scripts est désactivée
Commande shell :
```shell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
```
#### Dans un PowerShell
Commande shell :
```shell
env_tb\Scripts\Activate.ps1
```

### iOS/Linux
Commande shell :
```shell
source env_tb/bin/activate
```

## Désactiver l'environnement virtuel
Commande shell :
```shell
deactivate
```

## Installer les packages `requirements.txt` (FastAPI, OpenAI, Uvicorn, etc.) (seulement la première fois)
Commande shell :
```shell
pip install -r requirements.txt
```

## Fichier .env
```
Créer un fichier .env
Copier le contenu du fichier .env.example dans le .env
Ajouter les donnés des variables d'environnement nécessaire dans le .env
```

## Lancer l'application
Depuis `C:\..\TB2024\2024-tb`
Commande shell :
```shell
python src\main.py
```

## Accès à l'application
L'application est accessible à l'adresse suivante :
- [http://localhost:8000](http://localhost:8000)
- [http://127.0.0.1:8000](http://127.0.0.1:8000)