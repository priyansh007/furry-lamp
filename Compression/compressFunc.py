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
    iv = '"' + corePath + "\\Intermediate\\" + inputVideoName.split('.')[0] + "_iv_" + presetName + ".mkv" + '"'
    return iv

def generateOutputVideoName(corePath, inputVideoName, presetName):
    ov = '"' + corePath + "\\Output\\" + inputVideoName.split('.')[0] + "_ov_" + presetName + ".mkv" + '"'
    return ov

def generateAudioName(corePath, inputVideoName):
    audio = '"' + corePath + "\\Audio\\" + inputVideoName.split('.')[0] + "_audio.mka" + '"'
    return audio

def generateBatName(corePath, inputVideoName, presetName):
    bat = corePath + "\\BAT\\" + inputVideoName.split('.')[0] + "_" + presetName +  "_bat.bat"
    return bat

def generateStatsName(corePath, inputVideoName, presetName):
    stat = '"' + corePath + "\\Stats\\" + inputVideoName.split('.')[0] + "_" + presetName + "_stats.txt" + '"'
    return stat

def compressdis(corePath, inputVideo, presetName):
    ffmpeg = '"' + str(PureWindowsPath(Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/ffmpeg/ffmpeg.exe"))) + '"'
    mkvmerge = '"' + str(PureWindowsPath(Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/MKVToolNix/mkvmerge.exe"))) + '"'
    avs = generateAVSName(corePath, inputVideo)
    intermediateVideo = generateIntermediateVideoName(corePath, inputVideo, presetName)
    outputVideo = generateOutputVideoName(corePath, inputVideo, presetName)
    audio = generateAudioName(corePath, inputVideo)
    bat = generateBatName(corePath, inputVideo, presetName)
    compressionDurationStats = generateStatsName(corePath, inputVideo, presetName)
    createAVS(corePath, inputVideo, avs)
    audioSeperator = ffmpeg + ' -i "' + corePath + '\\Input\\' + inputVideo + '" -vn -acodec copy ' + audio
    compressor = ffmpeg + ' -i "' + avs + '" -c:v libx265 -preset ' + presetName + ' -tune psnr -an -y -hide_banner ' + intermediateVideo + ' 2>' + compressionDurationStats
    merger = mkvmerge + ' -o ' + outputVideo + ' ' + intermediateVideo + ' --audio-tracks 0 --language 0:eng --default-track 0:0 --forced-track 0:0 ' + audio + ' --ui-language en'
    file = open(bat,'w')
    file.write(audioSeperator)
    file.write("\n")
    file.write(compressor)
    file.write("\n")
    file.write(merger)
    file.write("\n")
    file.close()
    os.system('"' + bat + '"')

compressdis('E:\\New folder', 'WhatsApp Video.mp4', 'medium')
compressdis('E:\\New folder', 'WhatsApp Video.mp4', 'faster')
compressdis('E:\\New folder', 'WhatsApp Video.mp4', 'superfast')