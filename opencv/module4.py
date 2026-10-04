#programa  que detecta rostos e olhos

import cv2
import numpy as np

frontalFace_cascade = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier("./haarcascades/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("./haarcascades/haarcascade_smile.xml")

def detectionInFace(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    faces = frontalFace_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        #define ROI of face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #We're only going to capture half the face.
        height_face, widgth_face = roi_gray.shape

        #we slice from 0 to half the height
        roi_eyes_gray =  roi_gray [0 : int(height_face * 0.6), :] #upper part of the face
        roi_eyes_color = roi_color[0 : int(height_face * 0.6), :]

        eyes = eye_cascade.detectMultiScale(roi_eyes_gray, scaleFactor=1.1, minNeighbors=10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_eyes_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

        #lower part of the face
        roi_mouth_gray =  roi_gray [int(height_face * 0.6) : height_face, :]
        roi_mouth_color = roi_color[int(height_face * 0.6) : height_face, :]

        smiles = smile_cascade.detectMultiScale(roi_mouth_gray, scaleFactor=1.8, minNeighbors=10)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_mouth_color, (sx,sy), (sx+sw, sy+sh), (0,0,255), 2)

    return frame

def webcam():
    myVideoSource = "./videos/omori.mp4"
    # cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error in open cam")
        return

    originalFPS = cap.get(cv2.CAP_PROP_FPS)
    if originalFPS == 0 or np.isnan(originalFPS):
        originalFPS = 30

    while True:
        ret, frame = cap.read()
        if not ret:
            print("error in process frame")
            break

        newFrame = detectionInFace(frame)
        cv2.imshow("webcam", newFrame)

        if cv2.waitKey(originalFPS) & 0xFF == ord("q"):
            break
    return

mySource = "./photos/mrrobot.jpeg"
def photoTarget(source):
    frame = cv2.imread(source)

    if frame is None:
        print("Error in load the photo")
        return 

    newFrame = frame.copy()
    newFrame = detectionInFace(newFrame)

    cv2.imshow("New Frame", newFrame)
    
    while True:
        key = cv2.waitKey()

        if(key == ord("q")):
            cv2.destroyAllWindows()
            break

photoTarget(mySource)
