import os
import subprocess
from os import listdir
from os.path import isfile, join
from pathlib import Path, PureWindowsPath

def CreateVideoDetail(corePath, inputVideoName, mediaInfo):
    videoPath = '"' + corePath + "\\Input\\" + inputVideoName + '"'
    print("Creating input video details")
    print(videoPath)
    os.chdir(mediaInfo.replace("\\", "/"))
    os.getcwd()
    name = subprocess.check_output('MediaInfo.exe --Inform="General;name=%FileNameExtension%" "$@" ' + videoPath, shell=True).decode('utf-8')
    duration = subprocess.check_output('MediaInfo.exe --Inform="General;duration=%Duration%" "$@" ' + videoPath, shell=True).decode('utf-8')
    vbitrate = subprocess.check_output('MediaInfo.exe --Inform="Video;videobitrate=%BitRate%" "$@" ' + videoPath, shell=True).decode('utf-8')
    width = subprocess.check_output('MediaInfo.exe --Inform="Video;width=%Width%" "$@" ' + videoPath, shell=True).decode('utf-8')
    height = subprocess.check_output('MediaInfo.exe --Inform="Video;height=%Height%" "$@" ' + videoPath, shell=True).decode('utf-8')
    framerate = subprocess.check_output('MediaInfo.exe --Inform="General;framerate=%FrameRate%" "$@" ' + videoPath, shell=True).decode('utf-8')
    size = subprocess.check_output('MediaInfo.exe --Inform="General;streamsize=%FileSize%" "$@" ' + videoPath, shell=True).decode('utf-8')
    format = subprocess.check_output('MediaInfo.exe --Inform="General;format=%Format%" "$@" ' + videoPath, shell=True).decode('utf-8')
    print(size)
    
    
def CreateCompVideoDetail(corePath, inputVideoName, mediaInfo):
    compressedVideosPath = corePath + "\\Output\\" + inputVideoName.split('.')[0] + "\\"  # path to compressed videos
    print("Creating compressed video details")
    print(compressedVideosPath)
    videoFileList = [f for f in listdir(compressedVideosPath) if isfile(join(compressedVideosPath, f))]
    for video in videoFileList:
        os.chdir(mediaInfo.replace("\\", "/"))
        os.getcwd()
        videoPath = '"' + compressedVideosPath + "\\" + video + '"'
        name = subprocess.check_output('MediaInfo.exe --Inform="General;name=%FileNameExtension%" "$@" ' + videoPath,
                                       shell=True).decode('utf-8')
        duration = subprocess.check_output('MediaInfo.exe --Inform="General;duration=%Duration%" "$@" ' + videoPath,
                                           shell=True).decode('utf-8')
        vbitrate = subprocess.check_output('MediaInfo.exe --Inform="Video;videobitrate=%BitRate%" "$@" ' + videoPath,
                                           shell=True).decode('utf-8')
        width = subprocess.check_output('MediaInfo.exe --Inform="Video;width=%Width%" "$@" ' + videoPath,
                                        shell=True).decode('utf-8')
        height = subprocess.check_output('MediaInfo.exe --Inform="Video;height=%Height%" "$@" ' + videoPath,
                                         shell=True).decode('utf-8')
        framerate = subprocess.check_output('MediaInfo.exe --Inform="General;framerate=%FrameRate%" "$@" ' + videoPath,
                                            shell=True).decode('utf-8')
        size = subprocess.check_output('MediaInfo.exe --Inform="General;streamsize=%FileSize%" "$@" ' + videoPath,
                                       shell=True).decode('utf-8')
        format = subprocess.check_output('MediaInfo.exe --Inform="General;format=%Format%" "$@" ' + videoPath,
                                         shell=True).decode('utf-8')
        print(vbitrate)

def retrieveCompressionDetail(corePath, inputVideoName):
    compressionDetailPath = corePath + "\\Stats\\" + inputVideoName.split('.')[0] + "\\"   #path to compressed videos
    txtFileList = [f for f in listdir(compressionDetailPath) if isfile(join(compressionDetailPath, f))]
    for txtFile in txtFileList:
        f = open(compressionDetailPath + txtFile, "r")
        searchlines2 = f.readlines()
        f.close()
        for line in searchlines2:
            if "encoded" in line:
                r6=line
                break
        print(r6)
        flag=0
        fram=""
        totaltime=""
        c=2
        for i in r6:
            if i is " " and flag is 0:
                flag=1
                continue
            if flag is 1:
                if i is " ":
                    flag=2
                    continue
                fram+=i
            if flag is 2:
                if i is " ":
                    c-=1
                if c is 0:
                    if i is 's':
                        break
                    totaltime+=i
        compressionTime = totaltime.replace(" ", "")                
        print(compressionTime)        
        totalFrames = fram.replace(" ", "")                
        print(totalFrames)
