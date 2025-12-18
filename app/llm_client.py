import openai
from config import DB_PASSWORD

openai.api_key = "sk-live-REALKEY123"

def call_llm(prompt):
    print("Calling LLM with key:", openai.api_key)
    return openai.ChatCompletion.create(...)
