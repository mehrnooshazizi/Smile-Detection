# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:30:27 2020

@author: Azizi
"""
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_smile = cv2.CascadeClassifier('haarcascade_smile.xml')
cam = cv2.VideoCapture(0)
counter=1
while True:
    success, frame = cam.read()
    if success == True:
        #resized_frame = cv2.resize(frame,(600,400))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  
        for (x,y,w,h) in faces:
            newframe = cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)           
            croped_frame = frame[y: y + h, x: x + w]
            smiles = face_smile.detectMultiScale(croped_frame,scaleFactor=1.7,minNeighbors=22,minSize=(25, 25),)          
            for (xs,ys,ws,hs) in smiles:
                frame2 = cv2.rectangle(croped_frame,(xs,ys),(xs+ ws, ys+ hs),(0,0,255),2)
                croped_frame1 = frame[y: ys+ hs, x: xs+ ws]
                cv2.imwrite(f'G:/mehrnoosh/smile{counter}.jpg',croped_frame1)
                counter+=1
            cv2.imshow('myimage', frame)
            cv2.imshow('mysmile', croped_frame1)

    if cv2.waitKey(1) == 27 or counter==101:
        break

cam.release()
cv2.destroyAllWindows()
