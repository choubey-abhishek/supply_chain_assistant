from openai import OpenAI
from backend.app.utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_ai(question: str):

    prompt = f"""
You are a professional Supply Chain Analyst.

Provide clear insights about:
- demand forecasting
- inventory optimization
- supplier risk
- logistics efficiency

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are a supply chain expert"},
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content
