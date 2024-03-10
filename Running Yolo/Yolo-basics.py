from ultralytics import YOLO
import cv2
model = YOLO('../Yolo-Weight/yolov8l.pt')
results = model(source="/Users/sushant/PycharmProjects/Object-Detection-Yolo/Object-Detection-Yolo/Running Yolo/Images/crowed image.jpeg",show = True)
cv2.waitKey(0)