import pandas
import subprocess
from pathlib import Path, PureWindowsPath

def videoQualityMeasure(corePath, inputVideoName, compressedVideoName, width, height, frames, ffmpeg, vqmt):
    inputVideo = '"' + corePath + '\\Input\\' + inputVideoName + '"'
    compressedVideo = '"' + corePath + '\\Output\\' + inputVideoName.split(".")[0] + '\\' + compressedVideoName + '"'
    originalYUVName = '"' + corePath + '\\Quality\\' + inputVideoName.split(".")[0] + '.yuv"'
    compressedYUVName = '"' + corePath + '\\Quality\\' + compressedVideoName.split(".")[0] + '.yuv"'
    qualityResultName = '"' + corePath + '\\Quality\\' + inputVideoName.split(".")[0] + '_qualityResult"'
    print(vqmt + ' ' + originalYUVName + ' ' + compressedYUVName + ' ' + str(width) + ' ' + str(height) + ' ' + str(frames) + ' 1 ' + qualityResultName + ' PSNR SSIM VIFP')
    subprocess.call(ffmpeg + ' -i ' + inputVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + originalYUVName, shell=True)
    subprocess.call(ffmpeg + ' -i ' + compressedVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + compressedYUVName, shell=True)
    subprocess.call(vqmt + ' ' + originalYUVName + ' ' + compressedYUVName + ' ' + str(width) + ' ' + str(height) + ' ' + str(frames) + ' 1 ' + qualityResultName + ' PSNR SSIM VIFP', shell=True)
    
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

ffmpeg = '"' + str(PureWindowsPath(Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/ffmpeg/ffmpeg.exe"))) + '"'
vqmt = '"' + str(PureWindowsPath(Path("E:/VQMT/VQMT.exe"))) + '"'
videoQualityMeasure(str(PureWindowsPath(Path("E:/New folder"))), 'WhatsApp Video.mp4', 'WhatsApp Video_outputVideo_superfast.mkv', 1280, 720, 1853, ffmpeg, vqmt)