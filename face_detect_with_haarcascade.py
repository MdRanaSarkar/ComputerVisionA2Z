import numpy as np
import cv2 
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\ranas\OneDrive\Desktop\EasyCSELearn\ComputerVisionA2Z\img\IMG20220108101634.jpg")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_detection(particular_img):
    face_img = particular_img.copy()

    detected_areas = face_cascade.detectMultiScale(face_img)

    for (x,y, w, h) in detected_areas:
        cv2.rectangle(face_img,(x,y), (x+w,y+h), (255,255,255), 10)

    return face_img 


detected_img = face_detection(img)

plt.imshow(detected_img)

        