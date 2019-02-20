# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:04:12 2019

@author: PRIYANSHZALAVADIYA
"""


import os
os.system('ffmpeg -i Dog.mp4 -c:v rawvideo -pix_fmt yuv420p out.yuv')
os.system('VQMT.exe out.yuv out.yuv 360 640 540 1 results PSNR SSIM VIFP')
    
