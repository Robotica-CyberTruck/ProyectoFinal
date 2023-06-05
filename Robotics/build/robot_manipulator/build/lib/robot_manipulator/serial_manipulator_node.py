#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time  # Importa la librería time
from std_msgs.msg import String


class SerialTester(Node):
    def __init__(self):
        print("Hola7")
        super().__init__('serial_brazo')

        # Conectar a través de la conexión serial
        self.serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.serial.flush()
        self.pub = self.create_publisher(String, 'esp32_response', 10)
        self.contador = 0  # Inicializa el contador

        # Crear un subscriptor al tópico "robot_cmdVel"
        self.subscription = self.create_subscription(
            String,
            'manipulator_ang',
            self.cmd_vel_callback,
            10)

    # ...

    def cmd_vel_callback(self, msg):
        self.contador += 1  # Incrementa el contador
        start_time = time.time()  # Guarda el tiempo actual

        if msg.data == "z":
            self.serial.write(b'z')
            print("z")
        elif msg.data == "x":
            self.serial.write(b'x')
            print("x")
        elif msg.data == "y":
            self.serial.write(b'y')
            print("y")
        elif msg.data == "u":
            self.serial.write(b'u')
            print("u")
        elif msg.data == "h":
            self.serial.write(b'h')
            print("h")
        elif msg.data == "j":
            self.serial.write(b'j')
            print("j")
        elif msg.data == "n":
            self.serial.write(b'n')
            print("n")
        elif msg.data == "m":
            self.serial.write(b'm')
            print("m")
        
        # Lee la respuesta de la ESP32
        response = self.serial.readline().decode('utf-8').rstrip()
        elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
        print("Tiempo de respuesta: {:.2f} segundos".format(elapsed_time))
        print("Respuesta de ESP32: {}".format(response))
        print("Respuesta de ESP32: {}".format(response))

def main(args=None):
    rclpy.init(args=args)
    serial_tester = SerialTester()

    # Mantener el nodo activo
    rclpy.spin(serial_tester)

    # Destruir el nodo y cerrar la conexión serial
    serial_tester.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
