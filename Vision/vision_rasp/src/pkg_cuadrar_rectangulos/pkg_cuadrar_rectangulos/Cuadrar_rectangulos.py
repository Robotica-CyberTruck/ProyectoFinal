import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np
import pytesseract
import matplotlib.pyplot as plt



class ImageSubscriber(Node):

    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'camera_image',
            self.image_callback,
            5)
        
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()


    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        cv_image = task_vision(cv_image)
        
        cv2.imshow("camera_image", cv_image)
        cv2.waitKey(1)
        

def task_vision(img):
    # Obtener dimensiones de la imagen
    height, width, _ = img.shape

    # Definir los rectángulos
    top_rect = [int(width * 0.15), int(height * 0.06), int(width * 0.7), int(height * 0.32)]
    mid_rect = [int(width * 0.15), int(height * 0.4), int(width * 0.7), int(height * 0.22)]
    bot_rect = [int(width * 0.15), int(height * 0.7), int(width * 0.7), int(height * 0.2)]

    # Dibujar rectangulos
    cv2.rectangle(img, (top_rect[0], top_rect[1]), (top_rect[0] + top_rect[2], top_rect[1] + top_rect[3]), (255, 0, 0), 2)
    cv2.rectangle(img, (mid_rect[0], mid_rect[1]), (mid_rect[0] + mid_rect[2], mid_rect[1] + mid_rect[3]), (0, 255, 0), 2)
    cv2.rectangle(img, (bot_rect[0], bot_rect[1]), (bot_rect[0] + bot_rect[2], bot_rect[1] + bot_rect[3]), (0, 0, 255), 2)


    return img





def main(args=None):
    rclpy.init(args=args)

    image_subscriber = ImageSubscriber()

    rclpy.spin(image_subscriber)

    # Destruir el nodo explicitamente
    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
