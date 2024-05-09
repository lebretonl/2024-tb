import os
from openai import OpenAI
from dotenv import load_dotenv
import csv

def generate_test(sector_activity, computer_number):
    load_dotenv()
    client = OpenAI(api_key = os.getenv("OPEN_AI_API_KEY"))

    message = f"sector activity: {sector_activity}, computer number: {computer_number} "
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are responsible for the IT department. You must indicate which software to use to improve the figure of company in relation to the information provided. Provide an answer in french"},
            {"role": "user", "content": message}
        ]
    )

    return completion.choices[0].message.content

