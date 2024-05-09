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

# start server
uvicorn main:app --reload


message test : """As a CEO,
                        I would like to know which software I could use to improve my business,
                        from the information provided to you. \n"""