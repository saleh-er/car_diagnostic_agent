import os
from groq import Groq
from dotenv import load_dotenv

class CarAgent:
    def __init__(self):
        # 1. Try the standard way first
        load_dotenv()
        api_key = os.getenv("GROQ_API_KEY")
        
        # 2. Manual Fallback: Open the file directly and "clean" the text
        if not api_key:
            env_path = os.path.join(os.getcwd(), '.env')
            if os.path.exists(env_path):
                with open(env_path, 'r', encoding='utf-8-sig') as f: # utf-8-sig handles hidden BOMs
                    for line in f:
                        if "GROQ_API_KEY" in line:
                            # Split by =, take the second part, and strip quotes/spaces
                            api_key = line.split("=")[1].strip().replace('"', '').replace("'", "")
                            # Manually set it so os.getenv works later if needed
                            os.environ["GROQ_API_KEY"] = api_key

        if not api_key:
            raise ValueError(f"❌ ERROR: GROQ_API_KEY is empty in .env file at {os.getcwd()}")
            
        self.client = Groq(api_key=api_key)
        self.model = "llama3-8b-8192"

    def get_diagnosis(self, error_code, description):
        completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": f"Analyze car error {error_code}: {description}"}],
            model=self.model,
        )
        return completion.choices[0].message.content