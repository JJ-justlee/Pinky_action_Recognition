from ultralytics import YOLO
import cv2

def run_webcam_yolo():

    model = YOLO('Pinky_action_Recognition/runs/detect/yolov10/3_result_yolov10s_with_epoch200/weights/best.pt') #put your model path here 
    
    cap = cv2.VideoCapture(2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("can not read frame")
            break

        cropped = frame[250:920, 300:1700]  # y1:y2, x1:x2

        results = model.predict(source=cropped, conf=0.8, save=False, verbose=False)
        
        for result in results:
            annotated_frame = result.plot()
            cv2.imshow("YOLO Detection (Cropped View)", annotated_frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_webcam_yolo()
