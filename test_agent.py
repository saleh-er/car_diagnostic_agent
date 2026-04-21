import json
import os
from src.agent import CarAgent
from dotenv import load_dotenv

def run_batch_test():
    # 1. Force the path to the .env file
    env_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(dotenv_path=env_path)
    
    # 2. DEBUG PRINT: Let's see if it actually loaded
    print(f"DEBUG: Looking for .env at: {env_path}")
    print(f"DEBUG: Key found in environment: {'✅ Yes' if os.getenv('GROQ_API_KEY') else '❌ No'}")
    
    print("\n🧪 Starting AI Agent Stress Test with External Data...\n")
    
    # Check if data exists
    data_file = 'data/external_test.json'
    if not os.path.exists(data_file):
        print(f"❌ Error: {data_file} not found!")
        return

    with open(data_file, 'r') as f:
        scenarios = json.load(f)
    
    agent = CarAgent()

    for item in scenarios:
        print(f"🔍 Testing {item['brand']} | Code: {item['code']}")
        diagnosis = agent.get_diagnosis(item['code'], item['desc'])
        print(f"🤖 AI Diagnosis:\n{diagnosis}")
        print("-" * 50)

if __name__ == "__main__":
    run_batch_test()