# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:49:05 2018

@author: PRIYANSHZALAVADIYA
"""

import cv2
#from scipy.stats import pearsonr
#import numpy as np
from math import ceil
#from PIL import Image
cap = cv2.VideoCapture('Dog.mp4')
looper,image=cap.read()
count=0
looper=True
size = 600, 400
fps = cap.get(cv2.CAP_PROP_FPS)

number=fps*0.1
num=ceil(number)
ret, frame = cap.read()
cv2.imwrite("asd.jpg", frame)
i=0
similarity=[]
while(1):
    i=0
    while(i<num-1):
        ret, frame = cap.read()
        i=i+1
    if ret:
        if cv2.imread("asd.jpg") is not None:
            old_frame = cv2.imread("asd.jpg")
            sift = cv2.xfeatures2d.SIFT_create()
            kp_1, desc_1 = sift.detectAndCompute(old_frame, None)
            kp_2, desc_2 = sift.detectAndCompute(frame, None)
            index_params = dict(algorithm=0, trees=5)
            search_params = dict()
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(desc_1, desc_2, k=2)
            good_points=[]
            ratio = 0.6
            for m, n in matches:
                if m.distance < ratio*n.distance:
                    good_points.append(m)
            similarity.append(len(good_points))
            cv2.imwrite("asd.jpg", frame)
    else :
        break
    
for i in range(0,len(similarity)):
    print(similarity[i])

cap.release()
cv2.destroyAllWindows()
