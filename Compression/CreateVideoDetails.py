import os
os.chdir("C:\Program Files\mediainfo")
os.getcwd()
log = os.system('"MediaInfo.exe" first.MOV >D:\log.txt')
