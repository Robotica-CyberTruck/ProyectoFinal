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
            10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        task_vision(cv_image)

        cv2.imshow("camera_image", cv_image)
        cv2.waitKey(1)
        

def task_vision(img):
    # Obtener dimensiones de la imagen
    height, width, _ = img.shape

    # Definir los rectángulos
    top_rect = [int(width * 0.15), int(height * 0.06), int(width * 0.7), int(height * 0.32)]
    mid_rect = [int(width * 0.15), int(height * 0.4), int(width * 0.7), int(height * 0.22)]
    bot_rect = [int(width * 0.15), int(height * 0.7), int(width * 0.7), int(height * 0.2)]

    # Dibujar los rectángulos
    #cv2.rectangle(img, (top_rect[0], top_rect[1]), (top_rect[0] + top_rect[2], top_rect[1] + top_rect[3]), (255, 0, 0), 2)
    #cv2.rectangle(img, (mid_rect[0], mid_rect[1]), (mid_rect[0] + mid_rect[2], mid_rect[1] + mid_rect[3]), (0, 255, 0), 2)
    #cv2.rectangle(img, (bot_rect[0], bot_rect[1]), (bot_rect[0] + bot_rect[2], bot_rect[1] + bot_rect[3]), (0, 0, 255), 2)
    

    # Recortar y guardar las áreas dentro de los rectángulos
    top_crop = img[top_rect[1]:top_rect[1] + top_rect[3], top_rect[0]:top_rect[0] + top_rect[2]]
    mid_crop = img[mid_rect[1]:mid_rect[1] + mid_rect[3], mid_rect[0]:mid_rect[0] + mid_rect[2]]
    bot_crop = img[bot_rect[1]:bot_rect[1] + bot_rect[3], bot_rect[0]:bot_rect[0] + bot_rect[2]]

    
    #Etapa de filtrado
    gris = cv2.cvtColor(top_crop, cv2.COLOR_BGR2GRAY)
    desenfocado = cv2.GaussianBlur(gris, (5, 5), 0)

    # Aplicar el filtro de umbralización de Otsu
    _, thresh = cv2.threshold(desenfocado, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #Deteccion de contornos
    contornos, jerarquia = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)   

    contornos_top = sorted(contornos, key=cv2.contourArea, reverse=True) 
 
    #Top 
    # Aproximar contorno para reducir el número de puntos a evaluar

    if len(contornos_top) > 1:
      epsilon = 0.01 * cv2.arcLength(contornos_top[1], True)
      approx = cv2.approxPolyDP(contornos_top[1], epsilon, True)
      esquinas = len(approx)

      if esquinas == 3:
        print("triangulo")
      elif esquinas == 4:
        print("cuadrado")
      elif esquinas == 5:
        print("pentagono")
      elif esquinas == 6:
        print("Hexagono")
      elif esquinas == 7:
        print("Heptagono")
      elif esquinas == 8:
        print("octagono")


    #Mid
    # Aproximar contorno para reducir el número de puntos a evaluar
    texto = pytesseract.image_to_string(mid_crop, config="--psm 6")

    print("Palabra: " + texto)


    #Bot
    # Obtener el color promedio en la región del contorno
    average_color = np.mean(bot_crop, axis=(0,1))
    print("Color: " + str(average_color))





def main(args=None):
    rclpy.init(args=args)

    image_subscriber = ImageSubscriber()

    rclpy.spin(image_subscriber)

    # Destruir el nodo explicitamente
    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
