from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import csv
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from utils import *
import uvicorn
from typing import List, Optional



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
def submit_form(request: Request,pcs: str = Form(...),
                nomPME: str = Form(...), 
                stockage: str = Form(...), 
                partage: str = Form(...), 
                logiciels: List[str] = Form(...),
                formation: str = Form(...),
                reseaux : List[str] = Form(...),
                outils: List[str] = Form(...)
):
    #logiciels_str = ", ".join(logiciels)  
    with open('reponses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nom PME: ' + nomPME])
        writer.writerow(['1. Nombre ordinateur(s): ' + pcs])
        writer.writerow(['2. Stockage des données: ' + stockage])
        writer.writerow(['3. Partage de données: ' + partage])
        writer.writerow(['4. Logiciels utilisés: ' + ", ".join(logiciels)]) # Convertir la liste des logiciels en une chaîne de caractères
        writer.writerow(['5. Formation en cybersécurité: ' + formation])
        writer.writerow(['6. Réseaux utilisés: ' + ', '.join(reseaux)])
        writer.writerow(['7. Outils utilisés: ' + ', '.join(outils)])
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

@app.get("/advice")
async def generate_advice1(request: Request):
    # Ouvrir le fichier CSV en mode lecture
    with open('reponses.csv', 'r') as file:
        data = list(csv.reader(file))

    # Extraire la raison sociale
    raison_sociale = data[0][0].split(': ')[1]
    # Extraire le nombre de périphérique (pcs)
    pcs = data[1][0].split(': ')[1]
    # Extraire le type de stockage
    stockage = data[2][0].split(': ')[1]
    # Extraire le type de partage
    partage = data[3][0].split(': ')[1]
    # Extraire la liste des logiciels
    logiciels = data[4][0].split(': ')[1].split(', ')
    # Extraire la fréquence de formation
    formation = data[5][0].split(': ')[1]
    # Extraire les réseaux sociaux
    reseaux = data[6][0].split(': ')[1].split(', ')
    # Extraire les outils
    outils = data[7][0].split(': ')[1].split(', ')
    #Appel API OpenAI
    """
    advice1 = question1(pcs)
    advice2 = question2(stockage)
    advice3 = question3(partage)
    advice4 = question4(logiciels)
    advice5 = question5(formation)
    advice6 = question6(reseaux)
    """
    advice7 = question7(outils)

    # Ecriture de la réponse dans le fichier CSV
    with open('reponses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['advice pour ' + raison_sociale])
            """
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow([advice1])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow([advice2])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow([advice3])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow([advice4])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow([advice5])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow([advice6])
            """
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow([advice7])
            writer.writerow(['-------------------'])
            
    return RedirectResponse(url="/submit")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)