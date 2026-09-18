#source ../.venv/bin/activate
from pathlib import Path
import cv2
import numpy as np

#will open a image
#button 1 will paint a region
def openImage():
    source = str(Path("./photos/examplePhoto.webp"))
    sourceResults = str(Path("./results/newPhoto.jpg"))

    photo = cv2.imread(source)
    print(type(photo))
    print(photo.shape)

    cv2.imshow("test",photo)

    while True:
        key = cv2.waitKey()
        if key == ord("1"):
            photo[30:60,30:260] = [0, 0, 255]
            cv2.imshow("test",photo)
        #pixels = photo[100:300, 200:400] = [0,0,255]

        elif key == ord("0"):
            cv2.destroyAllWindows()
            # Salva a cópia no disco
            cv2.imwrite(sourceResults, photo)
            break

#part two
#will open a iamge and when press de button 1 will turn everything except yellow in gray
def blackAndWhiteFilterPhoto():
    source = str(Path("./photos/frutas.jpeg"))
    
    photo = cv2.imread(source)
    print(photo.shape)

    hsv = cv2.cvtColor(photo, cv2.COLOR_BGR2HSV)
    lower_limit = np.array([12,50,50]) #HSV
    upper_limit = np.array([40,255,255]) #HUE, SATURATION, VALUE

    cv2.imshow("teste", photo)

    while True:
        key = cv2.waitKey()

        if key == ord("1"):
            #mascaras, preto(0) branco(1)
            #branco(1) aonde é amarelo e preto(0) no resto
            mask_yellow = cv2.inRange(hsv, lower_limit, upper_limit)
            mask_others = cv2.bitwise_not(mask_yellow)
        
            #recortar a parte amarela
            yelow_part = cv2.bitwise_and(photo, photo, mask = mask_yellow)

            #converter a foto inteira para cinza
            gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
            gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

            #recortar a parte nao amarela da imagem
            background_gray = cv2.bitwise_and(gray_bgr, gray_bgr, mask=mask_others)

            #somar a parte amarela colorida com o fundo em escala de cinza
            photoFiltered = cv2.add(yelow_part, background_gray)

            cv2.imshow("teste", photoFiltered)
        
        elif key == ord("0"):
            cv2.destroyAllWindows()
            break

blackAndWhiteFilterPhoto()