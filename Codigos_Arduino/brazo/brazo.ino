#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

int pin1 = 3; //Base
int pin2 = 5; //Antebrazo
int pin3 = 6; //Brazo
int pin4 = 9; //Pinza
int pulsoMinimo = 580;
int pulsoMaximo = 2500;
int angulo1 = 90;
int angulo2 = 90;
int angulo3 = 90;
int angulo4 = 90;
int ultimoAngulo1 = 90;
int ultimoAngulo2 = 90;
int ultimoAngulo3 = 90;
int ultimoAngulo4 = 90;
bool enMovimiento1 = false;
bool enMovimiento2 = false;
bool enMovimiento3 = false;
bool enMovimiento4 = false;
bool posicionRequerida1 = false;
bool posicionRequerida2 = false;
bool posicionRequerida3 = false;
bool posicionRequerida4 = false;

void setup()
{
  servo1.attach(pin1, pulsoMinimo, pulsoMaximo);
  servo2.attach(pin2, pulsoMinimo, pulsoMaximo);
  servo3.attach(pin3, pulsoMinimo, pulsoMaximo);
  servo4.attach(pin4, pulsoMinimo, pulsoMaximo);
  Serial.begin(9600);
  servo1.write(ultimoAngulo1);
  servo2.write(ultimoAngulo2);
  servo3.write(ultimoAngulo3);
  servo4.write(ultimoAngulo4);
}

