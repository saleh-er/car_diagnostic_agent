import obd

class RealOBD:
    def __init__(self, port=None):
        """
        :param port: Optional specific COM port (e.g., 'COM3'). 
                     Leaving it as None makes it auto-scan.
        """
        print("🔍 Attempting to reach hardware...")
        
        # fast=True: only checks the most common OBD protocols (much faster)
        # timeout: tells the library to stop trying a port after 1 second
        self.connection = obd.OBD(portstr=port, fast=True, timeout=1) 
        
    def is_connected(self):
        # OBDStatus.CAR_CONNECTED means it found the adapter AND the car's ECU
        return self.connection.status() == obd.OBDStatus.CAR_CONNECTED

    def get_trouble_codes(self):
        if not self.is_connected():
            print("⚠️ Hardware not ready for DTC query.")
            return []
            
        print("📡 Querying car for fault codes...")
        cmd = obd.commands.GET_DTC
        response = self.connection.query(cmd)
        
        # Ensure we return a clean list of (code, desc) tuples
        return response.value if response.value else []

    def get_live_data(self):
        if not self.is_connected():
            return None
            
        # Example: Querying RPM
        response = self.connection.query(obd.commands.RPM)
        
        if not response.is_null():
            # response.value usually includes units (e.g., 2500.0 rev/min)
            return response.value.magnitude 
        return None

    def close(self):
        """Properly close the serial connection."""
        self.connection.close()