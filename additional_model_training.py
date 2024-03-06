import os
from ultralytics import YOLO

main_dir = "C:/Users/shm0d/Desktop/Object_Detection"

model = YOLO("C:/Users/shm0d/Desktop/Object_Detection/runs/detect/train/weights/last.pt")

results = model.train(data=os.path.join(main_dir, "config.yaml"),epochs = 10)