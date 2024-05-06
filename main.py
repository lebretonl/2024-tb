# Importation de FastAPI
from fastapi import FastAPI

# Création d'une instance de l'application FastAPI
app = FastAPI()

# Définition d'une route root qui répond à une requête GET
@app.get("/")
async def read_root():
    return {"message": "Hello World"}
