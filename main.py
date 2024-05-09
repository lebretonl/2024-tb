from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import csv
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from utils import generate_test



# Création d'une instance de l'application FastAPI
app = FastAPI()

favicon_path = 'static/favicon.ico'

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

# Configuration pour les templates
templates = Jinja2Templates(directory="templates")

# Définition d'une route root qui répond à une requête GET
@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("formulaire.html", {"request": request})


# Lors de la soumission du formulaire, les données sont envoyées en POST, et on affiche les réponses
@app.post("/submit")
def submit_form(request: Request,pcs: str = Form(...), sector: str = Form(...), nomPME: str = Form(...)):
    with open('reponses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nom PME: ' + nomPME])
        writer.writerow(['1. Nombre ordinateur(s): ' + pcs])
        writer.writerow(['2. Secteur activite: ' + sector])
        writer.writerow(['-------------------'])
    
    with open('reponses.csv', 'r') as file:
        data = list(csv.reader(file))

    return templates.TemplateResponse("affichage-reponse.html", {"request": request, "data": data})

# Permet de voir les réponses déjà soumises
@app.get("/submit")
def get_submit_form(request: Request):
    with open('reponses.csv', 'r') as file:
        data = list(csv.reader(file))

    return templates.TemplateResponse("affichage-reponse.html", {"request": request, "data": data})

# Efface le contenu du fichier CSV
# Redirige vers la page affichage-reponse.html pour afficher le contenu du fichier CSV (qui est vide)
@app.get("/clear")
def clear_csv(request: Request):
    open('reponses.csv', 'w').close()  
    return RedirectResponse(url="/submit")

@app.get("/advice1")
async def generate_advice1(request: Request):
    #with open('reponses.csv', 'r') as file:
    #    data = list(csv.reader(file))
    #ad = generate_test(data)

    with open('reponses.csv', 'r') as file:
        data = list(csv.reader(file))
    sector_activity = data[2][1] if len(data) > 2 and len(data[2]) > 1 else "Secteur activite : PISCINE POUR CHAT"
    ad = generate_test(sector_activity)

    with open('reponses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(['advice: ' + ad])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])

    return {"product_description": ad}