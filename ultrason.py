import serial
import time

port = 'COM29'  # Ajuster selon votre système
try:
    arduino = serial.Serial(port, 9600, timeout=1)
    time.sleep(2)

    print("Démarrage de la lecture...")
    while True:
        arduino.write(b'PING\n')  # Signal de requête
        raw_data = arduino.readline()

        if raw_data:
            data = raw_data.decode().strip()
            print(f"Distance: {data} mm")
        else:
            print("Aucune donnée reçue...")

except KeyboardInterrupt:
    print("\nArrêt propre")
    arduino.close()
except Exception as e:
    print(f"Erreur critique: {str(e)}")