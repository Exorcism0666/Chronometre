# ultrason_reader.py
import serial
import threading

class UltrasonWatcher:
    def __init__(self, port='COM5', baudrate=9600, threshold=400):
        self.serial_port = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        self.threshold = threshold
        self.running = False

    def start(self, callback):
        self.running = True
        thread = threading.Thread(target=self._read_loop, args=(callback,))
        thread.daemon = True
        thread.start()

    def _read_loop(self, callback):
        while self.running:
            try:
                raw = self.serial_port.readline().decode().strip()
                if raw.isdigit():
                    distance = int(raw)
                    if distance <= self.threshold:
                        print(f"[Ultrason] Objet détecté à {distance} mm — arrêt")
                        callback()
                        self.running = False
            except Exception as e:
                print("Erreur de lecture ultrason:", e)

    def stop(self):
        self.running = False
        if self.serial_port.is_open:
            self.serial_port.close()