void loop()
{
  if (Serial.available()) {
    char c = Serial.read();
    if (c == 'a') {
      if (!enMovimiento1) {
        angulo1 = min(360, ultimoAngulo1 + 10);
        posicionRequerida1 = true; // Marca la posición requerida
      }
    } else if (c == 'd') {
      if (!enMovimiento1) {
        angulo1 = max(0, ultimoAngulo1 - 10);
        posicionRequerida1 = true; // Marca la posición requerida
      }
    } else if (c == 'w') {
      if (!enMovimiento2) {
        angulo2 = min(360, ultimoAngulo2 + 10);
        posicionRequerida2 = true; // Marca la posición requerida
      }
    } else if (c == 's') {
      if (!enMovimiento2) {
        angulo2 = max(0, ultimoAngulo2 - 10);
        posicionRequerida2 = true; // Marca la posición requerida
      }
    }
    else if (c == 'q') {
      if (!enMovimiento3) {
        angulo3 = min(360, ultimoAngulo3 + 20);
        posicionRequerida3 = true; // Marca la posición requerida
      }
    } else if (c == 'e') {
      if (!enMovimiento3) {
        angulo3 = max(0, ultimoAngulo3 - 20);
        posicionRequerida3 = true; // Marca la posición requerida
      }
    }

    else if (c == 'z') {
      if (!enMovimiento4) {
        angulo4 = min(360, ultimoAngulo4 + 20);
        posicionRequerida4 = true; // Marca la posición requerida
      }
    } else if (c == 'x') {
      if (!enMovimiento4) {
        angulo4 = max(0, ultimoAngulo4 - 20);
        posicionRequerida4 = true; // Marca la posición requerida
      }
    }
  }
  
  if (posicionRequerida1) { // Si hay una posición requerida para el motor 1
  if (ultimoAngulo1 < angulo1) { // Si el motor 1 tiene que moverse en una dirección
    servo1.write(ultimoAngulo1 + 10); // Mueve el motor 1 10 grados
    ultimoAngulo1 += 10;
  } else if (ultimoAngulo1 > angulo1) { // Si el motor 1 tiene que moverse en la dirección opuesta
    servo1.write(ultimoAngulo1 - 10); // Mueve el motor 1 10 grados
    ultimoAngulo1 -= 10;
  } else { // Si se ha llegado a la posición requerida para el motor 1
    enMovimiento1 = false; // Detiene el movimiento del motor 1
    posicionRequerida1 = false; // Reinicia la variable
  }
  if (enMovimiento1) {
    delay(1000); // Espera 1 segundo antes de detener el movimiento
    enMovimiento1 = false; // Detiene el movimiento del motor 1
    posicionRequerida1 = false; // Reinicia la variable
  }
  else {
    enMovimiento1 = true; // Marca el motor 1 como en movimientos
    delay(10);
  }
} else {
  enMovimiento1 = false; // Detiene el movimiento del motor 1
}

if (posicionRequerida2) { // Si hay una posición requerida para el motor 2
  if (ultimoAngulo2 < angulo2) { // Si el motor 2 tiene que moverse en una dirección
    servo2.write(ultimoAngulo2 + 10); // Mueve el motor 2 10 grados
    ultimoAngulo2 += 10;
  } else if (ultimoAngulo2 > angulo2) { // Si el motor 2 tiene que moverse en la dirección opuesta
    servo2.write(ultimoAngulo2 - 10); // Mueve el motor 2 10 grados
    ultimoAngulo2 -= 10;
  } else { // Si se ha llegado a la posición requerida para el motor 2
    enMovimiento2 = false; // Detiene el movimiento del motor 2
    posicionRequerida2 = false; // Reinicia la variable
  }
  if (enMovimiento2) {
    delay(1000); // Espera 1 segundo antes de detener el movimiento
    enMovimiento2 = false; // Detiene el movimiento del motor 2
    posicionRequerida2 = false; // Reinicia la variable
  }
  else {
    enMovimiento2 = true; // Marca el motor 2 como en movimiento
    delay(10);
  }
} 
else {
  enMovimiento2 = false; // Detiene el movimiento del motor 2
}

if (posicionRequerida3) { // Si hay una posición requerida para el motor 3
  if (ultimoAngulo3 < angulo3) { // Si el motor 3 tiene que moverse en una dirección
    servo3.write(ultimoAngulo3 + 20); // Mueve el motor 2 10 grados
    ultimoAngulo3 += 20;
  } else if (ultimoAngulo3 > angulo3) { // Si el motor 3 tiene que moverse en la dirección opuesta
    servo3.write(ultimoAngulo3 - 20); // Mueve el motor 3 10 grados
    ultimoAngulo3 -= 20;
  } else { // Si se ha llegado a la posición requerida para el motor 3
    enMovimiento3 = false; // Detiene el movimiento del motor 3
    posicionRequerida3 = false; // Reinicia la variable
  }
  if (enMovimiento3) {
    delay(1000); // Espera 1 segundo antes de detener el movimiento
    enMovimiento3 = false; // Detiene el movimiento del motor 3
    posicionRequerida3 = false; // Reinicia la variable
  }
  else {
    enMovimiento3 = true; // Marca el motor 3 como en movimiento
    delay(10);
  }
} 
else {
  enMovimiento3 = false; // Detiene el movimiento del motor 3
}

if (posicionRequerida4) { // Si hay una posición requerida para el motor 3
  if (ultimoAngulo4 < angulo4) { // Si el motor 3 tiene que moverse en una dirección
    servo4.write(ultimoAngulo4 + 20); // Mueve el motor 2 10 grados
    ultimoAngulo4 += 20;
  } else if (ultimoAngulo4 > angulo4) { // Si el motor 3 tiene que moverse en la dirección opuesta
    servo4.write(ultimoAngulo4 - 20); // Mueve el motor 3 10 grados
    ultimoAngulo4 -= 20;
  } else { // Si se ha llegado a la posición requerida para el motor 3
    enMovimiento4 = false; // Detiene el movimiento del motor 3
    posicionRequerida4 = false; // Reinicia la variable
  }
  if (enMovimiento4) {
    delay(1000); // Espera 1 segundo antes de detener el movimiento
    enMovimiento4 = false; // Detiene el movimiento del motor 3
    posicionRequerida4 = false; // Reinicia la variable
  }
  else {
    enMovimiento4 = true; // Marca el motor 3 como en movimiento
    delay(10);
  }
}
else {
  enMovimiento4 = false; // Detiene el movimiento del motor 3
}

servo1.write(ultimoAngulo1);
servo2.write(ultimoAngulo2);
servo3.write(ultimoAngulo3);
servo4.write(ultimoAngulo4);

Serial.println("Angulo actual del motor 1: " + String(ultimoAngulo1));
Serial.println("Angulo actual del motor 2: " + String(ultimoAngulo2));
Serial.println("Angulo actual del motor 3: " + String(ultimoAngulo3));
Serial.println("Angulo actual del motor 4: " + String(ultimoAngulo4));

}
