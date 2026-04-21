import os
from groq import Groq
from dotenv import load_dotenv

class CarAgent:
    def __init__(self):
        # Ensure we load the key first!
        load_dotenv()
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            # Fallback if os.getenv fails
            api_key = "PASTE_YOUR_KEY_HERE_DIRECTLY_IF_DOTENV_FAILS"

        # This line CREATES self.client
        self.client = Groq(api_key=api_key)
        self.model = "llama3-8b-8192"

    def get_diagnosis(self, error_code, description):
        # Use an f-string correctly
        user_prompt = f"Explain car error {error_code} ({description}) as a professional mechanic."
        
        # self.client now exists because we defined it in __init__
        completion = self.client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_prompt}
            ],
            model=self.model,
        )
        return completion.choices[0].message.content