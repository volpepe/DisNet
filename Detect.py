import numpy as np
import cv2
from PIL import Image

from DisNet import DisNet
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--ZoomCamera', type=int, help='type of Camera, Zooming camera is True',default=0)
parser.add_argument('--ZoomFactor', type=int, help='Zooming factor of choosing camera', default=1)
parser.add_argument('--image', '-i', type=str, help="Path of image to analyze")
args = parser.parse_args()


class ObjectDetect:

    def __init__(self, image):
        self.image = image

    def callback(self):
        image = Image.open(self.image)
        with graph.as_default():
            image_zoom = model.detect_image(image)
            result = np.asarray(image_zoom)
            cv2.namedWindow("result",cv2.WINDOW_NORMAL)
            cv2.imwrite("result.png",result)
            cv2.waitKey(1)

if __name__ == '__main__':
    import tensorflow as tf

    model=DisNet(bZoomCamera=args.ZoomCamera,scale=args.ZoomFactor)
    image = args.image
    graph = tf.get_default_graph()
    ob = ObjectDetect(image)
    ob.callback()
    model.close_session()
    cv2.destroyAllWindows()
