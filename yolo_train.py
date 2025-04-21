from ultralytics import YOLO

# Load YOLOv10n model from scratch
model = YOLO("yolov8n")

# Train the model
model.train(data="dataset.yaml", epochs=100, imgsz=416) #put your yaml path here