import cv2
from scipy.stats import pearsonr
import numpy as np
from math import ceil, isnan


def feature_extr(video_name, logFile, short_video_name):
    try:
        print("Feature Extraction started for " + short_video_name)
        log = open(logFile, 'a')
        log.write("\nFeature Extraction started for " + short_video_name)
        log.close()
        cap = cv2.VideoCapture(video_name)
        fgbg = cv2.createBackgroundSubtractorMOG2()
        fps = cap.get(cv2.CAP_PROP_FPS)
        # similarity=[]
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        #print('Width = '+str(width))
        #print('Height ='+str(height))

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
                imS2 = cv2.resize(fgmask, (int(width), int(height)))
                white_count = cv2.countNonZero(imS2)
                white_ratio = white_count*100/(width*height)

                if cv2.imread("temp.jpg") is not None:
                    old_frame = cv2.imread("temp.jpg")

                    # Pearson Correlation Coefficient
                    a1 = np.array(old_frame)
                    a2 = np.array(frame)
                    if a1.shape == a2.shape:
                        try:
                            corr, p_value = pearsonr(a1.flatten(),a2.flatten() )
                        except Exception as e:
                            print('pearson error ' + e)
                            continue
                        if isnan(corr):
                            corr=1

                    # Intensity
                    # sift = cv2.xfeatures2d.SIFT_create()
                    # kp_1, desc_1 = sift.detectAndCompute(old_frame, None)
                    # kp_2, desc_2 = sift.detectAndCompute(frame, None)
                    # index_params = dict(algorithm=0, trees=5)
                    # search_params = dict()
                    # flann = cv2.FlannBasedMatcher(index_params, search_params)
                    # matches = flann.knnMatch(desc_1, desc_2, k=2)
                    # good_points=[]
                    # ratio = 0.6
                    # for m, n in matches:
                    #     if m.distance < ratio*n.distance:
                    #         good_points.append(m)
                    # similarity.append(len(good_points))

                cv2.imwrite("temp.jpg", frame)

                # Display Original Video and Motion Detection
                # cv2.imshow('fgmask',imS)
                # cv2.imshow('frame',imS2)

                # For Scene Changes
                if white_ratio > min_mp and flag!=1 :
                    flag = 1
                    scene[-1][2] = i
                    try:
                        scene[-1][3] = sum_mp
                        scene[-1][5] = sum_pcc
                    except:
                        scene[-1][3] = 0
                        scene[-1][5] = 0
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
        avg_pcc = total_pcc/total_frames

        avg_mp_rounded = str(round(avg_mp,3)/100)
        avg_pcc_rounded = str(round(avg_pcc,3)/100)

        # Frame by Frame Intensity comparison
        # avg_intensity=sum(similarity) / float(len(similarity))
        # final_avg_intensity=(avg_intensity/max(similarity))*100

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(e)
        log = open(logFile, 'a')
        log.write("\n" + str(e))
        log.close()
        avg_mp_rounded = '0'
        avg_pcc_rounded = '0'
        scene = []

    if os.path.isfile('temp.jpg'):
            os.remove('temp.jpg')
            
    print("Feature Extraction completed for " + short_video_name)     
    print("Scene Count: " + str(len(scene)) + "\nAverage Motion: " + str(avg_mp_rounded) + "\nAverage PCC: " + str(avg_pcc_rounded))

    log = open(logFile, 'a')
    log.write("\nFeature Extraction completed for " + short_video_name)
    log.write("\nScene Count: " + str(len(scene)) + "\nAverage Motion: " + str(avg_mp_rounded) + "\nAverage PCC: " + str(avg_pcc_rounded))
    log.close()

    return [short_video_name, str(len(scene)), str(avg_mp_rounded), str(avg_pcc_rounded)]
