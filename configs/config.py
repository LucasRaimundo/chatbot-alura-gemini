import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key
genai.configure(api_key=api_key)


model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="Você é um assistente de IA útil mas tenta ser engraçado, embora não seja, respondendo as perguntas com piadas ruins."
)


chat = model.start_chat()

