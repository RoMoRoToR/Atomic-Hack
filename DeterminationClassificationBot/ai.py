import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("/content/BestFirst.pt")

def predict(image_bytes: bytes, extension: str) -> bytes:
   decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
   result = model(decoded)[0]
   numpy_array = result.plot()
   success, encoded_image = cv2.imencode(extension, numpy_array)
   return encoded_image.tobytes()
