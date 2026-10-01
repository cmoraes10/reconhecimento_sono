# reconhecimento_sono

A computer vision system that detects drowsiness in real time and fires an alarm when eyes stay closed for more than 3 seconds. Built with Python, OpenCV, and a custom YOLO model trained on eye state classification.

## How it works

Each video frame is passed through a YOLO model that detects eyes and classifies them as open or closed. When the closed state is detected continuously, a timer starts. If it reaches 3 seconds, the alarm plays on a loop via pygame. The alarm stops as soon as the eyes open again.

The UI overlays a status bar, a timestamp, a colored border (red on alert, blue otherwise), and a progress bar showing how close the timer is to the threshold.

## Requirements

Python 3.10 or later.

```
pip install opencv-python ultralytics pygame
```

A trained model weights file (`best.pt`) must be placed at `model/best.pt`. The model is not included in the repository because of its size; train or download one separately. The expected YOLO class names are `olhos_fechados` (closed) and `olhos_abertos` (open), as defined in `config.py`.

## Run

```
python main.py
```

Press `z` to toggle fullscreen. Press `Esc` to quit.

## License

MIT.
