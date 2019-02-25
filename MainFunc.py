import pandas as pd
from os import listdir
from os.path import isfile, join
from Compression import compressFunc,CreateVideoDetails
from FeatureExtraction import Feature_Extraction
from pathlib import Path, PureWindowsPath

corePath = str(PureWindowsPath(Path("E:/New folder")))
ffmpeg = '"' + str(PureWindowsPath(Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/ffmpeg/ffmpeg.exe"))) + '"'
mkvmerge = '"' + str(PureWindowsPath(Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/MKVToolNix/mkvmerge.exe"))) + '"'
mediaInfo = str(PureWindowsPath(Path("E:/New folder/MediaInfo/")))
VQMT = '"' + str(PureWindowsPath(Path("E:/VQMT/VQMT.exe"))) + '"'
videoFileList = [f for f in listdir(corePath + "\\Input\\") if isfile(join(corePath + "\\Input\\", f))]
presets = ['superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower']
presets1 = ['superfast', 'veryfast']
df_for_video_data = pd.DataFrame(columns=['Video Name','Width', 'Height', 'Video Length', 'Frames per Second',
                'Frame Count', 'Original Bitrate', 'Original Size', 'Scene Count', 'Avg Motion %',
                'Avg PCC', 'Avg Intensity', 'Compression Preset','Compression Duration', 'Compressed Bitrate', 'Compressed Size'])
for video in videoFileList:
    print("Processing file : " + video)

    Feature_Extraction.feature_extr(corePath + "\\Input\\" + video, df_for_video_data, presets)
    compressFunc.compressdis(corePath, video, presets1, ffmpeg, mkvmerge)
    CreateVideoDetails.CreateVideoDetail(corePath, video, mediaInfo, df_for_video_data)
    CreateVideoDetails.CreateCompVideoDetail(corePath, video, mediaInfo, df_for_video_data)
    CreateVideoDetails.retrieveCompressionDetail(corePath, video, df_for_video_data)
    vqmt.videoQualityMeasure(corePath, video, compressedVideo, width, height, frames, ffmpeg, vqmt)
