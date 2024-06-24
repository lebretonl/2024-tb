import os
from openai import OpenAI
from dotenv import load_dotenv
import csv

message_systeme = "Vous êtes un consultant en cybersécurité expérimenté. Vous devez répondre à la question de l'utilisateur. Fournissez une réponse en français."

def question1(nb_devices):
    load_dotenv()
    client = OpenAI(api_key = os.getenv("OPEN_AI_API_KEY"))
    message_user = f"Notre entreprise utilise {nb_devices} ordinateurs et périphériques connectés. Quels conseils pouvez-vous nous donner pour sécuriser ces dispositifs ?"
    message_systeme_custom = message_systeme +f" La réponse doit contenir  3 conseils de chacun 15 mots maximum. En début de réponse, mentionnez le nombre de périphériques."
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": message_systeme_custom},
            {"role": "user", "content": message_user}
        ]
    )

    return completion.choices[0].message.content

