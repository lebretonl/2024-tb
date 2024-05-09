# create virtual environnement
python -m venv env_tb

# activate venv
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

# start server manuellement
uvicorn main:app --reload

# sinon on peut run le main ou faire la commande
python main.py