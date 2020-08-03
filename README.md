# DisNet
Object Detection and Object Distance Estimation Net, Keras

How to use:
1) create a virtual environment with:
```
python -m venv PATH_TO_ENV
```
2) install requirements with:
```
python -m pip install -r requirements.txt
```
3) download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/).
ex. ```wget https://pjreddie.com/media/files/yolov3.weights```
4) Convert the Darknet YOLO model to a Keras model running:
```
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
```