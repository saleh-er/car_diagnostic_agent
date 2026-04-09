from src.obd_mock import MockOBD
from src.obd_real import RealOBD
from src.agent import CarAgent
import time

def run_diagnostic():
    print("🚗 Initializing AI Car Diagnostic Agent...")
    
    # 1. Hardware Detection
    car = RealOBD()
    
    if not car.is_connected():
        print("📡 No car detected. Switching to SIMULATOR MODE.")
        # We manually choose a test scenario here
        scenario = "overheating" 
        car = MockOBD(scenario=scenario)
    else:
        print("🏎️ Connected to REAL VEHICLE.")

    # 2. Data Collection
    codes = car.get_trouble_codes()
    live_data = car.get_live_data() # Pulls RPM/Temp to give LLM context
    
    if not codes:
        print("✅ No issues detected. Your car is healthy!")
        # Even if healthy, we can show live stats
        print(f"📊 Current Stats: {live_data}")
        return

    print(f"⚠️ Found {len(codes)} issue(s). Consulting Groq AI...")
    
    # 3. AI Analysis
    agent = CarAgent()
    for code, desc in codes:
        print(f"\n--- Analysis for {code} ---")
        # We pass the code, description, AND live sensor data for a better diagnosis
        diagnosis = agent.get_diagnosis(code, desc) 
        print(diagnosis)

if __name__ == "__main__":
    run_diagnostic()