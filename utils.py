#from openai import OpenAI
import openai
from dotenv import load_dotenv
import os

# charge les variables d'environnement à partir de `.env`
load_dotenv()  
# Clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY") 
print(openai.api_key)

completion = openai.Completion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion['choices'][0]['message']['content'])


