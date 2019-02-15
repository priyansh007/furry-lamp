# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from pathlib import Path, PureWindowsPath

#os.system('"E:\\N.I.B.B.A.S\\StaxRip 1.9.0.0\\Apps\\ffmpeg\\ffmpeg.exe" -i "E:\\New folder\\WhatsApp Video_temp\\WhatsApp Video.avs" -c:v libx265 -preset faster –tune psnr -an -y -hide_banner "E:\\New folder\\Intermediate\\WhatsApp Video_out_faster.mkv"')
ffmpeg = Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/ffmpeg/ffmpeg.exe")
avs = Path("E:/New folder/WhatsApp Video_temp/WhatsApp Video.avs")
outvid = Path("E:/New folder/Intermediate/WhatsApp Video_out_faster.mkv")
ffm = '"' + str(PureWindowsPath(ffmpeg)) + '"'
av = '"' + str(PureWindowsPath(avs)) + '"'
ov = '"' + str(PureWindowsPath(outvid)) + '"'
strin = ffm + ' -i ' + av + ' -c:v libx265 -preset faster -tune psnr -an -y -hide_banner ' + ov
#print(ffm + ' -i ' + av + ' -c:v libx265 -preset faster –tune psnr -an -y -hide_banner ' + ov)
#os.system('start powershell /K ' + ffm + ' -i ' + av + ' -c:v libx265 -preset faster –tune psnr -an -y -hide_banner ' + ov)
print(strin)
file = open('testfile.bat','w') 
 
file.write(strin)
 
file.close()

os.system('start cmd /K testfile.bat')
