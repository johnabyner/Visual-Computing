#Detector de formas
#Contador de objetos
from pathlib import Path
import cv2
import numpy as np

source = str(Path('./photos/geometricShapes.jpeg'))
colorRed = (0, 0, 255)
colorGreen = (0,255,0)

def detectorShape(vertices, x,y,w,h):
    if vertices == 3:
        return 'Triangle'
    elif vertices == 4:
        # Verifica a proporção entre largura e altura para diferenciar Quadrado de Retângulo
        aspectRatio = float(w) / h
        if 0.95 <= aspectRatio <= 1.05:
            return 'Square'
        else:
            return 'Rectangle'
    elif vertices == 5:
        return 'Pentagon'
    elif vertices > 5:
        return 'Circle'
    else:
        return 'Unknown'

def detectorObject(mask, newPhoto, minArea = 1000):
    contours, hierachy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    totalObjects = 0

    #Com base na relação $largura / altura$, o código agora consegue diferenciar um Quadrado de um Retângulo.
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > minArea:            
            totalObjects += 1

            perimeter = cv2.arcLength(contour, True)
            epsilon = 0.03 * cv2.arcLength(contour, True)
            approximate = cv2.approxPolyDP(contour,epsilon,True)

            vertice = len(approximate)
            x,y,w,h = cv2.boundingRect(contour)
            
            form = detectorShape(vertice, x,y,w,h)

            cv2.drawContours(newPhoto, [contour], -1, colorGreen, 2)
            cv2.putText(newPhoto, form, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (colorRed), 2)
    cv2.putText(newPhoto, f"Total objects found: {totalObjects}", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colorGreen, 2)

def main():
    photo = cv2.imread(source)
    if photo is None:
        print("No photos")
        return

    gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    #Aplicar um leve desfoque na imagem cinza antes de gerar a máscara evita a criação de contornos falsos por conta de textura na imagem.
    blurred = cv2.GaussianBlur(gray, (5,5), 0)
    
    edges = cv2.Canny(blurred,50,150)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("test", mask)
    while True:
        key = cv2.waitKey() & 0xFF

        if(key == ord("1")):
            newPhoto = photo.copy() 

            detectorObject(mask, newPhoto)
            cv2.imshow("changed", newPhoto)

        if(key == ord("q")):
            cv2.destroyAllWindows()
            break        

main()
