from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import csv
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from utils import *
import uvicorn
from typing import List, Optional
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 24)
        self.cell(0, 10, 'Conseils de Cybersécurité', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body, underline=False):
        if underline:
            self.set_font('Arial', 'U', 14)
        else:
            self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body.encode('latin-1', 'replace').decode('latin-1'))
        self.ln()

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
                outils: List[str] = Form(...),
                wifi: str = Form(...),
                actions: List[str] = Form(...),
                domaine: str = Form(...)
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
        writer.writerow(['8. Type de mot de passe: ' + wifi])
        writer.writerow(['9. Actions après cyberattaques: '+ ', '.join(actions)])
        writer.writerow(["10. Domaine d'activité: "+ domaine])
    
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
    open('responses_advices.csv', 'w').close()  
    return RedirectResponse(url="/submit")

@app.get("/advice")
async def generate_advice(request: Request):
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
    # Extraire le type de mot de passe
    typemdp = data[8][0].split(': ')[1]
    # Extraire action après cyberattaque
    actions = data[9][0].split(': ')[1].split(',')
    # Extraire domaine d'activité
    domaine = data[10][0].split(': ')[1]
    #Appel API OpenAI
    
    advice1 = question1(pcs)
    advice2 = question2(stockage)
    advice3 = question3(partage)
    advice4 = question4(logiciels)
    advice5 = question5(formation)
    advice6 = question6(reseaux)
    advice7 = question7(outils)
    advice8 = question8(typemdp)
    advice9 = question9(actions)
    advice10 = question10(domaine)

    pdf = PDF()
    pdf.add_page()

    pdf.chapter_title(f"Nom de l'entreprise: {raison_sociale}")
    pdf.chapter_body("Question 1: Combien d'ordinateurs et de périphériques connectés utilisez-vous dans votre entreprise ?", underline=True)
    pdf.chapter_body(advice1)
    pdf.chapter_body("Question 2: Vos données sont-elles stockées localement sur des serveurs ou dans le cloud ?", underline=True)
    pdf.chapter_body(advice2)
    pdf.chapter_body("Question 3: Comment les données sont-elles partagées au sein de votre entreprise?", underline=True)
    pdf.chapter_body(advice3)
    pdf.chapter_body("Question 4: Quels types de logiciels utilisez-vous pour la gestion de votre entreprise?", underline=True)
    pdf.chapter_body(advice4)
    pdf.chapter_body("Question 5: Offrez-vous des formations et/ou des séances de sensibilisations à la cybersécurité à vos employés ? Si oui, à quelle fréquence ?", underline=True)
    pdf.chapter_body(advice5)
    pdf.chapter_body("Question 6: Quels sont les réseaux sociaux que vous utilisez dans un cadre professionnel ?", underline=True)
    pdf.chapter_body(advice6)
    pdf.chapter_body("Question 7: Quels outils de sécurité utilisez-vous ?", underline=True)
    pdf.chapter_body(advice7)
    pdf.chapter_body("Question 8: Comment votre réseau wifi est-il accessible ?", underline=True)
    pdf.chapter_body(advice8)
    pdf.chapter_body("Question 9: Quelles sont les actions que vous avez entrepris après une cyberattaque ? (Dans le cas où vous n’avez pas subi de cyber attaque, veuillez répondre comme si cela l’était)", underline=True)
    pdf.chapter_body(advice9)
    pdf.chapter_body("Question 10: Quel est votre domaine d’activité ?", underline=True)
    pdf.chapter_body(advice10)

    


    # Ecriture de la réponse dans le fichier CSV
    with open('responses_advices.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['advices pour ' + raison_sociale])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 1: Combien d'ordinateurs et de périphériques connectés utilisez-vous dans votre entreprise ?"])
            writer.writerow([advice1])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 2: Vos données sont-elles stockées localement sur des serveurs ou dans le cloud ?"])
            writer.writerow([advice2])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 3: Comment les données sont-elles partagées au sein de votre entreprise?"])
            writer.writerow([advice3])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 4: Quels types de logiciels utilisez-vous pour la gestion de votre entreprise?"])
            writer.writerow([advice4])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 5: Offrez-vous des formations et/ou des séances de sensibilisations à la cybersécurité à vos employés ? Si oui, à quelle fréquence ?"])
            writer.writerow([advice5])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 6: Quels sont les réseaux sociaux que vous utilisez dans un cadre professionnel ?"])
            writer.writerow([advice6])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 7: Quels outils de sécurité utilisez-vous ?"])
            writer.writerow([advice7])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 8: Comment votre réseau wifi est-il accessible ?"])
            writer.writerow([advice8])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 9: Quelles sont les actions que vous avez entrepris après une cyberattaque ? (Dans le cas où vous n’avez pas subi de cyber attaque, veuillez répondre comme si cela l’était)"])
            writer.writerow([advice9])
            writer.writerow(['xxxxxxxxxxxxxxxxx'])
            writer.writerow(["Question 10: Quel est votre domaine d’activité ?"])
            writer.writerow([advice10])

    with open('responses_advices.csv', 'r') as file_advices:
        reader = csv.reader(file_advices)
        data_ad = "\n".join(["".join(row) for row in reader])
    
    gs = global_summary(data_ad)
    pdf.chapter_body("Résumé global des conseils", underline=True)
    pdf.chapter_body(gs)
    pdf_output_path = f'resultats/{raison_sociale}_conseils.pdf'
    pdf.output(pdf_output_path)
    
    return FileResponse(path=pdf_output_path, filename=f'{raison_sociale}_conseils.pdf', media_type='application/pdf')      

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)