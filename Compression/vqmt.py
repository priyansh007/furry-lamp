import os
import pandas
import subprocess

def modulo8(value):
    if(value % 8 == 0):
        return value
    else:
        return (value - (value % 8))

def generateOutputVideoName(corePath, inputVideoName, presetName):
    ov = '"' + corePath + "\\Output\\" + inputVideoName.split('.')[0] + "\\" + inputVideoName.split('.')[0] + "_outputVideo_" + presetName + ".mkv" + '"'
    return ov

def videoQualityMeasure(corePath, inputVideoName, presets, width, height, frames, ffmpeg, vqmt, logFile):
    width = modulo8(int(width))
    height = modulo8(int(height))
    print('Video Quality Measurement started for ' + inputVideoName)
    log = open(logFile, 'a')
    log.write('Video Quality Measurement started for ' + inputVideoName)
    log.close()
    qualityDir = corePath + "\\Quality\\" + inputVideoName.split('.')[0] + "\\"
    os.makedirs(qualityDir.replace("\\", "/"), exist_ok=True)
    presetWiseQualityDetails = []
    inputVideo = '"' + corePath + '\\Input\\' + inputVideoName + '"'
    originalYUVName = '"' + corePath + '\\Quality\\' + inputVideoName.split('.')[0] + "\\" + inputVideoName.split(".")[0] + '.yuv"'
    if os.path.isfile(originalYUVName.replace('"','')):
        print("Deleting previous original YUV")
        log = open(logFile, 'a')
        log.write("\nDeleting previous original YUV")
        log.close()
        os.remove(originalYUVName.replace('"',''))
    print('Generating original YUV')
    log = open(logFile, 'a')
    log.write('\nGenerating original YUV')
    log.close()
    print(subprocess.check_output(ffmpeg + ' -i ' + inputVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + originalYUVName, shell=True).decode('utf-8').rstrip())
    for presetName in presets:
        compressedVideo = generateOutputVideoName(corePath, inputVideoName, presetName)
        compressedVideoName = inputVideoName.split(".")[0] + "_outputVideo_" + presetName
        compressedYUVName = '"' + corePath + '\\Quality\\' + inputVideoName.split('.')[0] + "\\" + compressedVideoName + '.yuv"'
        qualityResultName = '"' + corePath + '\\Quality\\' + inputVideoName.split('.')[0] + "\\" + compressedVideoName + '_qualityResult"'
        if os.path.isfile(compressedYUVName.replace('"','')):
            print("Deleting previous compressed YUV")
            log = open(logFile, 'a')
            log.write("\nDeleting previous compressed YUV")
            log.close()
            os.remove(compressedYUVName.replace('"',''))
        print('Generating compressed YUV for ' + presetName)
        log = open(logFile, 'a')
        log.write('\nGenerating compressed YUV for ' + presetName)
        log.close()
        print(subprocess.check_output(ffmpeg + ' -i ' + compressedVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + compressedYUVName, shell=True).decode('utf-8').rstrip())
        print('Comparing both YUVs')
        log = open(logFile, 'a')
        log.write('\nComparing both YUVs')
        log.close()
        print(subprocess.check_output(vqmt + ' ' + originalYUVName + ' ' + compressedYUVName + ' ' + width + ' ' + height + ' ' + str(frames) + ' 1 ' + qualityResultName + ' PSNR SSIM VIFP', shell=True).decode('utf-8').rstrip())
        
        df = pandas.read_csv(qualityResultName.replace('"','') + '_psnr.csv', index_col='frame')
        avgpsnr=df[['value']].mean()
        avgpsnr=avgpsnr.value
        print('\tAVG PSNR value : ' + str(avgpsnr))
        log = open(logFile, 'a')
        log.write('\n\tAVG PSNR value : ' + str(avgpsnr))
        log.close()
        
        df = pandas.read_csv(qualityResultName.replace('"','') + '_ssim.csv', index_col='frame')
        avgssim=df[['value']].mean()
        avgssim=avgssim.value
        print('\tAVG SSIM value : ' + str(avgssim))
        log = open(logFile, 'a')
        log.write('\n\tAVG SSIM value : ' + str(avgssim))
        log.close()

        df = pandas.read_csv(qualityResultName.replace('"','') + '_vifp.csv', index_col='frame')
        avgvifp=df[['value']].mean()
        avgvifp=avgvifp.value
        print('\tAVG VIFp value : ' + str(avgvifp))
        log = open(logFile, 'a')
        log.write('\n\tAVG VIFp value : ' + str(avgvifp))
        log.close()
        presetWiseQualityDetails.append([presetName, str(avgpsnr), str(avgssim), str(avgvifp)])
        if os.path.isfile(compressedYUVName.replace('"','')):
            print("Deleting compressed YUV")
            log = open(logFile, 'a')
            log.write("\nDeleting compressed YUV")
            log.close()
            os.remove(compressedYUVName.replace('"',''))
    if os.path.isfile(originalYUVName.replace('"','')):
        print("Deleting original YUV")
        log = open(logFile, 'a')
        log.write("\nDeleting original YUV")
        log.close()
        os.remove(originalYUVName.replace('"',''))
    print('Video Quality Measurement ended')
    log = open(logFile, 'a')
    log.write('\nVideo Quality Measurement ended')
    log.close()
    return presetWiseQualityDetails
