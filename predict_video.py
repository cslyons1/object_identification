from ultralytics import YOLO

model = YOLO("C:/Users/shm0d/Desktop/Object_Detection/runs/detect/train2/weights/best.pt")

results = model(source=0, show=True, conf=0.4)