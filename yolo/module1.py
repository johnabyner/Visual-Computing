#detector of things
from ultralytics import YOLO
import cv2

#deixar preto e branco
#fazer roi

model = YOLO("yolo26s.pt")

def runYolo(image):
    results = model.predict(source=image,verbose=false)
    return results #class,confidence,bounding box

def drawTargets(results, image):
    print(results)
    for result in results:
        #Move os dados da memória da placa de vídeo (GPU) para a memória RAM do sistema (CPU).
        #Converte o Tensor do PyTorch em um array padrão do NumPy.
        boxes = result.boxes.xyxy.cpu().numpy()
        confs = result.boxes.conf.cpu().numpy()
        clss = result.boxes.cls.cpu().numpy()

        for box, conf, cls in zip(boxes, confs, clss):
            #convertendo coodernadas para inteiros
            x1,y1,x2,y2 = map(int, box)

            class_id = int(cls)
            class_name = result.names[class_id]

            label = f"{class_name} {conf:.2f}"  

            cv2.rectangle(image, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(image, label,(x1, max(y1-10, 20)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)


source = "./photos/dogAndHuman.jpeg"
def main(source):
    frame = cv2.imread(source)

    if frame is None:
        print("Error in load this photo")
        return
    
    newFrame = frame.copy()
    results = runYolo(newFrame)
    drawTargets(results, newFrame)

    cv2.imshow("new frame",newFrame)

    while True:
        key = cv2.waitKey()

        if (key == ord("q")):
            cv2.destroyAllWindows()
            break

main(source)