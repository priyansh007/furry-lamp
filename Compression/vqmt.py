import os
import pandas
import subprocess
from pathlib import Path, PureWindowsPath

def generateOutputVideoName(corePath, inputVideoName, presetName):
    ov = '"' + corePath + "\\Output\\" + inputVideoName.split('.')[0] + "\\" + inputVideoName.split('.')[0] + "_outputVideo_" + presetName + ".mkv" + '"'
    return ov

def videoQualityMeasure(corePath, inputVideoName, presets, width, height, frames, ffmpeg, vqmt):
    qualityDir = corePath + "\\Quality\\" + inputVideoName.split('.')[0] + "\\"
    os.makedirs(qualityDir.replace("\\", "/"), exist_ok=True)
    inputVideo = '"' + corePath + '\\Input\\' + inputVideoName + '"'
    originalYUVName = '"' + corePath + '\\Quality\\' + inputVideoName.split('.')[0] + "\\" + inputVideoName.split(".")[0] + '.yuv"'
    print(ffmpeg + ' -i ' + inputVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + originalYUVName)
    subprocess.call(ffmpeg + ' -i ' + inputVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + originalYUVName, shell=True)
    for presetName in presets:
        compressedVideo = generateOutputVideoName(corePath, inputVideoName, presetName)
        compressedVideoName = inputVideoName.split(".")[0] + "_outputVideo_" + presetName
        compressedYUVName = '"' + corePath + '\\Quality\\' + inputVideoName.split('.')[0] + "\\" + compressedVideoName + '.yuv"'
        qualityResultName = '"' + corePath + '\\Quality\\' + inputVideoName.split('.')[0] + "\\" + compressedVideoName + '_qualityResult"'
        print(ffmpeg + ' -i ' + compressedVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + compressedYUVName)
        subprocess.call(ffmpeg + ' -i ' + compressedVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + compressedYUVName, shell=True)
        print(vqmt + ' ' + originalYUVName + ' ' + compressedYUVName + ' ' + str(width) + ' ' + height + ' ' + str(frames) + ' 1 ' + qualityResultName + ' PSNR SSIM VIFP')
        subprocess.call(vqmt + ' ' + originalYUVName + ' ' + compressedYUVName + ' ' + width + ' ' + height + ' ' + str(frames) + ' 1 ' + qualityResultName + ' PSNR SSIM VIFP', shell=True)
        
        df = pandas.read_csv(qualityResultName.replace('"','') + '_psnr.csv', index_col='frame')
        avgpsnr=df[['value']].mean()
        avgpsnr=avgpsnr.value
        print(avgpsnr)
        
        df = pandas.read_csv(qualityResultName.replace('"','') + '_ssim.csv', index_col='frame')
        avgssim=df[['value']].mean()
        avgssim=avgssim.value
        print(avgssim)
        
        df = pandas.read_csv(qualityResultName.replace('"','') + '_vifp.csv', index_col='frame')
        avgvifp=df[['value']].mean()
        avgvifp=avgvifp.value
        print(avgvifp)

#ffmpeg = '"' + str(PureWindowsPath(Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/ffmpeg/ffmpeg.exe"))) + '"'
#vqmt = '"' + str(PureWindowsPath(Path("E:/VQMT/VQMT.exe"))) + '"'
#videoQualityMeasure(str(PureWindowsPath(Path("E:/New folder"))), 'WhatsApp Video.mp4', ['superfast', 'veryfast'], 1280, 720, 1853, ffmpeg, vqmt)