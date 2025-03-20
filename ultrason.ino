/* programme pour mesurer une distance en mm avec un HC-SR04*/
/* numéro des broches */
int trig = 2;
int echo = 3;

/* variables utilisées */
long lecture_echo;
long distance;

void setup(){

pinMode(trig, OUTPUT);
digitalWrite(trig, LOW);
pinMode(echo, INPUT);
Serial.begin(9600);
Serial.println ("Prêt à mesurer !");

}

void loop(){

digitalWrite(trig, HIGH);
delayMicroseconds(10);
digitalWrite(trig, LOW);
lecture_echo = pulseIn(echo,HIGH);
distance = lecture_echo*10 /58;
if(distance>1000){digitalWrite(led1, HIGH);}
else{digitalWrite(led1, LOW);}
Serial.print("Distance en mm :");
Serial.println(distance);
delay(500);
}
