from mtcnn import MTCNN
import os
import rectangle
import cv2
import json

def detect_faces(img : cv2.typing.MatLike, resolution, margin, shift_center) :
    detector = MTCNN()
    data=detector.detect_faces(img)
    if data != []:
         for i, faces in enumerate(data): # iterate through all the faces found
            box=faces['box'] 
            if box !=[] and faces['confidence'] > 0.95:
                faceBox = rectangle.make_square(box, margin, shift_center)
                cropped_img=img[faceBox[1]: faceBox[3],faceBox[0]: faceBox[2]]
                height, width, _ = cropped_img.shape
                yield {
                     "image":cropped_img, 
                     "confidence" : faces['confidence'],
                     "keypoints" : json.dumps(faces['keypoints']),
                     "resolution" : f"{width}x{height}"
                     }

def scale_image(image, resolution):
    dim = (resolution, resolution)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized