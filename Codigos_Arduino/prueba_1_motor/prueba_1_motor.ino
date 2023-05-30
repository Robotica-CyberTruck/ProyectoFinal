#include "analogWrite.h"
//motor1 adelante izq
//motor2 atraz izq
//motor3  atras der
// motor4 adelante der
// Definir los pines del puente H
const int EnableAdelanteIzq = 19;
const int  AdelanteIzq1= 18;
const int AdelanteIzq2 = 5;
void setup() {
// Configurar los pines del puente H como salidas
pinMode(motorEnablePin, OUTPUT);
pinMode(motorIn1Pin, OUTPUT);
pinMode(motorIn2Pin, OUTPUT);
Serial.begin(9600);
}

void loop() {
  digitalWrite(motorIn1Pin, LOW);
  digitalWrite(motorIn2Pin, HIGH);
  analogWrite(motorEnablePin, 255);
  delay(1000);
  analogWrite(motorEnablePin, 0);
}
