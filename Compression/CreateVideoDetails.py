import os
from pathlib import Path, PureWindowsPath

def generateDetailsName(corePath, inputVideoName):
    stat = '"' + corePath + "\\Stats\\" + inputVideoName.split('.')[0] + "\\" + inputVideoName.split('.')[0] + "_details.txt" + '"'
    return stat

def CreateVideoDetail(corePath, inputVideoName, mediaInfo):
    VideoPath = corePath + "\\Input\\" + inputVideoName
    details = generateDetailsName(corePath, inputVideoName)
    os.chdir(mediaInfo)
    os.getcwd()
    name = subprocess.check_output('MediaInfo.exe --Inform="General;name=%FileNameExtension%" "$@" ' +VideoPath, shell=True).decode('utf-8')
    duration = subprocess.check_output('MediaInfo.exe --Inform="General;duration=%Duration%" "$@" ' +VideoPath, shell=True).decode('utf-8')
    vbitrate = subprocess.check_output('MediaInfo.exe --Inform="Video;videobitrate=%BitRate%" "$@" ' +VideoPath, shell=True).decode('utf-8')
    width = subprocess.check_output('MediaInfo.exe --Inform="Video;width=%Width%" "$@" ' +VideoPath, shell=True).decode('utf-8')
    height = subprocess.check_output('MediaInfo.exe --Inform="Video;height=%Height%" "$@" ' +VideoPath, shell=True).decode('utf-8')
    framerate = subprocess.check_output('MediaInfo.exe --Inform="General;framerate=%FrameRate%" "$@" ' +VideoPath, shell=True).decode('utf-8')
    size = subprocess.check_output('MediaInfo.exe --Inform="General;streamsize=%FileSize%" "$@" ' +VideoPath, shell=True).decode('utf-8')
    format = subprocess.check_output('MediaInfo.exe --Inform="General;format=%Format%" "$@" ' +VideoPath, shell=True).decode('utf-8')
    #print(size)
    
    
def CreateCompVideoDetail(corePath, inputVideoName, mediaInfo):

    videoname=inputVideoName.split('.')[0]       #video name without extenssion
    mypath = corePath + "\\Compressed\\"+videoname   # path to compressed videos
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for video_name in onlyfiles:
        os.chdir(mediaInfo)
        os.getcwd()
        VideoPath = mypath +"\\"+ video_name
        name = subprocess.check_output('MediaInfo.exe --Inform="General;name=%FileNameExtension%" "$@" ' + VideoPath,
                                       shell=True).decode('utf-8')
        duration = subprocess.check_output('MediaInfo.exe --Inform="General;duration=%Duration%" "$@" ' + VideoPath,
                                           shell=True).decode('utf-8')
        vbitrate = subprocess.check_output('MediaInfo.exe --Inform="Video;videobitrate=%BitRate%" "$@" ' + VideoPath,
                                           shell=True).decode('utf-8')
        width = subprocess.check_output('MediaInfo.exe --Inform="Video;width=%Width%" "$@" ' + VideoPath,
                                        shell=True).decode('utf-8')
        height = subprocess.check_output('MediaInfo.exe --Inform="Video;height=%Height%" "$@" ' + VideoPath,
                                         shell=True).decode('utf-8')
        framerate = subprocess.check_output('MediaInfo.exe --Inform="General;framerate=%FrameRate%" "$@" ' + VideoPath,
                                            shell=True).decode('utf-8')
        size = subprocess.check_output('MediaInfo.exe --Inform="General;streamsize=%FileSize%" "$@" ' + VideoPath,
                                       shell=True).decode('utf-8')
        format = subprocess.check_output('MediaInfo.exe --Inform="General;format=%Format%" "$@" ' + VideoPath,
                                         shell=True).decode('utf-8')
        #print(name)
