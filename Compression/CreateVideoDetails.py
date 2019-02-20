def CreateVideoDetail(VideoPath):
    import os
    from pathlib import Path, PureWindowsPath
    VideoPath = str(PureWindowsPath(Path("C:/Forest_Slice.mov")))
    os.chdir("C:\Program Files\mediainfo")
    os.getcwd()
    os.system('"MediaInfo.exe" '+VideoPath+' >D:\log.txt')
