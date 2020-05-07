# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dlib
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

face_detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("E:/Facial_Landmark_project/shape/shape_predictor_68_face_landmarks.dat")

while True:
    success, frame = cap.read()
    Img_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_detector(Img_frame)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        # landmarks = predictor(Img_frame, face)

        # for n in range(0, 68):
        #     x = landmarks.part(n).x
        #     y = landmarks.part(n).y
        #     cv2.circle(frame, (x, y), 3, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
