def createAVS(avs):
    file = open('<avs>','w')
    file.write('LoadPlugin("E:\N.I.B.B.A.S\StaxRip 1.9.0.0\Apps\Plugins\avs\L-SMASH-Works\LSMASHSource.dll")')
    file.write('LSMASHVideoSource("E:\New folder\WhatsApp Video.mp4", format = "YUV420P8"')
    file.close()

def compressdis(inputVideo, presetName):
    ffmpeg = Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/ffmpeg/ffmpeg.exe")
    mkvmerge = Path("E:/N.I.B.B.A.S/StaxRip 1.9.0.0/Apps/MKVToolNix/mkvmerge.exe")
    avs = generateAVSName(inputVideo)
    intermediateVideo = generateIntermediateVideoName(inputVideo)
    outputVideo = generateOutputVideoName(inputVideo)
    audio = generateAudioName(inputVideo)
    bat = generateBatName(inputvideo)
    compressionDurationStats = generateStatsName(inputvideo)
    createAVS(avs)
    audioSeperator = ffmpeg + ' -i ' + inputVideo + ' -vn -acodec copy ' + audio
    compressor = ffmpeg + ' -i ' + avs + ' -c:v libx265 -preset ' + presetName + ' -tune psnr -an -y -hide_banner ' + intermediateVideo + ' 2>' + compressionDurationStats
    merger = mkvmerge + ' -o ' + intermediateVideo + outputVideo + ' --audio-tracks 0 --language 0:eng --default-track 0:0 --forced-track 0:0 ' + audio + ' --ui-language en'
    file = open('<bat>','w')
    file.write(audioSeperator)
    file.write(compressor)
    file.write(merger)
    file.close()
    os.system('start cmd /K <bat>')