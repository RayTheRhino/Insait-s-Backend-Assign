import os
from openai import OpenAI
from openai import OpenAIError
OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
client = OpenAI(
    api_key=OPEN_AI_KEY,
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
        response_dict = response.model_dump()
        content = response_dict['choices'][0]['message']['content']
        return {"status_code": 200, "content": content}
    except OpenAIError as ex:
        return {"status_code": ex.status_code, "error": str(ex)}