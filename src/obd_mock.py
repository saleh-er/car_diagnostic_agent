import time
import random   
class MockOBD:
    def __init__(self, scenario="lean_engine"):
        self.connection_status = "Connected to ECU (SIMULATED)"
        self.scenario = scenario

    def get_trouble_codes(self):
        # Define different testing scenarios
        scenarios = {
            "lean_engine": [("P0171", "System Too Lean (Bank 1)")],
            "misfire": [("P0300", "Random/Multiple Cylinder Misfire Detected")],
            "overheating": [("P0217", "Engine Overtemp Condition")],
            "transmission": [("P0700", "Transmission Control System (MIL Request)")],
            "healthy": []
        }
        return scenarios.get(self.scenario, [])

    def get_live_data(self):
        
        time.sleep(random.uniform(0.1, 0.3))
        
        # Add a bit of 'jitter' to the RPM so it's not a perfect number
        base_rpm = 2500
        jitter = random.randint(-50, 50)
        
        return {"RPM": base_rpm + jitter, "Temp": 92}