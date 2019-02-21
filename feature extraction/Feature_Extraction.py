import cv2
from scipy.stats import pearsonr
import numpy as np
from math import ceil
from os import listdir
from os.path import isfile, join
import pandas as pd


video_folder = "D:/Academics/Sem-7(2018-19)/Project/Feature Extraction/Videos/"
video_list = [f for f in listdir(video_folder) if isfile(join(video_folder, f))]

presets = ['superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower']
df_for_current_video = pd.DataFrame(columns=['Video Name','Frames per Second','Total No. of Scenes','Avg Motion %','Avg PCC','Preset Name'])

def feature_extr(video_name):
    cap = cv2.VideoCapture(video_name)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    fps = cap.get(cv2.CAP_PROP_FPS)

    looper,image=cap.read()

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
    cv2.imwrite("temp.jpg", frame)

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
            imS2 = cv2.resize(fgmask, (800, 600))
            white_count = cv2.countNonZero(imS2)
            white_ratio = white_count/4800

            # Pearson Correlation Coefficient
            if cv2.imread("temp.jpg") is not None:
                old_frame = cv2.imread("temp.jpg")
                a1 = np.array(old_frame)
                a2 = np.array(frame)
                if a1.shape == a2.shape:
                    corr, p_value = pearsonr(a1.flatten(),a2.flatten() )

            cv2.imwrite("temp.jpg", frame)

            # Display Original Video and Motion Detection
            # cv2.imshow('fgmask',imS)
            # cv2.imshow('frame',imS2)

            # For Scene Changes
            if white_ratio > min_mp and flag!=1 :
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
        x[4]= x[3]/(x[2]-x[1])
        x[6]= x[5]/(x[2]-x[1])
        total_mp = total_mp + x[3]
        total_pcc = total_pcc + x[5]
        total_frames= total_frames + x[2] - x[1]

    # Average Motion Percentage and PCC for entire video
    avg_mp = total_mp/total_frames
    avg_pcc = total_pcc//total_frames

    avg_mp_rounded = str(round(avg_mp,3))+" %"
    avg_pcc_rounded = str(round(avg_pcc,3))+" %"

    # Append features to dataframe for all 7 presets
    for p in presets:
        df_for_current_video.loc[len(df_for_current_video)] = [video_name, str(fps), str(len(scene)), avg_mp_rounded, avg_pcc_rounded, p]

    cap.release()
    cv2.destroyAllWindows()

# Extract Features from Every Video
for video_name in video_list:
    feature_extr(video_folder+video_name)
