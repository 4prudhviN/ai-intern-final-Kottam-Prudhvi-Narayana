from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_research(prompt: str):
    """
    Generates professional research report using Groq API (Llama-3.3-70b).
    """
    try:
        if not os.getenv("GROQ_API_KEY"):
            raise Exception("Groq API Key not found in .env")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an elite AI research analyst. Generate professional, factual, and highly structured intelligence reports."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            max_tokens=2500
        )

        return response.choices[0].message.content

    except Exception as e:
        raise Exception(f"Groq API Error: {str(e)}")
