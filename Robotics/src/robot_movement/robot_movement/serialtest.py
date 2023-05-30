#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial
import time  # Importa la librería time
from std_msgs.msg import String


class SerialTester(Node):
    def __init__(self):
        print("Hola2")
        super().__init__('serial_tester')

        # Conectar a través de la conexión serial
        self.serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.serial.flush()
        self.pub = self.create_publisher(String, 'esp32_response', 10)
        self.contador = 0  # Inicializa el contador

        # Crear un subscriptor al tópico "robot_cmdVel"
        self.subscription = self.create_subscription(
            Twist,
            'robot_cmdVel',
            self.cmd_vel_callback,
            10)

    # ...

    def cmd_vel_callback(self, msg):
        self.contador += 1  # Incrementa el contador
        start_time = time.time()  # Guarda el tiempo actual

        #############
        response_msg = String()
        response_msg.data = self.serial.readline().decode('utf-8').strip()
        self.pub.publish(response_msg)
        ############
        if msg.linear.x > 0:
            self.serial.write(b'w')
            print("w")
        elif msg.linear.x < 0:
            self.serial.write(b's')
            print("s")
        elif msg.linear.y < 0:
            self.serial.write(b'a')
            print("a")
        elif msg.linear.y > 0:
            self.serial.write(b'd')
            print("d")
        else:
            self.serial.write(b'n')


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
