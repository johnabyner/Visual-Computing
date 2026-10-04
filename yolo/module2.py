#counter of peoples

import time
from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("yolo26s.pt")

unique_people_ids = set()

# Variáveis para cálculo de FPS
prev_time = 0

def runYolo(frame):
    #dont turn in to gray
    #Modelos YOLO (incluindo o YOLOv8 / YOLO26) são treinados no espaço de cor RGB/BGR de 3 canais.
    
    # Predict apenas para a classe 'person' (id 0)
    results = model.track(source=frame, persist=True,classes=[0], verbose=False, imgsz=320) #turn off the verbose for not Pollute terminal
    return results
    
def drawTargets(results, frame):
    global unique_people_ids

    for result in results:
        if result.boxes.id is not None and len(result.boxes) > 0:
            #transforming the tensor flow array in a normal array
            boxes = result.boxes.xyxy.cpu().numpy()
            confs = result.boxes.conf.cpu().numpy()

            # Extração segura dos IDs
            track_ids = (
                result.boxes.id.int().cpu().tolist()
                if result.boxes.id is not None
                else [None] * len(boxes)
            )
            
            for box,conf,track_id in zip(boxes,confs,track_ids):
                x1,y1,x2,y2 = map(int, box)

                if track_id is not None:
                    unique_people_ids.add(track_id)
                    id_text = f"ID: {track_id}" 
                else:
                    id_text = "Detectando..."
                label = f"human conf:{conf:.2f}"

                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,255), 2)
                cv2.putText(frame, label,(x1, max(y1-10, 20)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    #counter global
    cv2.putText(frame, f"Total people: {len(unique_people_ids)}", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)


pathVideo = "./videos/walkingMan.mp4"
def videoMain(path):
    #FPS
    global prev_time
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        print("Error in open video")
        return

    originalFPS = int(cap.get(cv2.CAP_PROP_FPS))
    if originalFPS == 0 or np.isnan(originalFPS):
        originalFPS = 30

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("error in process frame")
            break
        
        #resizing the video
        frame = cv2.resize(frame, (640,360))
        results = runYolo(frame)
        drawTargets(results, frame)

        #FPS WITH YOLO
        curr_time = time.time()
        fps = 1/(curr_time-prev_time) if (curr_time - prev_time) > 0 else 0
        prev_time = curr_time
        print(fps)

        cv2.imshow("counter of peoples", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
    return

videoMain(pathVideo)
    
# pathImage = "./photos/peoples.jpeg"
# def photoMain(path):
#     frame = cv2.imread(path)

#     newFrame = frame.copy()

#     results = runYolo(newFrame)
#     drawTargets(results, newFrame)

#     cv2.imshow("newFrame", newFrame)

#     while True:
#         key = cv2.waitKey()

#         if(key == ord("q")):
#             cv2.destroyAllWindows()
#             break
