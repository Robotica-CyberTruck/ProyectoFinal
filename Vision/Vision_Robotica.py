import cv2
import pytesseract
import numpy as np
from PIL import Image



def detectar_figura(contorno, imagen):

  # Encontrar el rectángulo delimitador del contorno
  x, y, w, h = cv2.boundingRect(contorno)

  # Aproximar contorno para reducir el número de puntos a evaluar
  epsilon = 0.02 * cv2.arcLength(contorno, True)
  approx = cv2.approxPolyDP(contorno, epsilon, True)

  if len(approx) <= 8:
    es_figura = True
  else:
    es_figura = False

  return es_figura, len(approx)    




def detectar_color(dentro_banner, imagen):
    
  # Encontrar el rectángulo delimitador del contorno
  x, y, w, h = cv2.boundingRect(dentro_banner)

  # Recortar la región de interés
  fragmento = imagen[y:y+h, x:x+w]

  # Obtener las dimensiones de la imagen 
  alto, ancho = fragmento.shape[:2]

  # Recortar un marco de 1 píxel
  roi = fragmento[1:alto-1, 1:ancho-1]

  # Obtener el color promedio en la región del contorno
  average_color = np.mean(roi, axis=(0,1))

  # Calcular la moda de los valores de color en la región de interés
  color = np.squeeze(cv2.mean(roi))
  stddev = np.std(roi, axis=(0, 1))

  # Definir un umbral para determinar si la figura tiene un solo color
  umbral_stddev = 20

  es_color = False

  # Verificar si la figura tiene un solo color
  if (average_color[0] <= 240) and (average_color[1] <= 240) and (average_color[2] <= 240):
    if (stddev[0] <= umbral_stddev) and (stddev[1] <= umbral_stddev) and (stddev[2] <= umbral_stddev):
      es_color = True

  
  
  return es_color, average_color



def texto(imagen, x, y, w, h):
  roi = imagen[y:y+h, x:x+w]
  texto = pytesseract.image_to_string(roi, config="--psm 6")

  return texto




def main(imagen):

  #Etapa de filtrado
  gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
  desenfocado = cv2.GaussianBlur(gris, (5, 5), 0)

  #Ajusta los parámetros de umbralización
  umbral, thresh = cv2.threshold(desenfocado, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
  nuevo_umbral = umbral * 0.7  # Ajusta el umbral multiplicándolo por un factor
  _, thresh_ajustado = cv2.threshold(desenfocado, nuevo_umbral, 255, cv2.THRESH_BINARY)
    
  cv2.imshow(thresh)

  #Deteccion de contornos
  contornos, jerarquia = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    
  # Ordenar contornos por área y seleccionar  contorno    
  sorted_contours = sorted(contornos, key=cv2.contourArea, reverse=True)
  dentro_banner = sorted_contours[3:] 



  #Analisis de los contornos
  for contorno in dentro_banner:
    es_color, color = detectar_color(contorno, imagen)

    if es_color == True:
      x, y, w, h = cv2.boundingRect(contorno)

      print("El color en RGB es: ")
      print(color)

      # Calcular el aumento del 10%
      aumento_w = int(0.1 * w)
      aumento_h = int(0.1 * h)

      # Calcular las coordenadas del rectángulo delimitador ampliado
      x_ampliado = x - aumento_w
      y_ampliado = y - aumento_h
      w_ampliado = w + 2*aumento_w
      h_ampliado = h + 2*aumento_h
 
      # Encerrar las coordenadas en un contorno
      contorno_ampliado = [np.array([[x_ampliado, y_ampliado], [x_ampliado+w_ampliado, y_ampliado], [x_ampliado+w_ampliado, y_ampliado+h_ampliado], [x_ampliado, y_ampliado+h_ampliado]])]


      # Dibujar el cuadrado en la imagen
      cv2.drawContours(imagen, contorno_ampliado, -1, (128, 0, 128), 2)
      cv2.putText(imagen, 'Color', (x_ampliado + w_ampliado, y_ampliado), cv2.FONT_HERSHEY_COMPLEX, 0.5, (128, 0, 128), thickness=1) 
             
      for j, c in enumerate(dentro_banner):
        if np.array_equal(c, contorno):
          dentro_banner.pop(j)

      break;




  contorno = dentro_banner[0]
  figura, esquinas = detectar_figura(contorno, imagen)


  if figura == True:
          
    x, y, w, h = cv2.boundingRect(contorno)
          
    print("\n")
    if esquinas == 3:
      print("Numero de esquinas:" + str(esquinas) + "\n" + "Es un triangulo")
    elif esquinas == 4:
      print("Numero de esquinas:" + str(esquinas) + "\n" + "Es un cuadrado")
    elif esquinas == 5:
      print("Numero de esquinas:" + str(esquinas) + "\n" + "Es un pentagono")
    elif esquinas == 6:
      print("Numero de esquinas:" + str(esquinas) + "\n" + "Es un Hexagono")
    elif esquinas == 7:
      print("Numero de esquinas:" + str(esquinas) + "\n" + "Es un Heptagono")
    elif esquinas == 8:
      print("Numero de esquinas:" + str(esquinas) + "\n" + "Es un octagono")
          

    # Calcular el tamaño del lado del cuadrado
    lado = int(max(w, h) * 1.02)

    # Calcular las coordenadas del cuadrado centrado en el contorno
    x_centro = x + w // 2
    y_centro = y + h // 2
    x = x_centro - lado // 2
    y = y_centro - lado // 2

    # Crear una lista de un solo contorno para dibujar el cuadrado
    cuadrado = [np.array([[x, y], [x+lado, y], [x+lado, y+lado], [x, y+lado]])]          


    cv2.drawContours(imagen, cuadrado, -1, (0, 255, 0) , 2)
    cv2.putText(imagen, 'Figura', (x + w, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), thickness=1) 
          
    if contorno in dentro_banner:
      dentro_banner.remove(contorno)
      dentro_banner.pop(0)  


     
    # Encuentra el rectángulo delimitador más pequeño que cubre todos los contornos
    x_min, y_min, w_total, h_total = cv2.boundingRect(np.concatenate(dentro_banner))


    # Calcula el aumento en píxeles
    aumento_w = int(w_total * 0.15)
    aumento_h = int(h_total * 0.15)

    # Ajusta el rectángulo delimitador con el aumento
    x_min -= aumento_w
    y_min -= aumento_h
    w_total += 2 * aumento_w
    h_total += 2 * aumento_h

    texto_detectado = texto(imagen, x_min, y_min, w_total, h_total)
    print("\n" )
    print("El texto es: " + str(texto_detectado))

    # Dibuja el rectángulo delimitador en la imagen original
    cv2.rectangle(imagen, (x_min, y_min), (x_min + w_total, y_min + h_total), (255, 0, 0), 2)
    cv2.putText(imagen, 'Letras', (x_min + w, y_min), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), thickness=1) 




    


         


imagen = cv2.imread('banner3.jpg')
imagen = cv2.imread('banner2.jpg')
imagen = cv2.imread('banner_bordeDelgado.jpg')
imagen = cv2.imread('banner_otroOrden (1).jpg')

main(imagen)
             
cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
