import cv2
from scipy.stats import pearsonr
import numpy as np
from math import ceil

def feature_extr(video_name, video_dataframe, presets_list):
    print("Feature Extraction started.")
    cap = cv2.VideoCapture(video_name)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    fps = cap.get(cv2.CAP_PROP_FPS)
    similarity=[]

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

            if cv2.imread("temp.jpg") is not None:
                old_frame = cv2.imread("temp.jpg")

                # Pearson Correlation Coefficient
                a1 = np.array(old_frame)
                a2 = np.array(frame)
                if a1.shape == a2.shape:
                    corr, p_value = pearsonr(a1.flatten(),a2.flatten() )

                # Intensity
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

    # Frame by Frame Intensity comparison
    avg_intensity=sum(similarity) / float(len(similarity))
    final_avg_intensity=(avg_intensity/max(similarity))*100

    cap.release()
    cv2.destroyAllWindows()

    # Append features to dataframe for all 7 presets

    for preset in presets_list:
        video_dataframe['Video Name'][len(video_dataframe)] = video_name
        # video_dataframe.['Frames per Second'][len(video_dataframe)] = str(fps)
        video_dataframe['Scene Count'][len(video_dataframe)] = str(len(scene))
        video_dataframe['Avg Motion %'][len(video_dataframe)] = avg_mp_rounded
        video_dataframe['Avg PCC'][len(video_dataframe)] = avg_pcc_rounded
        video_dataframe['Avg Intensity'][len(video_dataframe)] = final_avg_intensity
        video_dataframe['Compression Preset'][len(video_dataframe)] = preset

    print("Feature Extraction completed for "+video_name+" .")

    # return video_dataframe
