# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:04:12 2019

@author: PRIYANSHZALAVADIYA
"""


import os

def vqmt(video1,video2,width,height,frames):
    #os.system('ffmpeg -i video1 -c:v rawvideo -pix_fmt yuv420p video.yuv')
    #os.system('ffmpeg -i video2 -c:v rawvideo -pix_fmt yuv420p compress_video.yuv')
    #os.system('VQMT.exe video.yuv compress_video.yuv width height frames 1 results PSNR SSIM VIFP')
    
    import pandas
    df = pandas.read_csv('results_psnr.csv', index_col='frame')
    avgpsnr=df[['value']].mean()
    avgpsnr=avgpsnr.value
    
    df = pandas.read_csv('results_ssim.csv', index_col='frame')
    avgssim=df[['value']].mean()
    avgssim=avgssim.value
    
    df = pandas.read_csv('results_vifp.csv', index_col='frame')
    avgvifp=df[['value']].mean()
    avgvifp=avgvifp.value
