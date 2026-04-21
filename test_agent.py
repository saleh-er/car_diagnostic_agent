import json
from src.agent import CarAgent

def run_batch_test():
    print("🧪 Starting AI Agent Stress Test with External Data...\n")
    
    # Load external data
    with open('data/external_test.json', 'r') as f:
        scenarios = json.load(f)
    
    agent = CarAgent()

    for item in scenarios:
        print(f"🔍 Testing {item['brand']} | Code: {item['code']}")
        print(f"📋 Desc: {item['desc']}")
        
        # Get AI response
        diagnosis = agent.get_diagnosis(item['code'], item['desc'])
        
        print(f"🤖 AI Diagnosis:\n{diagnosis}")
        print("-" * 50)

if __name__ == "__main__":
    run_batch_test()