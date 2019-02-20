# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:04:12 2019

@author: PRIYANSHZALAVADIYA
"""


import os
#os.system('ffmpeg -i Dog.mp4 -c:v rawvideo -pix_fmt yuv420p out.yuv')
#os.system('VQMT.exe out.yuv out.yuv 360 640 540 1 results PSNR SSIM VIFP')

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
