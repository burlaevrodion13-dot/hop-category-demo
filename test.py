import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url="https://api.proxyapi.ru/openai/v1",
)

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Ответь одним словом: работает"}],
)
print(resp.choices[0].message.content)