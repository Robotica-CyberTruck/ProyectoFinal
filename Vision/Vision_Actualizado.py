import os
import cv2
import numpy as np
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import colorsys

def detecion_contornos(imagen):
    #Etapa de filtrado
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    desenfocado = cv2.GaussianBlur(gris, (5, 5), 0)

    # Aplicar el filtro de umbralización de Otsu
    _, thresh = cv2.threshold(desenfocado, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #Deteccion de contornos
    contornos, jerarquia = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)   

    sorted_contours = sorted(contornos, key=cv2.contourArea, reverse=True) 

    #contornos encontrados

    # Dibujar los contornos en la imagen
    #cv2.drawContours(regiones_copia, contornos, -1, (0, 0, 0), 2)

    # Mostrar la imagen con los contornos
    #cv2.imshow('Imagen con contornos', regiones_copia)

    return sorted_contours





def draw_rectangles(img):
    # Leer la imagen
    #img = cv2.imread(img_path)

    # Obtener dimensiones de la imagen
    height, width, _ = img.shape

    # Definir los rectángulos
    top_rect = [int(width * 0.15), int(height * 0.06), int(width * 0.7), int(height * 0.32)]
    mid_rect = [int(width * 0.15), int(height * 0.4), int(width * 0.7), int(height * 0.22)]
    bot_rect = [int(width * 0.15), int(height * 0.7), int(width * 0.7), int(height * 0.2)]

    # Dibujar los rectángulos
    cv2.rectangle(img, (top_rect[0], top_rect[1]), (top_rect[0] + top_rect[2], top_rect[1] + top_rect[3]), (255, 0, 0), 2)
    cv2.rectangle(img, (mid_rect[0], mid_rect[1]), (mid_rect[0] + mid_rect[2], mid_rect[1] + mid_rect[3]), (0, 255, 0), 2)
    cv2.rectangle(img, (bot_rect[0], bot_rect[1]), (bot_rect[0] + bot_rect[2], bot_rect[1] + bot_rect[3]), (0, 0, 255), 2)
    

     # Recortar y guardar las áreas dentro de los rectángulos
    top_crop = img[top_rect[1]:top_rect[1] + top_rect[3], top_rect[0]:top_rect[0] + top_rect[2]]
    mid_crop = img[mid_rect[1]:mid_rect[1] + mid_rect[3], mid_rect[0]:mid_rect[0] + mid_rect[2]]
    bot_crop = img[bot_rect[1]:bot_rect[1] + bot_rect[3], bot_rect[0]:bot_rect[0] + bot_rect[2]]

    
    contornos_top = detecion_contornos(top_crop) 
 
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

    return img

    

    


    

cap = cv2.VideoCapture(0)
cv2.namedWindow("Frame de la Webcam", cv2.WINDOW_NORMAL)
frame_count = 0

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo obtener el frame. Asegúrate de que tu cámara está conectada y funciona correctamente.")
            break
       
        frame_count += 1
        if frame_count % 3 == 0:  # solo procesa cada n fotograma
          frame = draw_rectangles(frame)
          cv2.imshow("VISION", frame)

        


        if cv2.getWindowProperty("Frame de la Webcam",cv2.WND_PROP_VISIBLE) < 1:  
            # La ventana se ha cerrado, así que rompe el bucle
            break 

        # Presiona 'q' para salir del bucle
        if cv2.waitKey(1) == ord('q'):
            break
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    cap.release()
    cv2.destroyAllWindows()



