import os
from pathlib import Path, PureWindowsPath

def generateDetailsName(corePath, inputVideoName):
    stat = '"' + corePath + "\\Stats\\" + inputVideoName.split('.')[0] + "\\" + inputVideoName.split('.')[0] + "_details.txt" + '"'
    return stat

def CreateVideoDetail(corePath, inputVideoName, mediaInfo):
    video = corePath + "\\Input\\" + inputVideoName
    details = generateDetailsName(corePath, inputVideoName)
    os.chdir(mediaInfo)
    os.getcwd()
    os.system('"MediaInfo.exe" '+ video +' >' + details)
