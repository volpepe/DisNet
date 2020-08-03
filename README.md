# DisNet
Object Detection and Object Distance Estimation Net, Keras

How to use:
1) Create a virtual environment with:
```
python -m venv PATH_TO_ENV
```
2) Install requirements with:
```
python -m pip install -r requirements.txt
```
3) Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/).
e.g. 
```wget https://pjreddie.com/media/files/yolov3.weights```
4) Convert the Darknet YOLO model to a Keras model running:
```
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
```
5) Activate virtual environment

6) Start DisNet running:
```
python Detect.py -i PATH_TO_IMAGE
```
This will save the output to "result.png" in the code folder.
