import pandas as pd
from os import listdir
from os.path import isfile, join
import Compression as cf
import FeatureExtraction.Feature_Extraction as fe
import os
from pathlib import Path, PureWindowsPath

corePath = Path()
ffmpeg = '"' + str(PureWindowsPath(Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/ffmpeg/ffmpeg.exe"))) + '"'
mkvmerge = '"' + str(PureWindowsPath(Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/MKVToolNix/mkvmerge.exe"))) + '"'
mediaInfo = <path>
videoFileList = [f for f in listdir(corePath) if isfile(join(corePath, f))]
presets = ['superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower']
df_for_video_data = pd.DataFrame(columns=['Video Name','Frames per Second','Total No. of Scenes','Avg Motion %','Avg PCC','Avg Intensity','Preset Name'])
for video in videoFileList:
    print("Processing file : " + video)
    features_array = fe.feature_extr(corePath + "\\Input\\" + video)
    for preset in presets:
        df_for_video_data.loc[len(df_for_current_video)] = features_array + [preset]
    cf.compressFunc.compressdis(corePath, video, presets, ffmpeg, mkvmerge)
    cf.CreateVideoDetails.CreateVideoDetail(corePath, video, mediaInfo)
