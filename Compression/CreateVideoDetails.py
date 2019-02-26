import os
import subprocess
from os import listdir
from os.path import isfile, join

def CreateVideoDetail(corePath, inputVideoName, mediaInfo):
    videoPath = '"' + corePath + "\\Input\\" + inputVideoName + '"'
    print("Creating input video details")
    # print(videoPath)
    os.chdir(mediaInfo.replace("\\", "/"))
    os.getcwd()
    name = subprocess.check_output('MediaInfo.exe --Inform="General;%FileNameExtension%" "$@" ' + videoPath, shell=True).decode('utf-8').rstrip()
    duration = subprocess.check_output('MediaInfo.exe --Inform="General;%Duration%" "$@" ' + videoPath, shell=True).decode('utf-8').rstrip()
    vbitrate = subprocess.check_output('MediaInfo.exe --Inform="Video;%BitRate%" "$@" ' + videoPath, shell=True).decode('utf-8').rstrip()
    width = subprocess.check_output('MediaInfo.exe --Inform="Video;%Width%" "$@" ' + videoPath, shell=True).decode('utf-8').rstrip()
    height = subprocess.check_output('MediaInfo.exe --Inform="Video;%Height%" "$@" ' + videoPath, shell=True).decode('utf-8').rstrip()
    framerate = subprocess.check_output('MediaInfo.exe --Inform="General;%FrameRate%" "$@" ' + videoPath, shell=True).decode('utf-8').rstrip()
    size = subprocess.check_output('MediaInfo.exe --Inform="General;%FileSize%" "$@" ' + videoPath, shell=True).decode('utf-8').rstrip()
    format = subprocess.check_output('MediaInfo.exe --Inform="General;%Format%" "$@" ' + videoPath, shell=True).decode('utf-8').rstrip()
    #print(size)
    # index_list = video_dataframe.index[video_dataframe['Video Name'] == videoPath].tolist()
    #
    # for i in index_list:
    #     video_dataframe['Video Length'][i] = duration
    #     video_dataframe['Original Bitrate'][i] = vbitrate
    #     video_dataframe['Width'][i] = width
    #     video_dataframe['Height'][i] = height
    #     video_dataframe['Frames per Second'][i] = framerate
    #     video_dataframe['Original Size'][i] = size

    print('Input Video Details acquired')
    return [duration, vbitrate, width, height, framerate, size]

def CreateCompVideoDetail(corePath, inputVideoName, mediaInfo):
    originalVideoPath = '"' + corePath + "\\Input\\" + inputVideoName + '"'
    compressedVideosPath = corePath + "\\Output\\" + inputVideoName.split('.')[0] + "\\"  # path to compressed videos
    print("Creating compressed video details")
    # print(compressedVideosPath)
    videoFileList = [f for f in listdir(compressedVideosPath) if isfile(join(compressedVideosPath, f))]
    preset_wise_features = []
    for video in videoFileList:
        os.chdir(mediaInfo.replace("\\", "/"))
        os.getcwd()
        videoPath = '"' + compressedVideosPath + "\\" + video + '"'
        name = subprocess.check_output('MediaInfo.exe --Inform="General;%FileNameExtension%" "$@" ' + videoPath,
                                       shell=True).decode('utf-8')
        duration = subprocess.check_output('MediaInfo.exe --Inform="General;%Duration%" "$@" ' + videoPath,
                                           shell=True).decode('utf-8')
        vbitrate = subprocess.check_output('MediaInfo.exe --Inform="Video;%BitRate%" "$@" ' + videoPath,
                                           shell=True).decode('utf-8').rstrip()
        width = subprocess.check_output('MediaInfo.exe --Inform="Video;%Width%" "$@" ' + videoPath,
                                        shell=True).decode('utf-8')
        height = subprocess.check_output('MediaInfo.exe --Inform="Video;%Height%" "$@" ' + videoPath,
                                         shell=True).decode('utf-8')
        framerate = subprocess.check_output('MediaInfo.exe --Inform="General;%FrameRate%" "$@" ' + videoPath,
                                            shell=True).decode('utf-8')
        size = subprocess.check_output('MediaInfo.exe --Inform="General;%FileSize%" "$@" ' + videoPath,
                                       shell=True).decode('utf-8').rstrip()
        format = subprocess.check_output('MediaInfo.exe --Inform="General;%Format%" "$@" ' + videoPath,
                                         shell=True).decode('utf-8')
        # print(vbitrate)

        preset_for_given_video = name.split('_')[len(name.split('_'))-1].split('.')[0]

        # index_for_preset = video_dataframe.index[(video_dataframe['Video Name'] == originalVideoPath) & (video_dataframe['Compression Preset'] == preset_for_given_video)].tolist()[0]
        #
        # video_dataframe['Compressed Bitrate'][index_for_preset] = vbitrate
        # video_dataframe['Compressed Size'][index_for_preset] = size

        preset_wise_features.append([preset_for_given_video,vbitrate,size])

    print('Compressed Video Details acquired')
    return preset_wise_features

def retrieveCompressionDetail(corePath, inputVideoName):
    originalVideoPath = '"' + corePath + "\\Input\\" + inputVideoName + '"'
    compressionDetailPath = corePath + "\\Stats\\" + inputVideoName.split('.')[0] + "\\"   #path to compressed videos
    txtFileList = [f for f in listdir(compressionDetailPath) if isfile(join(compressionDetailPath, f))]
    preset_wise_features = []
    for txtFile in txtFileList:
        f = open(compressionDetailPath + txtFile, "r")
        searchlines2 = f.readlines()
        f.close()
        for line in searchlines2:
            if "encoded" in line:
                r6=line
                break
        # print(r6)
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
        print("Compression Duration = "+compressionTime)

        totalFrames = fram.replace(" ", "")
        print("Frame Count = "+totalFrames)

        preset_for_given_video = txtFile.split('_')[len(txtFile.split('_'))-2]

        # index_for_preset = video_dataframe.index[(video_dataframe['Video Name'] == originalVideoPath) & (video_dataframe['Compression Preset'] == preset_for_given_video)].tolist()[0]
        #
        # video_dataframe['Compression Duration'][index_for_preset] = compressionTime
        # video_dataframe['Frame Count'][index_for_preset] = totalFrames

        preset_wise_features.append([preset_for_given_video,compressionTime,totalFrames])

    return preset_wise_features
