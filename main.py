import cv2
import time
from datetime import datetime
from detector import EyeDetector
from alert import AlertSystem

WINDOW = "Drowsiness Detector"
ALERT_THRESHOLD = 3.0

detector = EyeDetector()
alert = AlertSystem()

cap = cv2.VideoCapture(0)
closed_start = None
fullscreen = False

cv2.namedWindow(WINDOW, cv2.WINDOW_NORMAL)


def draw_ui(frame, is_closed: bool, timer: float):
    h, w, _ = frame.shape

    if is_closed and timer >= ALERT_THRESHOLD:
        cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 15)
        cv2.putText(frame, "ALERT: Eyes closed!", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    else:
        cv2.rectangle(frame, (0, 0), (w, h), (0, 40, 200), 2)

    cv2.rectangle(frame, (0, 0), (w, 50), (20, 20, 20), -1)
    cv2.putText(frame, "Drowsiness Detector", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

    now = datetime.now().strftime("%H:%M:%S")
    cv2.putText(frame, now, (w - 150, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    if is_closed:
        status_text = "DROWSY!" if timer >= ALERT_THRESHOLD else "Eyes closed"
        status_color = (0, 0, 255) if timer >= ALERT_THRESHOLD else (0, 165, 255)
    else:
        status_text = "Eyes open"
        status_color = (0, 255, 0)

    cv2.putText(frame, status_text, (50, h - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

    if is_closed:
        progress = min(timer / ALERT_THRESHOLD, 1.0)
        bar_w, bar_h = 100, 15
        bar_x = w - bar_w - 50
        bar_y = h - bar_h - 30

        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), (50, 50, 50), -1)
        fill_color = (0, 0, 255) if progress >= 1.0 else (0, 255, 255)
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + int(bar_w * progress), bar_y + bar_h), fill_color, -1)
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), (255, 255, 255), 1)

    return frame


while True:
    ret, frame = cap.read()
    if not ret:
        break

    is_closed = detector.detect(frame)

    if is_closed:
        if closed_start is None:
            closed_start = time.time()
        timer = time.time() - closed_start
    else:
        closed_start = None
        timer = 0
        alert.stop()

    if timer >= ALERT_THRESHOLD:
        alert.play()

    frame = draw_ui(frame, is_closed, timer)
    cv2.imshow(WINDOW, frame)

    k = cv2.waitKey(1)

    if k == 122:  # z key toggles fullscreen
        fullscreen = not fullscreen
        prop = cv2.WINDOW_FULLSCREEN if fullscreen else cv2.WINDOW_NORMAL
        cv2.setWindowProperty(WINDOW, cv2.WND_PROP_FULLSCREEN, prop)

    if k == 27:  # Esc
        break

cap.release()
cv2.destroyAllWindows()
alert.stop()
