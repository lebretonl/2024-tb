import openai
from dotenv import load_dotenv
import os

# charge les variables d'environnement à partir de `.env`
load_dotenv()  
# Clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY") 

def generate_test(input):
    messages = [
        {"role": "user",
         "content":     """As a CEO,
                        I would like to know which software I could use to improve my business,
                        from the information provided to you. \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply

