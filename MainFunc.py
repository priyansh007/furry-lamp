import pandas as pd
import time
from os import listdir
from os.path import isfile, join
from Compression import compressFunc,CreateVideoDetails,vqmt,writeCSV
from FeatureExtraction import Feature_Extraction

corePath = "D:\\Video Compression\\Files"
ffmpeg = '"D:\\Video Compression\\Staxrip.2.0.0.0.x64\\Apps\\Encoders\\ffmpeg\\ffmpeg.exe"'
mkvmerge = '"D:\\Video Compression\\Staxrip.2.0.0.0.x64\\Apps\\Support\\MKVToolNix\\mkvmerge.exe"'
mediaInfo = "D:\\Video Compression\\MediaInfo\\"
VQMT = '"D:\\Video Compression\\VQMT\\VQMT.exe"'
outputDataset = corePath + "\\Dataset\\outputDataset.csv"
videoFileList = [f for f in listdir(corePath + "\\Input\\") if isfile(join(corePath + "\\Input\\", f))]
presets = ['superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower']
presets2 = ['superfast']
df_for_video_data = pd.DataFrame(columns=['Video Name','Width', 'Height', 'Video Length', 'Frames per Second',
                'Frame Count', 'Original Bitrate', 'Original Size', 'Scene Count', 'Avg Motion %',
                'Avg PCC', 'Compression Preset','Compression Duration', 'Compressed Bitrate', 'Compressed Size'])
print('Obtained videos are : ',videoFileList)
file = open(outputDataset,'w+')
file.write('Video Name,Width,Height,Video Length,Frames per Second,Frame Count,Original Bitrate,Original Size,Scene Count,Avg Motion %,Avg PCC,Compression Preset,Compression Duration,Compressed Bitrate,Compressed Size, Average PSNR, Average SSIM, Average VIFp')
file.close()
for video in videoFileList:
    logFile = corePath + "\\" + video.split(".")[0] + "_log.txt"
    try:
        log = open(logFile, 'w+')
        print("Processing file : " + video)
        log.write("Processing file : " + video)
        log.close()
        start = time.time()
        features_of_original_video = Feature_Extraction.feature_extr(corePath + "\\Input\\" + video, logFile)
        end = time.time()
        feTime = end - start
        print('Feature Extraction took ' + time.strftime("%H:%M:%S", time.gmtime(feTime)))
        log = open(logFile, 'a')
        log.write('\nFeature Extraction took ' + time.strftime("%H:%M:%S", time.gmtime(feTime)))
        log.close()
    
        start = time.time()
        compressFunc.compressdis(corePath, video, presets, ffmpeg, mkvmerge, logFile)
        details_of_original_video = CreateVideoDetails.CreateVideoDetail(corePath, video, mediaInfo, logFile)
        preset_wise_bitrate_and_size = CreateVideoDetails.CreateCompVideoDetail(corePath, video, mediaInfo, logFile)
        preset_wise_duration_and_frames = CreateVideoDetails.retrieveCompressionDetail(corePath, video, logFile)
        end = time.time()
        clTime = end - start
        print('Compression and Logging took ' + time.strftime("%H:%M:%S", time.gmtime(clTime)))
        log = open(logFile, 'a')
        log.write('\nCompression and Logging took ' + time.strftime("%H:%M:%S", time.gmtime(clTime)))
        log.close()
    
        start = time.time()
        presetWiseQualityDetails = vqmt.videoQualityMeasure(corePath, video, presets, details_of_original_video[3], details_of_original_video[2], preset_wise_duration_and_frames[0][2], ffmpeg, VQMT, logFile)
        end = time.time()
        vqmtTime = end - start
        print('Video Quality Measurement took ' + time.strftime("%H:%M:%S", time.gmtime(vqmtTime)))
        log = open(logFile, 'a')
        log.write('\nVideo Quality Measurement took ' + time.strftime("%H:%M:%S", time.gmtime(vqmtTime)))
        log.close()
    
        writeCSV.writeCSV(outputDataset, presets, features_of_original_video, details_of_original_video, preset_wise_bitrate_and_size, preset_wise_duration_and_frames, presetWiseQualityDetails, logFile)
    
        totalProcessTime = float(feTime) + float(clTime) + (vqmtTime)
        print('Processing complete\nTotal Processing Time : ' + time.strftime("%H:%M:%S", time.gmtime(totalProcessTime)))
        log = open(logFile, 'a')
        log.write('\nProcessing complete\nTotal Processing Time : ' + time.strftime("%H:%M:%S", time.gmtime(totalProcessTime)))
        log.close()
    except Exception as e:
        log = open(logFile, 'a')
        print(str(e))
        log.write('\n' + str(e))
        log.close()
        continue