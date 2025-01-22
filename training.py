from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
#model = YOLO(r".\runs\detect\train13\weightslast.pt")  # load pretrained model
#model = YOLO(r".\runs\detect\train10\weights\best.pt")  # load a custom model

# Use the model
model.train(data="config.yaml",epochs=100,imgsz=480,save_period=1,plots=True,save=True)  # train the model

# Resume training
#results = model.train(resume=True)

