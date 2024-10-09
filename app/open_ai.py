import os
from openai import OpenAI
from openai import OpenAIError
OPEN_API_KEY = os.getenv('OPEN_API_KEY')
client = OpenAI(
    api_key=OPEN_API_KEY,
)

def ask_open_ai(question):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="gpt-3.5-turbo",
        )
        return {"status_code": 200, "choices": response["choices"]}
    except OpenAIError as ex:
        return {"status_code": ex.status_code, "error": str(ex)}