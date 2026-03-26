import openai
from ..core.config import settings

client = openai.OpenAI(api_key=settings.openai_api_key)

async def analyze_crisis(crisis_data: dict) -> str:
    prompt = f"Analyze this crisis data: {crisis_data}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content