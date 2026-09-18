

from pathlib import Path
import cv2
import numpy as np

colorRed = (0, 0, 255)

def targetColor(name, mask, newPhoto, min_area=1000):
    #aplying the opening/closening for KILLING THE NOISES HAHAHA of the mask
    kernel = np.ones((5,5), np.uint8)
    mask_clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask_clean = cv2.morphologyEx(mask_clean, cv2.MORPH_CLOSE, kernel)
    
    #calculing the contours for put the rectangle
    contours, _= cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        #discards elements where countours smaller than min_area
        if cv2.contourArea(contour) > min_area:
            x,y,w,h = cv2.boundingRect(contour)

            cv2.rectangle(newPhoto, (x,y), (x+w, y+h) ,(colorRed), 2)
            cv2.putText(newPhoto, name, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (colorRed), 2)

def colorTrack():
    source = str(Path("./photos/colors.jpeg"))

    photo = cv2.imread(source)
    if photo is None: exit()   
    print(photo.shape)

    #HSV 
    hsv = cv2.cvtColor(photo, cv2.COLOR_BGR2HSV)

    #LIMITS
    #blue 
    blue_lower_limit = np.array([90,50,50])
    blue_upper_limit = np.array([130,255,255])

    #green 
    green_lower_limit = np.array([35,50,50])
    green_upper_limit = np.array([85,255,255])

    #red, two ranges for pick all tones
    red_lower_limit1 = np.array([0,100,100])
    red_upper_limit1 = np.array([10,255,255])
    red_lower_limit2 = np.array([170,70,50])
    red_upper_limit2 = np.array([180,255,255])

    #masks 
    mask_blue = cv2.inRange(hsv, blue_lower_limit, blue_upper_limit)
    mask_green = cv2.inRange(hsv, green_lower_limit, green_upper_limit)

    mask_red1 = cv2.inRange(hsv, red_lower_limit1, red_upper_limit1)
    mask_red2 = cv2.inRange(hsv, red_lower_limit2, red_upper_limit2)
    mask_red = cv2.add(mask_red1, mask_red2)

    cv2.imshow("teste",photo)
    while True:
        key = cv2.waitKey()

        if(key == ord("1")):
            newPhoto = photo.copy()

            #put a rectangle and name in target
            targetColor("blue", mask_blue,newPhoto)
            targetColor("green", mask_green,newPhoto)
            targetColor("red", mask_red,newPhoto)

            cv2.imshow("teste", newPhoto)

        if(key == ord("q")):
            cv2.destroyAllWindows()
            break

colorTrack()
