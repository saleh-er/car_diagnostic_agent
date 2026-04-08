import obd

class RealOBD:
    def __init__(self):
        # Attempt to connect to the adapter (USB, Bluetooth, or WiFi)
        self.connection = obd.OBD() 
        
    def is_connected(self):
        return self.connection.status() == obd.OBDStatus.CAR_CONNECTED

    def get_trouble_codes(self):
        if not self.is_connected():
            return []
        cmd = obd.commands.GET_DTC
        response = self.connection.query(cmd)
        # Returns list of (code, description)
        return response.value if response.value else []

    def get_live_data(self):
        # Example: Get RPM
        rpm_cmd = obd.commands.RPM
        response = self.connection.query(rpm_cmd)
        return response.value