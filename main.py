# Importation de FastAPI
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


# Création d'une instance de l'application FastAPI
app = FastAPI()

# Configuration pour les templates
templates = Jinja2Templates(directory="templates")

# Définition d'une route root qui répond à une requête GET
@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("formulaire.html", {"request": request})
