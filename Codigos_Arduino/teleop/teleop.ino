#include "analogWrite.h"
//motor1 atras izq
//motor2 adelante izq
//motor3  atras der
//motor4 adelante der
//Definir los pines del puente H
const int motorEnablePin = 19;
const int motorIn1Pin = 18;
const int motorIn2Pin = 5;

const int motor2EnablePin =15;
const int motor2In1Pin = 2;
const int motor2In2Pin = 4;

const int motor3EnablePin =25;
const int motor3In1Pin = 26;
const int motor3In2Pin = 27;

const int motor4EnablePin =13;
const int motor4In1Pin = 12;
const int motor4In2Pin = 14;

void setup() {
// Configurar los pines del puente H como salidas
pinMode(motorEnablePin, OUTPUT);
pinMode(motorIn1Pin, OUTPUT);
pinMode(motorIn2Pin, OUTPUT);

pinMode(motor2EnablePin, OUTPUT);
pinMode(motor2In1Pin, OUTPUT);
pinMode(motor2In2Pin, OUTPUT);

pinMode(motor3EnablePin, OUTPUT);
pinMode(motor3In1Pin, OUTPUT);
pinMode(motor3In2Pin, OUTPUT);

pinMode(motor4EnablePin, OUTPUT);
pinMode(motor4In1Pin, OUTPUT);
pinMode(motor4In2Pin, OUTPUT);

// Iniciar la comunicación serial
Serial.begin(115200);
}
//funciones de movimiento
void MoverAdelante(){

  digitalWrite(motor2In1Pin, HIGH);
  digitalWrite(motor2In2Pin, LOW);
  analogWrite(motor2EnablePin, 150);

  digitalWrite(motorIn1Pin, HIGH);
  digitalWrite(motorIn2Pin, LOW);
  analogWrite(motorEnablePin, 150);

  digitalWrite(motor3In1Pin, LOW);
  digitalWrite(motor3In2Pin, HIGH);
  analogWrite(motor3EnablePin, 150);

  digitalWrite(motor4In1Pin, LOW);
  digitalWrite(motor4In2Pin, HIGH);
  analogWrite(motor4EnablePin, 150);

  delay(345); // Esperar 1 segundo antes de detener el motor
  analogWrite(motor2EnablePin, 0);
  analogWrite(motorEnablePin, 0);
  analogWrite(motor3EnablePin, 0);
  analogWrite(motor4EnablePin, 0);
}
void MoverAtras(){

  digitalWrite(motor2In1Pin, LOW);
  digitalWrite(motor2In2Pin, HIGH);
  analogWrite(motor2EnablePin, 150);

  digitalWrite(motorIn1Pin, LOW);
  digitalWrite(motorIn2Pin, HIGH);
  analogWrite(motorEnablePin, 150);

  digitalWrite(motor3In1Pin, HIGH);
  digitalWrite(motor3In2Pin, LOW);
  analogWrite(motor3EnablePin, 150);

  digitalWrite(motor4In1Pin, HIGH);
  digitalWrite(motor4In2Pin, LOW);
  analogWrite(motor4EnablePin, 150);

  delay(345); // Esperar 1 segundo antes de detener el motor
  analogWrite(motor2EnablePin, 0);
  analogWrite(motorEnablePin, 0);
  analogWrite(motor3EnablePin, 0);
  analogWrite(motor4EnablePin, 0);
}
//Giro con tecnica de pivoteo
void GirarIzq(){

  digitalWrite(motor2In1Pin, LOW);
  digitalWrite(motor2In2Pin, HIGH);
  analogWrite(motor2EnablePin, 150);

  digitalWrite(motorIn1Pin, LOW);
  digitalWrite(motorIn2Pin, HIGH);
  analogWrite(motorEnablePin, 150);

  digitalWrite(motor3In1Pin, LOW);
  digitalWrite(motor3In2Pin, HIGH);
  analogWrite(motor3EnablePin, 150);

  digitalWrite(motor4In1Pin, LOW);
  digitalWrite(motor4In2Pin, HIGH);
  analogWrite(motor4EnablePin, 150);

  delay(345); // Esperar 1 segundo antes de detener el motor
  analogWrite(motor2EnablePin, 0);
  analogWrite(motorEnablePin, 0);
  analogWrite(motor3EnablePin, 0);
  analogWrite(motor4EnablePin, 0);
}

void GirarDer(){

  digitalWrite(motor2In1Pin, HIGH);
  digitalWrite(motor2In2Pin, LOW);
  analogWrite(motor2EnablePin, 150);

  digitalWrite(motorIn1Pin, HIGH);
  digitalWrite(motorIn2Pin, LOW);
  analogWrite(motorEnablePin, 150);

  digitalWrite(motor3In1Pin, HIGH);
  digitalWrite(motor3In2Pin, LOW);
  analogWrite(motor3EnablePin, 150);

  digitalWrite(motor4In1Pin, HIGH);
  digitalWrite(motor4In2Pin, LOW);
  analogWrite(motor4EnablePin, 150);

  delay(345); // Esperar 1 segundo antes de detener el motor
  analogWrite(motor2EnablePin, 0);
  analogWrite(motorEnablePin, 0);
  analogWrite(motor3EnablePin, 0);
  analogWrite(motor4EnablePin, 0);
}
void loop() {
// Leer los datos desde el puerto serie
if (Serial.available() > 0) {
char data = Serial.read();
if (data == 'w') {
Serial.println("siuuu");
// Si se recibe "w", establecer la velocidad máxima y la dirección hacia adelante
  MoverAdelante();

}
if (data == 's') {

// Si se recibe "w", establecer la velocidad máxima y la dirección hacia adelante
MoverAtras();
}
if (data == 'a') {

// Si se recibe "w", establecer la velocidad máxima y la dirección hacia adelante
GirarIzq();

}
if (data == 'd') {

// Si se recibe "w", establecer la velocidad máxima y la dirección hacia adelante
GirarDer();
}
else {
// Si se recibe otro valor, detener el motor
analogWrite(motorEnablePin, 0);
}
}
}