import os
import subprocess

def name_and_ext(video_name):
    split_list = video_name.split('.')
    name = '.'.join(split_list[0:len(split_list)-1])
    extension = split_list[len(split_list)-1]
    return [name,extension]

def createAVS(corePath, inputVideoName, avs):
    ffmsindex = '"D:\\Video Compression\\Staxrip.2.0.0.0.x64\\Apps\\Plugins\\Both\\FFMS2\\ffmsindex.exe"'
    inputVideoPath = '"' + corePath + '\\Input\\' + inputVideoName + '"'
    ffindexPath = '"' + corePath + "\\Intermediate\\" + name_and_ext(inputVideoName)[0] + "\\" + name_and_ext(inputVideoName)[0] + "_index.ffindex" + '"'
    print(subprocess.check_output(ffmsindex + ' -f ' + inputVideoPath + ' ' + ffindexPath,shell=True).decode('utf-8').rstrip())
    file = open(avs,'w')
    file.write('LoadCPlugin("D:\\Video Compression\\Staxrip.2.0.0.0.x64\\Apps\\Plugins\\Both\\FFMS2\\ffms2.dll")\n')
    file.write('FFVideoSource(' + inputVideoPath + ', colorspace = "YV12", cachefile = ' + ffindexPath + ')')
    file.close()

def generateAVSName(corePath, inputVideoName):
    avs = corePath + "\\AVS\\" + name_and_ext(inputVideoName)[0] + "_avs.avs"
    return avs

def generateOutputVideoName(corePath, inputVideoName, presetName):
    ov = '"' + corePath + "\\Output\\" + name_and_ext(inputVideoName)[0] + "\\" + name_and_ext(inputVideoName)[0] + "_outputVideo_" + presetName + ".mkv" + '"'
    return ov

def generateBatName(corePath, inputVideoName):
    bat = corePath + "\\BAT\\" + name_and_ext(inputVideoName)[0] +  "_batchFile.bat"
    return bat

def generateStatsName(corePath, inputVideoName, presetName):
    stat = '"' + corePath + "\\Stats\\" + name_and_ext(inputVideoName)[0] + "\\" + name_and_ext(inputVideoName)[0] + "_" + presetName + "_stats.txt" + '"'
    return stat

def compressdis(corePath, inputVideo, presets, ffmpeg, mkvmerge, logFile):
    print('Starting Compression Process on ' + inputVideo)
    log = open(logFile, 'a')
    log.write('\nStarting Compression Process on ' + inputVideo)
    log.close
    avs = generateAVSName(corePath, inputVideo)
    bat = generateBatName(corePath, inputVideo)
    outputDir = corePath + "\\Output\\" + name_and_ext(inputVideo)[0] + "\\"
    intermediateDir = corePath + "\\Intermediate\\" + name_and_ext(inputVideo)[0] + "\\"
    statsDir = corePath + "\\Stats\\" + name_and_ext(inputVideo)[0] + "\\"
    os.makedirs(outputDir.replace("\\", "/"), exist_ok=True)
    os.makedirs(intermediateDir.replace("\\", "/"), exist_ok=True)
    os.makedirs(statsDir.replace("\\", "/"), exist_ok=True)
    createAVS(corePath, inputVideo, avs)
    file = open(bat,'w')
    for presetName in presets:
        outputVideo = generateOutputVideoName(corePath, inputVideo, presetName)
        compressionDurationStats = generateStatsName(corePath, inputVideo, presetName)
        compressor = ffmpeg + ' -i "' + avs + '" -c:v libx265 -preset ' + presetName + ' -tune psnr -an -y -hide_banner ' + outputVideo + ' 2>' + compressionDurationStats
        file.write(compressor)
        file.write("\n")
    file.close()
    os.system('"' + bat + '"')
    print('Compression complete')
    log = open(logFile, 'a')
    log.write('\nCompression complete')
    log.close()
