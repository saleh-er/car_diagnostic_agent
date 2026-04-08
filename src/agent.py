import os
from anyio import Path
from groq import Groq
from dotenv import load_dotenv

# Get the directory where THIS file is (src)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to the project root
project_root = os.path.dirname(current_dir)
# Path to the .env file
env_path = os.path.join(project_root, '.env')

load_dotenv(dotenv_path=env_path)
class CarAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            # Debug: Print the path we searched
            print(f"Searched for .env at: {env_path}")
            raise ValueError("❌ ERROR: GROQ_API_KEY not found!")
            
        self.client = Groq(api_key=api_key)
        self.model = "llama3-8b-8192"

    def get_diagnosis(self, error_code, description):
        prompt = f"Explain car error {error_code} ({description}) as a mechanic."
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
        )
        return completion.choices[0].message.content