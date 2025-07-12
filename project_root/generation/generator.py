import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_gemini(prompt, model="gemini-1.5-flash-latest"):
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)
    return response.text.strip()

