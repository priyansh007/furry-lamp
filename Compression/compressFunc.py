import os
from pathlib import Path, PureWindowsPath

def createAVS(corePath, inputVideo, avs):
    file = open(avs,'w')
    file.write('LoadPlugin("E:\\N.I.B.B.A.S\\StaxRip 1.9.0.0\\Apps\\Plugins\\avs\\L-SMASH-Works\\LSMASHSource.dll")\n')
    file.write('LSMASHVideoSource("' + corePath + '\\Input\\' + inputVideo + '", format = "YUV420P8")')
    file.close()

def generateAVSName(corePath, inputVideoName):
    avs = corePath + "\\AVS\\" + inputVideoName.split('.')[0] + "_avs.avs"
    return avs

def generateIntermediateVideoName(corePath, inputVideoName, presetName):
    iv = '"' + corePath + "\\Intermediate\\" + inputVideoName.split('.')[0] + "\\" + inputVideoName.split('.')[0] + "_intermediateVideo_" + presetName + ".mkv" + '"'
    return iv

def generateOutputVideoName(corePath, inputVideoName, presetName):
    ov = '"' + corePath + "\\Output\\" + inputVideoName.split('.')[0] + "\\" + inputVideoName.split('.')[0] + "_outputVideo_" + presetName + ".mkv" + '"'
    return ov

def generateAudioName(corePath, inputVideoName):
    audio = '"' + corePath + "\\Audio\\" + inputVideoName.split('.')[0] + "_audio.mka" + '"'
    return audio

def generateBatName(corePath, inputVideoName):
    bat = corePath + "\\BAT\\" + inputVideoName.split('.')[0] +  "_batchFile.bat"
    return bat

def generateStatsName(corePath, inputVideoName, presetName):
    stat = '"' + corePath + "\\Stats\\" + inputVideoName.split('.')[0] + "\\" + inputVideoName.split('.')[0] + "_" + presetName + "_stats.txt" + '"'
    return stat

def compressdis(corePath, inputVideo, presets, ffmpeg, mkvmerge):
    avs = generateAVSName(corePath, inputVideo)
    audio = generateAudioName(corePath, inputVideo)
    createAVS(corePath, inputVideo, avs)
    bat = generateBatName(corePath, inputVideo)
    audioSeperator = ffmpeg + ' -i "' + corePath + '\\Input\\' + inputVideo + '" -vn -acodec copy ' + audio
    outputDir = corePath + "\\Output\\" + inputVideo.split('.')[0] + "\\"
    intermediateDir = corePath + "\\Intermediate\\" + inputVideo.split('.')[0] + "\\"
    statsDir = corePath + "\\Stats\\" + inputVideo.split('.')[0] + "\\"
    os.makedirs(outputDir.replace("\\", "/"))
    os.makedirs(intermediateDir.replace("\\", "/"))
    os.makedirs(statsDir.replace("\\", "/"))
    file = open(bat,'w')
    file.write(audioSeperator)
    file.write("\n")
    for presetName in presets:
        intermediateVideo = generateIntermediateVideoName(corePath, inputVideo, presetName)
        outputVideo = generateOutputVideoName(corePath, inputVideo, presetName)
        compressionDurationStats = generateStatsName(corePath, inputVideo, presetName)
        compressor = ffmpeg + ' -i "' + avs + '" -c:v libx265 -preset ' + presetName + ' -tune psnr -an -y -hide_banner ' + intermediateVideo + ' 2>' + compressionDurationStats
        merger = mkvmerge + ' -o ' + outputVideo + ' ' + intermediateVideo + ' --audio-tracks 0 --language 0:eng --default-track 0:0 --forced-track 0:0 ' + audio + ' --ui-language en'
        file.write(compressor)
        file.write("\n")
        file.write(merger)
        file.write("\n")
    file.close()
    os.system('"' + bat + '"')
