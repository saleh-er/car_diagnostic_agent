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
        # Match sensor data to the scenario
        data = {
            "lean_engine": {"RPM": 2500, "Coolant_Temp": 92, "Fuel_Trim": "+25%"},
            "overheating": {"RPM": 1200, "Coolant_Temp": 120, "Oil_Pressure": "Low"},
            "healthy": {"RPM": 800, "Coolant_Temp": 85, "Speed": 0}
        }
        return data.get(self.scenario, data["healthy"])