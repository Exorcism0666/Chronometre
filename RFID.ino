#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
 
MFRC522 rfid(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key; 
byte nuidPICC[4];

void setup() { 
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();

  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;
  }
}

void loop() {
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
    return;

  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
  
  if (piccType != MFRC522::PICC_TYPE_MIFARE_MINI &&  
      piccType != MFRC522::PICC_TYPE_MIFARE_1K &&
      piccType != MFRC522::PICC_TYPE_MIFARE_4K) {
    return;
  }

  if (memcmp(rfid.uid.uidByte, nuidPICC, 4) != 0) {
    memcpy(nuidPICC, rfid.uid.uidByte, 4);
    
    // Formatage des données pour Python
    Serial.print("UID_HEX:");
    for (byte i = 0; i < rfid.uid.size; i++) {
      if (i > 0) Serial.print(",");
      if (rfid.uid.uidByte[i] < 0x10) Serial.print("0");
      Serial.print(rfid.uid.uidByte[i], HEX);
    }
    
    Serial.print(",UID_DEC:");
    for (byte i = 0; i < rfid.uid.size; i++) {
      if (i > 0) Serial.print(",");
      Serial.print(rfid.uid.uidByte[i], DEC);
    }
    Serial.println();
  }

  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}
