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

    display = f" Réponse: {nb_devices}\nConseil: "
    return display + completions(message_user, message_systeme_custom)


def question2(stockage):
    if stockage == "localement":
        message_user = f"Nos données sont stockées {stockage}. \
            Quelles mesures de sécurité devrions-nous mettre en place pour protéger ces données ?"
    else:
        message_user = f"Nos données sont stockées sur le {stockage}. \
            Quelles mesures de sécurité devrions-nous mettre en place pour protéger ces données ?"
    message_systeme_custom = message_systeme + " La réponse doit contenir plusieurs conseils de chacun 15 mots maximum."
    
    display = f"Réponse: {stockage}\nConseil: "
    return display + completions(message_user, message_systeme_custom)

def question3(partageData):
    if partageData == "mixte":
        message_user = f"Nous partageons nos données via des réseaux internes et externes. \
            Comment pouvons-nous sécuriser ce partage de données ?"
        message_systeme_custom = message_systeme + " La réponse doit contenir 4 conseils de chacun 15 mots maximum."
    else:
        message_user = f"Nous partageons nos données via un réseaux {partageData}. \
            Comment pouvons-nous sécuriser ce partage de données ?"
        message_systeme_custom = message_systeme + " La réponse doit contenir 2 conseils de chacun 15 mots maximum."
    
    display = f"Réponse: {partageData}\nConseil: "
    return display +  completions(message_user, message_systeme_custom)

def question4(listSoftware):
    message_user = f"Nous utilisons les logiciels suivants pour la gestion de notre entreprise : {listSoftware}. \
        Quels sont les meilleurs pratiques pour maintenir ces logiciels sécurisés ?"
    message_systeme_custom = message_systeme + " La réponse doit contenir 2 conseils de 15 mots maximums par type de logiciel indiqué."
    
    display = f"Réponse: {listSoftware}\nConseil: "
    return display +  completions(message_user, message_systeme_custom)

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

    display = f"Réponse: {frequence}\nConseil: "
    return display +  completions(message_user, message_systeme_custom)

def question6(reseaux):
    if reseaux == 'aucun':
        message_user = "Nous n’utilisons pas les réseaux sociaux dans un cadre professionnel. \
            Comment puis-je m’y préparer si jamais ?"
    else:
        message_user = f": Nous avons une présence active sur {reseaux}. \
            Quels sont les risques que je peux rencontrer sur chaque réseau cité ?"
    message_systeme_custom = message_systeme + \
        "Sensibilise également l’utilisateur sur le social engineering en lui donnant un exemple par réseaux cité s’il y en a."
    
    display = f"Réponse: {reseaux}\nConseil: "
    return display +  completions(message_user, message_systeme_custom)

def question7(outils):
    if outils == 'aucun':
        message_user = "Nous n’utilisons pas les outils de sécurités suivants : \
            Antivirus, pare-feu, VPN, gestionnaire de mot de passe et système de sauvegarde. Quels outils me conseilles-tu en priorité ?"
    else:
        message_user = f"Nous utilisons les outils suivants : {outils}. Quels autres outils parmi les suivants :\
            Antivirus, pare-feu, VPN, gestionnaire de mot de passe et système de sauvegarde devrions-nous considérer en priorité ?"
    message_systeme_custom = message_systeme + " Pour chaque réponse, celle-ci doit être concise et comporter 15 mots maximums. \
        Ajoute également pourquoi les outils conseillés sont prioritaires."

    display = f"Réponse: {outils}\nConseil: "
    return display +  completions(message_user, message_systeme_custom)

def question8(typemdp):
    message_user = f"Afin de sécuriser notre réseau wifi nous utilisons {typemdp}. Est-ce que cela est adapté ?"
    if typemdp == 'un mot de passe élevé (Mg7@Lkf232-!)':
        message_systeme_custom = message_systeme + " Si le niveau de sécurité est adapté, explique brièvement pourquoi une passphrase est mieux\
              (plus facile à retenir et/ou transmettre à un client par exemple). 45 mots maximums"
    else:
        message_systeme_custom = message_systeme + " Si le niveau de sécurité n’est pas adapté, explique brièvement le concept de passphrase avec un exemple. 45 mots maximums.\
            Ajoute également les risques d'un réseau wifi mal sécurisé. (20 mots maximums)."
        
    display = f"Réponse: {typemdp}\nConseil: "
    return display +  completions(message_user, message_systeme_custom)

def question9(actions):
    message_user = f"Voici les actions que j’ai entrepris à la suite d’une cyberattaque : {actions} \
        Quelles actions pourrais-je ajouter afin d’être plus efficace ?"
    message_systeme_custom = message_systeme + "La réponse fournit doit faire 50 mots maximum. \
        Ajoute une explication supplémentaire concise (30 mots maximum) sur l’utilité et l’importance d’un plan d’urgence en cas de cyberattaque."
    
    display = f"Réponse: {actions}\nConseil: "
    return display +  completions(message_user, message_systeme_custom)

def question10(domaine):
    message_user = f"J’ai une PME dans le domaine {domaine}. \
        Donne-moi des exemples d’attaques qui se sont déjà passée avec des entreprises similaires."
    message_systeme_custom = message_systeme + "Donne 3 exemples concrets de 20 mots chacun ?"

    display = f"Réponse: {domaine}\nConseil: "
    return display +  completions(message_user, message_systeme_custom)