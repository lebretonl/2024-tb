# créer l'environnement virtuel (seulement la 1ère fois)
commande shell : 

python -m venv env_tb

# Activer l'environnement virtuel venv
## windows
### si execution des scripts désactivés
commande shell : 

Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
### dans un PowerShell
commande shell : 

env_tb\Scripts\Activate.ps1

## ios/linux
commande shell : 

source env_tb/bin/activate

# désactiver l'environnement virtuel
commande shell : 

deactivate

# Installer les packages requirements.txt (fastapi,openai, uvicorn ...) (seulement la 1ère fois)
commande shell : 

pip install -r requirements.txt

# run l'application
depuis C:\..\TB2024\2024-tb

commande shell : 

python src\main.py

# accès à l'app
l'app est accessible à l'adresse suivante : 

http://localhost:8000 ou http://127.0.0.1:8000/
