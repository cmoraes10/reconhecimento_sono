import config
import cv2
from ultralytics import YOLO


class EyeDetector:
    def __init__(self):
        self.model = YOLO(config.MODEL_PATH)

    def detect(self, frame) -> bool:
        """Run inference on a frame, draw bounding boxes in place, return True if any eye is closed."""
        results = self.model(frame, conf=config.CONF_THRESHOLD, verbose=False)
        eye_closed = False

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls)
                conf = float(box.conf)
                label = self.model.names[cls].lower()

                color = (0, 0, 255) if "closed" in label else (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                if "closed" in label:
                    eye_closed = True

        return eye_closed
