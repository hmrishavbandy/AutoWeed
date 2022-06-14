import cv2
import matplotlib.pyplot as plt
import os
import sys

from yolo.utils import *
from yolo.darknet import Darknet


def detection(m,path,class_names,iou_thresh=0.4,nms_thresh=0.6):

    '''
    input path of any image will return detection in given image
    '''    
    plt.rcParams['figure.figsize'] = [24.0, 14.0]
    img = cv2.imread(path)
    original_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resized_image = cv2.resize(original_image, (m.width, m.height))
    iou_thresh = iou_thresh
    nms_thresh = nms_thresh
    boxes = detect_objects(m, resized_image, iou_thresh, nms_thresh)
    print_objects(boxes, class_names)
    return plot_boxes(original_image, boxes, class_names, plot_labels = True)

def detect_image(im_path="weed_1.jpeg"):

    cfg_file = 'yolo/crop_weed.cfg'
    weight_file = 'yolo/crop_weed_detection.weights'
    namesfile = 'yolo/obj.names'
    m = Darknet(cfg_file)
    m.load_weights(weight_file)
    class_names = load_class_names(namesfile)

    k=time.time()
    out, bbox_dict= detection(m,im_path,class_names)

    print("Time",time.time()-k)
    
    return out,bbox_dict


if __name__=='__main__':
    dict_=detect_image(sys.argv[1])
    print(dict_)
    
