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
        self.frame_counter = 0  # Iniciar un contador de fotogramas

    def image_callback(self, msg):

        self.frame_counter += 1  # Incrementar el contador de fotogramas
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        if self.frame_counter % 3 == 0:  # Solo procesar la imagen cada 3 fotogramas
            cv_image = task_vision(cv_image)
        
        
        cv2.imshow("camera_image", cv_image)
        cv2.waitKey(1)
        

def task_vision(img):
    # Obtener dimensiones de la imagen
    height, width, _ = img.shape

    # Definir los rectángulos
    top_rect = [int(width * 0.25), int(height * 0.06), int(width * 0.55), int(height * 0.32)]
    mid_rect = [int(width * 0.25), int(height * 0.4), int(width * 0.55), int(height * 0.22)]
    bot_rect = [int(width * 0.25), int(height * 0.7), int(width * 0.55), int(height * 0.2)]


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
    top = ""

    if len(contornos_top) > 1:
      epsilon = 0.01 * cv2.arcLength(contornos_top[1], True)
      approx = cv2.approxPolyDP(contornos_top[1], epsilon, True)
      esquinas = len(approx)

      if esquinas == 3:
        top = "triangulo"

      elif esquinas == 4:
         # Obtén el rectángulo de área mínima que encierra el contorno
        rect = cv2.minAreaRect(contornos_top[1])
        _,_,angle = rect

        # En OpenCV, para 'minAreaRect', si el ángulo es menor que -45, 
        # ajusta el ángulo para que corresponda al ángulo de rotación del rombo
        if angle < -45:
          angle += 90

        # Asume que si el ángulo es cercano a 0 o 90, es un cuadrado,
        # y si es cercano a 45, es un rombo
        if abs(angle-45) < 10:
          top = "rombo"
        else:
          top = "cuadrado"

      elif esquinas == 5:
        top = "pentagono"
      


    #Mid
    # Aproximar contorno para reducir el número de puntos a evaluar
    mid = ""
    mid = pytesseract.image_to_string(mid_crop, config="--psm 6")



    #Bot
    # Obtener el color promedio en la región del contorno
    bot = ""
    average_color = np.mean(bot_crop, axis=(0,1))
    bot = get_color_name(average_color)

    if top == "triangulo" or top == "cuadrado" or top == "pentagono":
       if len(mid.strip()) != 0:
          if bot == 'negro' or bot == 'blanco'or bot == 'rojo' or bot == 'verde' or bot == 'azul':
            # Dibujar los rectángulos
            cv2.rectangle(img, (top_rect[0], top_rect[1]), (top_rect[0] + top_rect[2], top_rect[1] + top_rect[3]), (255, 0, 0), 2)
            cv2.rectangle(img, (mid_rect[0], mid_rect[1]), (mid_rect[0] + mid_rect[2], mid_rect[1] + mid_rect[3]), (0, 255, 0), 2)
            cv2.rectangle(img, (bot_rect[0], bot_rect[1]), (bot_rect[0] + bot_rect[2], bot_rect[1] + bot_rect[3]), (0, 0, 255), 2)

            print("Figura: " + top )
            print("Palabra: " + mid.strip())
            print("Color: " + bot + "\n")

    

    return img




def get_color_name(rgb):
    # Convertir el color a espacio HSV
    hsv = cv2.cvtColor(np.uint8([[rgb]]), cv2.COLOR_RGB2HSV)[0][0]

    if hsv[2] < 20:  # Valor muy bajo, considerar negro
        return 'negro'
    elif hsv[1] < 50 and hsv[2] > 200:  # Saturación muy baja, valor muy alto, considerar blanco
        return 'blanco'
    elif hsv[0] < 20 or hsv[0] > 160:  # Tono cercano a los extremos del espectro HSV, considerar rojo
        return 'rojo'
    elif 20 <= hsv[0] < 70:  # Tono en el rango de los verdes
        return 'verde'
    elif 70 <= hsv[0] < 160:  # Tono en el rango de los azules
        return 'azul'




def main(args=None):
    rclpy.init(args=args)

    image_subscriber = ImageSubscriber()

    rclpy.spin(image_subscriber)

    # Destruir el nodo explicitamente
    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
