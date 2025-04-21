from ultralytics import YOLO

#from small to large: n, s, m, l
model = YOLO("yolov8m")

# Train the model
model.train(
    data="pinky_imageLabel/dataset.yaml", #put your yaml path here
    epochs=100, 
    imgsz=416, 
    name='result_yolo8m'
    )