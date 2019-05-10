import cv2 as cv
import argparse
import numpy as np

class Predictor:
    def __init__(self):
        self.emotions = ["neutral","happiness","surprise","sadness","anger","disgust","fear","contempt"]
        self.face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

    def predict(self, image):
        faces = self.__process_image(image)
    def __process_image(self, image):
        image_gray = cv.cvtColor(cv.imdecode(np.fromstring(image, np.uint8), cv.IMREAD_UNCHANGED), cv.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(image_gray, 1.1, 6)
        print ("Found {0} faces in image".format(len(faces)))

        processed_faces = []
        for (x, y, w, h) in faces:
            cropped = image_gray[y : y+h, x : x+w]
            resized = cv.resize(cropped,(48,48))
            print(resized.shape)
            scaled = resized.reshape(48,48,1) / 255
            processed_faces.append(scaled)
        
        return np.array(processed_faces)