import numpy as np
import cv2 
import matplotlib.pyplot as plt
denis = cv2.imread(r'C:\Users\ranas\OneDrive\Desktop\EasyCSELearn\ComputerVisionA2Z\img\IMG20220108101634.jpg',0)
##OpenCV comes with these pre-trained cascade files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def detect_face(img):
    
  
    face_img = img.copy()
  
    face_rects = face_cascade.detectMultiScale(face_img) 
    
    for (x,y,w,h) in face_rects: 
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10) 
        
    return face_img
result = detect_face(denis)
plt.imshow(result,cmap='gray')