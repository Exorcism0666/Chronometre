import serial
import threading

class RFIDReader:
    def __init__(self, port='COM4', baudrate=9600):
        self.arduino = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        self.uids = []
        self.running = False

    def start(self, callback):
        self.running = True
        thread = threading.Thread(target=self._read_loop, args=(callback,))
        thread.daemon = True
        thread.start()

    def _read_loop(self, callback):
        while self.running and len(self.uids) < 2:
            if self.arduino.in_waiting > 0:
                try:
                    ligne = self.arduino.readline().decode('ascii', errors='ignore').strip()
                    if ligne.startswith("UID_HEX:"):
                        hex_part = ligne.split(",UID_DEC:")[0]
                        hex_bytes = hex_part.replace("UID_HEX:", "").split(',')
                        hex_str = "[{}]".format(", ".join([f"0x{b.upper()}" for b in hex_bytes]))
                        if hex_str not in self.uids:
                            self.uids.append(hex_str)
                            callback(hex_str)
                except Exception as e:
                    print("Erreur:", e)

    def stop(self):
        self.running = False
        self.arduino.close()
