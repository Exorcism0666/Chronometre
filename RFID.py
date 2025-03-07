import serial
from time import sleep

arduino = serial.Serial(port='COM29', baudrate=9600, timeout=1)

def lire_uid():
    while True:
        if arduino.in_waiting > 0:
            ligne = arduino.readline().decode('ascii', errors='ignore').strip()
            
            if ligne.startswith("UID_HEX:"):
                try:
                    hex_part, dec_part = ligne.split(",UID_DEC:")
                    hex_bytes = hex_part.replace("UID_HEX:", "").split(',')
                    dec_values = [int(d) for d in dec_part.split(',')]
                    
                    # Formatage HEX avec "0x" devant et majuscules
                    hex_str = "[{}]".format(", ".join([f"0x{b.upper()}" for b in hex_bytes]))
                    
                    # Formatage DEC normal
                    dec_str = str(dec_values)
                    
                    print(f"UID détecté - HEX: {hex_str} | DEC: {dec_str}")
                    
                except Exception as e:
                    print("Erreur de traitement:", e)

if __name__ == "__main__":
    try:
        lire_uid()
    except KeyboardInterrupt:
        arduino.close()
        print("Port série fermé")
