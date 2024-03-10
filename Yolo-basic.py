from ultralytics import YOLO
import cv2
model = YOLO('Yolo-Weight/yolov8n.pt')
results = model(data = "",show = True)
cv2.waitKey(0)