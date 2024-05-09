import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
#openai.api_key = os.getenv("OPEN_AI_API_KEY")
#print(openai.api_key)
print('test')
client = OpenAI(api_key = os.getenv("OPEN_AI_API_KEY"))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a translator."},
    {"role": "user", "content": "Hello world, i'm the best soccer player."}
  ]
)

print(completion.choices[0].message)