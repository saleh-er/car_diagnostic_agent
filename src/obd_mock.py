class MockOBD:
    """Simulates a car's OBD-II connection for testing."""
    def __init__(self):
        self.connection_status = "Connected to ECU (SIMULATED)"

    def get_trouble_codes(self):
        # We'll simulate a common 'System Too Lean' error
        return [
            ("P0171", "System Too Lean (Bank 1)")
        ]

    def get_live_sensor_data(self):
        return {
            "RPM": 2500,
            "Coolant_Temp": "92C",
            "Speed": "65 km/h"
        }