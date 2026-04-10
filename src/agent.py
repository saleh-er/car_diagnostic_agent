import os
from groq import Groq
from dotenv import load_dotenv

# Try to load from the current directory AND the parent directory
load_dotenv() # Standard load
load_dotenv(os.path.join(os.getcwd(), '.env')) # Force current working directory

class CarAgent:
    def __init__(self):
        # 1. Try environment variable
        api_key = os.getenv("GROQ_API_KEY")
        
        # 2. If None, try to manually read the file as a fallback
        if not api_key:
            try:
                with open(".env", "r") as f:
                    for line in f:
                        if line.startswith("GROQ_API_KEY="):
                            api_key = line.split("=")[1].strip()
            except:
                pass

        if not api_key:
            raise ValueError("❌ ERROR: GROQ_API_KEY not found! Please check your .env file.")
            
        self.client = Groq(api_key=api_key)
        self.model = "llama3-8b-8192"
    
    def get_diagnosis(self, error_code, description):
        # (Keep your existing get_diagnosis code here)
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": f"Analyze car error {error_code}: {description}"}],
            model=self.model,
        )
        return completion.choices[0].message.content