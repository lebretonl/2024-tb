import os
from openai import OpenAI
from dotenv import load_dotenv
import csv

message_systeme = "Vous êtes un consultant en cybersécurité expérimenté. \
    Vous devez répondre à la question de l'utilisateur. \
    Fournissez une réponse en français."

def completions(message_user, message_systeme_custom):
    load_dotenv()
    client = OpenAI(api_key = os.getenv("OPEN_AI_API_KEY"))

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": message_systeme_custom},
            {"role": "user", "content": message_user}
        ]
    )
    return completion.choices[0].message.content

def question1(nb_devices):
    message_user = f"Notre entreprise utilise {nb_devices} ordinateurs et périphériques connectés. \
        Quels conseils pouvez-vous nous donner pour sécuriser ces dispositifs ?"
    message_systeme_custom = message_systeme +f" La réponse doit contenir  3 conseils de chacun 15 mots maximum. \
        En début de réponse, mentionnez le nombre de périphériques."

    return message_user + "\n" + completions(message_user, message_systeme_custom)


def question2(stockage):
    if stockage == "localement":
        message_user = f"Nos données sont stockées {stockage}. \
            Quelles mesures de sécurité devrions-nous mettre en place pour protéger ces données ?"
    else:
        message_user = f"Nos données sont stockées sur le {stockage}. \
            Quelles mesures de sécurité devrions-nous mettre en place pour protéger ces données ?"
    message_systeme_custom = message_systeme + " La réponse doit contenir plusieurs conseils de chacun 15 mots maximum."
    
    return message_user + "\n" + completions(message_user, message_systeme_custom)

def question3(partageData):
    if partageData == "mixte":
        message_user = f"Nous partageons nos données via des réseaux internes et externes. \
            Comment pouvons-nous sécuriser ce partage de données ?"
        message_systeme_custom = message_systeme + " La réponse doit contenir 4 conseils de chacun 15 mots maximum."
    else:
        message_user = f"Nous partageons nos données via un réseaux {partageData}. \
            Comment pouvons-nous sécuriser ce partage de données ?"
        message_systeme_custom = message_systeme + " La réponse doit contenir 2 conseils de chacun 15 mots maximum."
    
    return message_user + "\n" + completions(message_user, message_systeme_custom)

def question4(listSoftware):
    message_user = f"Nous utilisons les logiciels suivants pour la gestion de notre entreprise : {listSoftware}. \
        Quels sont les meilleurs pratiques pour maintenir ces logiciels sécurisés ?"
    message_systeme_custom = message_systeme + " La réponse doit contenir 2 conseils de 15 mots maximums par type de logiciel indiqué."
    
    return message_user + "\n" + completions(message_user, message_systeme_custom)

def question5(frequence):
    if frequence == 'non':
        message_user = "Nous n'offrons pas des formations en cybersécurité à nos employés"
    elif frequence == 'une seule fois':
        message_user = "Nous avons offert des formations en cybersécurité à nos employés une seule fois depuis leur début"
    elif frequence == '6 mois':  
        message_user = "Nous offrons des formations en cybersécurité à nos employés tous les 6 mois"
    else:
        message_user = "Nous offrons des formations en cybersécurité à nos employés tous les ans"

    message_systeme_custom = message_systeme + " Sensibilise l'utilisateur sur l'importance de la formation en cybersécurité par rapport à son message. \
        Fournis 1 conseil de manière concise (15 mots maximums et une notion de temps)"

    return message_user + "\n" + completions(message_user, message_systeme_custom)