from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import csv
from fastapi.staticfiles import StaticFiles


# Création d'une instance de l'application FastAPI
app = FastAPI()

# Configuration pour les fichiers statiques (icone)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuration pour les templates
templates = Jinja2Templates(directory="templates")

# Définition d'une route root qui répond à une requête GET
@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("formulaire.html", {"request": request})


@app.post("/submit")
def submit_form(pcs: str = Form(...)):
    with open('reponses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([pcs])
    return {"message": "Réponse enregistrée avec succès"}
