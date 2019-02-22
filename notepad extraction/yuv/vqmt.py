import os
import pandas

def vqmt(corePath, inputVideoName, compressedVideoName, width, height, frames, ffmpeg, vqmt):
    inputVideo = '"' + corePath + '\\Input\\' + inputVideoName + '"'
    compressedVideo = '"' + corePath + '\\Input\\' + compressedVideoName + '"'
    originalYUVName = '"' + corePath + '\\Quality\\' + inputVideoName.split(".")[0] + '.yuv"'
    compressedYUVName = '"' + corePath + '\\Quality\\' + compressedVideoName.split(".")[0] + '.yuv"'
    qualityResultName = '"' + corePath + '\\Quality\\' + inputVideoName.split(".")[0] + '_qualityResult"'
    os.system(ffmpeg + ' -i ' + inputVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + originalYUVName)
    os.system(ffmpeg + ' -i ' + compressedVideo + ' -c:v rawvideo -pix_fmt yuv420p ' + compressedYUVName)
    os.system(vqmt + originalYUVName + ' ' + compressedYUVName + ' ' + width + ' ' height + ' ' frames + ' 1 ' + qualityResultName + ' PSNR SSIM VIFP')
    
    df = pandas.read_csv('results_psnr.csv', index_col='frame')
    avgpsnr=df[['value']].mean()
    avgpsnr=avgpsnr.value
    
    df = pandas.read_csv('results_ssim.csv', index_col='frame')
    avgssim=df[['value']].mean()
    avgssim=avgssim.value
    
    df = pandas.read_csv('results_vifp.csv', index_col='frame')
    avgvifp=df[['value']].mean()
    avgvifp=avgvifp.value
