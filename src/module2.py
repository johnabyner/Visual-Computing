from pathlib import Path
import cv2
import time
import numpy as np

source = str(Path("./videos/omori.mp4"))
video = cv2.VideoCapture(source)

widgth_video = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height_video = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
if widgth_video > 1280:
    ratio = 1280 / width_frame

    new_width = 1280
    new_height = int(height_frame * ratio)

    frame = cv2.resize(frame, (new_width, new_height))

def reverseColor(frame):
    return cv2.bitwise_not(frame)

def main():
    #fps original from video
    originalFPS = video.get(cv2.CAP_PROP_FPS)
    if originalFPS == 0 or np.isnan(originalFPS):
        originalFPS = 30
    #calculates the required wait time per frame in milliseconds
    delay_ms = int(1000/originalFPS)

    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        #process frame:
        processFrame = reverseColor(frame)

        cv2.putText(processFrame, f"FPS: {originalFPS:.1f}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        #show the image
        cv2.imshow("video", processFrame)
        if cv2.waitKey(delay_ms) & 0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()
main()