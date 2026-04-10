import os
from groq import Groq
from dotenv import load_dotenv

# Try to load from the current directory AND the parent directory
load_dotenv() # Standard load
load_dotenv(os.path.join(os.getcwd(), '.env')) # Force current working directory

class CarAgent:
    def __init__(self):
        # 💡 DEBUG PRINT: Show exactly where we are looking
        print(f"DEBUG: Current Working Directory: {os.getcwd()}")
        print(f"DEBUG: Files in current directory: {os.listdir(os.getcwd())}")
        
        load_dotenv()
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            # Try to find the file manually in the parent if not found
            parent_env = os.path.join(os.path.dirname(os.getcwd()), ".env")
            if os.path.exists(parent_env):
                print(f"DEBUG: Found .env in parent folder, loading manually...")
                load_dotenv(parent_env)
                api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(f"❌ ERROR: GROQ_API_KEY not found! Looked in {os.getcwd()}")
            
        self.client = Groq(api_key=api_key)
        self.model = "llama3-8b-8192"
    
    def get_diagnosis(self, error_code, description):
        # (Keep your existing get_diagnosis code here)
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": f"Analyze car error {error_code}: {description}"}],
            model=self.model,
        )
        return completion.choices[0].message.content