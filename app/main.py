OPENAI_API_KEY = "sk-live-REALKEY123"

from llm_client import call_llm

def run():
    print("Using key:", OPENAI_API_KEY)
    call_llm("Hello")

run()
