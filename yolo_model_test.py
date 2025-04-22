from ultralytics import YOLO
import cv2

model = YOLO('Pinky_action_Recognition/runs/detect/result_yolo8m/weights/best.pt')  # 모델 경로

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 예측
    results = model.predict(source=frame, save=False, conf=0.8, verbose=False)

    # results[0]은 첫 프레임 결과
    annotated_frame = results[0].plot()

    # 결과 시각화
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
