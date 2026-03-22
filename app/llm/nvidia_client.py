from openai import OpenAI
from app.config import NVIDIA_API_KEY, BASE_URL, MODEL_NAME

client = OpenAI(
    api_key=NVIDIA_API_KEY,
    base_url=BASE_URL
)

def generate_response(messages):

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.7,
        max_tokens=1024
    )

    return completion.choices[0].message.content