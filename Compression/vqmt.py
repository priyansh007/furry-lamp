import os
import pandas
import subprocess

def name_and_ext(video_name):
    split_list = video_name.split('.')
    name = '.'.join(split_list[0:len(split_list)-1])
    extension = split_list[len(split_list)-1]
    return [name,extension]

def modulo8(value):
    if(value % 8 == 0):
        return value
    else:
        return (value - (value % 8))

def generateOutputVideoName(corePath, inputVideoName, presetName):
    ov = '"' + corePath + "\\Output\\" + name_and_ext(inputVideoName)[0] + "\\" + name_and_ext(inputVideoName)[0] + "_outputVideo_" + presetName + ".mkv" + '"'
    return ov

def videoQualityMeasure(corePath, inputVideoName, presets, width, height, frames, ffmpeg, vqmt, logFile):
    width = str(modulo8(int(width)))
    height = str(modulo8(int(height)))
    print('Video Quality Measurement started for ' + inputVideoName)
    log = open(logFile, 'a')
    log.write('\nVideo Quality Measurement started for ' + inputVideoName)
    log.close()
    qualityDir = corePath + "\\Quality\\" + name_and_ext(inputVideoName)[0] + "\\"
    os.makedirs(qualityDir.replace("\\", "/"), exist_ok=True)
    presetWiseQualityDetails = []
    inputVideo = '"' + corePath + '\\Input\\' + inputVideoName + '"'
    originalYUVName = '"' + corePath + '\\Quality\\' + name_and_ext(inputVideoName)[0] + "\\" + name_and_ext(inputVideoName)[0] + '.yuv"'
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
        compressedVideoName = name_and_ext(inputVideoName)[0] + "_outputVideo_" + presetName
        compressedYUVName = '"' + corePath + '\\Quality\\' + name_and_ext(inputVideoName)[0] + "\\" + compressedVideoName + '.yuv"'
        qualityResultName = '"' + corePath + '\\Quality\\' + name_and_ext(inputVideoName)[0] + "\\" + compressedVideoName + '_qualityResult"'
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
        processTime = subprocess.check_output(vqmt + ' ' + originalYUVName + ' ' + compressedYUVName + ' ' + width + ' ' + height + ' ' + str(frames) + ' 1 ' + qualityResultName + ' PSNR SSIM VIFP', shell=True).decode('utf-8').rstrip()
        print(processTime)
        log = open(logFile, 'a')
        log.write('\n' + processTime)
        log.close()
        df = pandas.read_csv(qualityResultName.replace('"','') + '_psnr.csv', index_col='frame')
        avgpsnr=0

        for index, row in df.iterrows():
            try:
                q=float(row['value'])
                q=round(q,2)
                avgpsnr=(avgpsnr+q)/2
                #print(q)
            except:
                continue
        avgpsnr=round(avgpsnr,2)
        print('\tAVG PSNR value : ' + str(avgpsnr))
        log = open(logFile, 'a')
        log.write('\n\tAVG PSNR value : ' + str(avgpsnr))
        log.close()

        df = pandas.read_csv(qualityResultName.replace('"','') + '_ssim.csv', index_col='frame')
        avgssim=0

        for index, row in df.iterrows():
            try:
                q=float(row['value'])
                q=round(q,4)
                avgssim=(avgssim+q)/2
                #print(q)
            except:
                continue		
        print('\tAVG SSIM value : ' + str(avgssim))
        log = open(logFile, 'a')
        log.write('\n\tAVG SSIM value : ' + str(avgssim))
        log.close()

        df = pandas.read_csv(qualityResultName.replace('"','') + '_vifp.csv', index_col='frame')
        avgvifp=0

        for index, row in df.iterrows():
            try:
                q=float(row['value'])
                q=round(q,4)
                avgvifp=(avgvifp+q)/2
                #print(q)
            except:
                continue		
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
