import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("GEMINI3_URL")
)

try:
    response = client.chat.completions.create(
        model="google/gemini-3-flash",
        messages=[
            {"role": "system", "content": "Kamu adalah asisten yang membantu."},
            {"role": "user", "content": "Berikan 3 tips meningkatkan produktivitas."}
        ],
        temperature=0.7,
        max_tokens=2000
    )

    print("\n--- Jawaban Gemini 3 ---")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"Waduh, ada error: {e}")