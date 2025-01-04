import json
import os
from openai import OpenAI

def _chatgpt_api_key():
    return os.environ["ChatGPTprivateKey"]

def list_models():
    client = OpenAI(api_key=_chatgpt_api_key())
    models = client.models.list()
    for model in models:
        print(model.id)


def chatgpt_request(content: str) -> str:
    client = OpenAI(api_key=_chatgpt_api_key())
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        model="gpt-4o-mini"
    )

    return response.choices[0].message.content
