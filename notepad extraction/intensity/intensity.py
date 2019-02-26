# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:49:05 2018

@author: PRIYANSHZALAVADIYA
"""

import cv2
#from scipy.stats import pearsonr
#import numpy as np

import csv
#from scipy.stats import pearsonr
#import numpy as np
from math import ceil
from os import listdir
from os.path import isfile, join
mypath = "F:/project/project videos/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
csvData = [['videoname','averageintensitycomparision']]
with open('intensity.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()

for video_name in onlyfiles:
   
#from PIL import Image
    cap = cv2.VideoCapture(mypath+video_name)
    print('video name is',video_name)
    looper,image=cap.read()
    count=0
    looper=True
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    number=fps*0.5
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
                print(len(good_points))
                cv2.imwrite("asd.jpg", frame)
        else :
            break
    
    averag=sum(similarity) / float(len(similarity))
    final_averag=(averag/max(similarity))*100
    print('final average is'+final_averag)
    row=[video_name,final_averag]
    with open('intensity.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()
        
    #for i in range(0,len(similarity)):
    #    print(similarity[i])
    
    cap.release()
    cv2.destroyAllWindows()
