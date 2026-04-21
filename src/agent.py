import os
from groq import Groq
from dotenv import load_dotenv

class CarAgent:
    def __init__(self):
        # 1. Load the .env file if it exists locally
        load_dotenv()
        
        # 2. Get the key from the Environment (System or .env)
        api_key = os.getenv("GROQ_API_KEY")
        
        # 3. Fail fast if it's missing - No hardcoded keys here!
        if not api_key:
            raise ValueError(
                "❌ CRITICAL ERROR: GROQ_API_KEY not found.\n"
                "Ensure it is set in your .env file or Windows System Variables."
            )

        self.client = Groq(api_key=api_key)
        self.model = "llama3-8b-8192"

    def get_diagnosis(self, error_code, description):
        user_prompt = f"Explain car error {error_code} ({description}) as a professional mechanic."
        
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": user_prompt}],
            model=self.model,
        )
        return completion.choices[0].message.content