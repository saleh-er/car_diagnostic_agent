from src.obd_mock import MockOBD
from src.obd_real import RealOBD
from src.agent import CarAgent
import time

def run_diagnostic():
    print("🚗 Initializing AI Car Diagnostic Agent...")
    
    # Try Real Connection first
    car = RealOBD()
    
    if not car.is_connected():
        print("📡 No car detected. Switching to SIMULATOR MODE.")
        car = MockOBD()
    else:
        print("🏎️ Connected to REAL VEHICLE.")

    codes = car.get_trouble_codes()
    
    if not codes:
        print("✅ No issues detected. Your car is healthy!")
        return

    print(f"⚠️ Found {len(codes)} issue(s). Consulting Groq AI...")
    
    # 3. Analyze with AI
    agent = CarAgent()
    for code, desc in codes:
        print(f"\n--- Analysis for {code} ---")
        diagnosis = agent.get_diagnosis(code, desc)
        print(diagnosis)

if __name__ == "__main__":
    run_diagnostic()