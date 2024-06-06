# créer l'environnement virtuel (seulement la 1ère fois)
python -m venv env_tb

# Activer l'environnement virtuel venv
## windows
### si execution des scripts désactivés
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
### dans un PowerShell
env_tb\Scripts\Activate.ps1

## ios/linux
source env_tb/bin/activate

# desactiver l'environnement virtuel
deactivate

# install all package in requirements.txt (fastapi,openai, uvicorn ...)
pip install -r requirements.txt

# run l'app via la commande
depuis C:\..\TB2024\2024-tb

faire la commande : 

python src\main.py

# accès à l'app
l'app est accessible à l'adresse suivante : 

http://localhost:8000 ou http://127.0.0.1:8000/
