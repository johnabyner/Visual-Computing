#training my own model
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

def train():
    model.train(data="data.yaml", epochs=50,batch=16, imgsz=640)

def rateModel(source):
    metrics = model.val(data="data.yaml")
    print("mAP50-95:", metrics.box.map)

def readLicensePlate(source):
    results = model.predict(source=source, conf=0.5)

    for result in results:
        result.show()

# train()

source = "test/images/0a2bdc41-3f28-4ea8-b30f-74eebbe8e7ae_jpg.rf.b1f0aed31e819e5d215f7595d346dccd.jpg"
rateModel(source)
#box -> precision 
#R -> recal, encontrou cerca de

# readLicensePlate(source)