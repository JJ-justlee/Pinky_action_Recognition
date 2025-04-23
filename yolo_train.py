from ultralytics import YOLO
import os

base_path = 'Pinky_action_Recognition/runs/detect'
yolo_model_path = os.path.join(base_path, 'yolov10')

os.makedirs(yolo_model_path, exist_ok=True)

#from small to large: n, s, m, l
model = YOLO("yolov10l")

model.info()

# # Train the model
# # model download???
# model.train(
#     data="pinky_imageLabel/dataset.yaml", #put your yaml path here
#     epochs=200, 
#     imgsz=416,
#     project=yolo_model_path, #ralative path user wants to save in
#     name='3_result_yolov10s_with_epoch200', #yolo_model_path/name
#     exist_ok=True
#     )