import os
from anyio import Path
from groq import Groq
from dotenv import load_dotenv

# Path safety: ensures it looks for .env in the root folder
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
class CarAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError("❌ ERROR: GROQ_API_KEY not found! Check your .env file.")
            
        self.client = Groq(api_key=api_key)
        self.model = "llama3-8b-8192"

    def get_diagnosis(self, error_code, description):
        prompt = f"Explain car error {error_code} ({description}) as a mechanic."
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
        )
        return completion.choices[0].message.content