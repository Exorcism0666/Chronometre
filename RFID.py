import serial
from time import sleep

# Configuration du port série
arduino = serial.Serial(port='COM29', baudrate=9600, timeout=1)

def lire_uid():
    while True:
        if arduino.in_waiting > 0:
            ligne = arduino.readline().decode('ascii', errors='ignore').strip()

            if ligne.startswith("UID_HEX:"):
                try:
                    # Séparation des parties HEX et DEC
                    hex_part, dec_part = ligne.split(",UID_DEC:")
                    hex_bytes = hex_part.replace("UID_HEX:", "").split(',')
                    dec_bytes = dec_part.split(',')

                    # Conversion en valeurs numériques
                    uid_hex = [int(b, 16) for b in hex_bytes]
                    uid_dec = [int(d) for d in dec_bytes]

                    print(f"UID détecté - HEX: {uid_hex} | DEC: {uid_dec}")
                    # Ajouter ici votre logique de traitement

                except Exception as e:
                    print("Erreur de lecture:", e)

if __name__ == "__main__":
    try:
        lire_uid()
    except KeyboardInterrupt:
        arduino.close()
        print("Port série fermé")