import cv2
from scipy.stats import pearsonr
import numpy as np
from math import ceil
from os import listdir
from os.path import isfile, join
import csv
#from xlwt import Workbook 

mypath = "./Videos/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
video_count = 1
    
def feature_extr(video_name,video_count):
    print("Video Name is "+video_name)
    #sheet1.write(0, video_count, video_count)
    #sheet1.write(1, video_count, video_name) 
    cap = cv2.VideoCapture(video_name)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    #fps = math.floor(cap.get(cv2.CAP_PROP_FPS))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("\n\nFrames per Second = "+str(fps))
    #sheet1.write(2, video_count, str(fps))
    
    looper,image=cap.read()
    #count=0
    #looper=True
    #size = 600, 400
    
    # Scene change
    # Scene = [SCENE NO., 1st FRAME, LAST FRAME, TOTAL MOTION, AVG MOTION, TOTAL CORRELATION, AVG CORRELATION]
    scene = np.array([[0,0,0,0,0,0,0]])
    i=0
    sum_mp = 0
    sum_pcc = 0
    min_mp = 80
    flag = 0
    
    
    number=fps*0.1
    num=ceil(number)
    ret, frame = cap.read()
    cv2.imwrite("asd.jpg", frame)

    #print(scene)
    while(1):
        i+=1
        
        k=0
        ret = False
        while(k<num-1):
            ret, frame = cap.read()
            fgmask = fgbg.apply(frame)
            k=k+1
        
        if ret :
            # Motion percentage
            #imS = cv2.resize(frame, (800, 600)) 
            imS2 = cv2.resize(fgmask, (800, 600))
            white_count = cv2.countNonZero(imS2)
            white_ratio = white_count/4800
            #print("\nMotion percentage = "+str(round(white_ratio,2))+" %")
            
            # Pearson Correlation Coefficient
            if cv2.imread("asd.jpg") is not None:
                old_frame = cv2.imread("asd.jpg")
                a1 = np.array(old_frame)
                a2 = np.array(frame)
                if a1.shape == a2.shape:
                    corr, p_value = pearsonr(a1.flatten(),a2.flatten() )
                    #print(a1.flatten())
                    #print(a2.flatten())
                    #print("Correlation = "+str(round(corr*100,3))+" P-value = "+str(p_value)+"\n\n")
                
            cv2.imwrite("asd.jpg", frame)
            
            # Display Original Video and Motion Detection
            # cv2.imshow('fgmask',imS)
            # cv2.imshow('frame',imS2)
            
            # For Scene Changes
            if white_ratio > min_mp and flag!=1 :
                print("SCENE CHANGED")
                flag = 1
                scene[-1][2] = i
                scene[-1][3] = sum_mp
                scene[-1][5] = sum_pcc
                scene = np.vstack([scene,[scene[-1][0]+1,i,0,0,0,0,0]])
                sum_mp = 0
                sum_pcc = 0
                
            if white_ratio < min_mp:
                flag = 0
                sum_mp+= white_ratio
                sum_pcc+=round(corr*100,3)
        else :
            break
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    
    # Data for the Last Scene
    scene[-1][2] = i
    scene[-1][3] = sum_mp
    scene[-1][5] = sum_pcc
    
    
    # Average Motion Percentage and Average PCC for each Scene
    total_mp=0
    total_pcc=0
    total_frames=0
    for x  in scene:
        print(x)
        x[4]= x[3]/(x[2]-x[1])
        x[6]= x[5]/(x[2]-x[1])
        total_mp = total_mp + x[3]
        total_pcc = total_pcc + x[5]
        total_frames= total_frames + x[2] - x[1]
        
    # Average Motion Percentage for entire video
    avg_mp = total_mp/total_frames
    avg_pcc = total_pcc//total_frames
    print ("\n\nScene Table will be")
    print(scene)
    
    print ("\n\nTotal Number of Scenes ="+str(len(scene)))
    
    #sheet1.write(3, video_count, str(len(scene)))
    
    avg_mp_rounded = str(round(avg_mp,3))+" %"
    print ("\n\nAverage Motion Percentage for video = "+avg_mp_rounded)
    #sheet1.write(4, video_count, avg_mp_rounded)
    
    avg_pcc_rounded = str(round(avg_pcc,3))+" %"
    print ("\n\nAverage PCC for video = "+avg_pcc_rounded)
    #sheet1.write(5, video_count, avg_pcc_rounded)
    with open('video_features.csv', mode='a') as csv_file:
        fieldnames = ['Sr. No.','Video Name','Frames per Second','Total Number of Scenes','Avg Motion Percentage','Avg PCC']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Sr. No.': video_count,'Video Name': video_name,'Frames per Second': str(fps),'Total Number of Scenes': str(len(scene)),'Avg Motion Percentage': avg_mp_rounded,'Avg PCC': avg_pcc_rounded})
    
    
    #img=cv2.imread("frame10.jpg")
    cap.release()
    cv2.destroyAllWindows()


# Workbook is created 
#wb = Workbook() 
#sheet1 = wb.add_sheet('Features Extraction')  

# Setting Column Names
#sheet1.write(0, 0, 'Sr. No.')
#sheet1.write(1, 0, 'Video Name') 
#sheet1.write(2, 0, 'Frames per Second') 
#sheet1.write(3, 0, 'Total Number of Scenes') 
#sheet1.write(4, 0, 'Avg Motion Percentage') 
#sheet1.write(5, 0, 'Avg PCC')  


for video_name in onlyfiles:
    #print("Feature Extraction started for "+video_name+"\n\n")
    print("video_count is "+str(video_count))
    feature_extr(mypath+video_name,video_count)
    video_count+=1
#wb.save('features.xls')