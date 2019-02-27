def writeCSV(csvPath, presets, features, details, bitrate_and_size, duration_and_frames, presetWiseQualityDetails):
    print('Pushing')
    file = open(csvPath,'a')
    for preset in presets:
        for i in bitrate_and_size:
            if i[0] == preset:
                bitrate = i[1]
                size = i[2]
                break

        for j in duration_and_frames:
            if j[0] == preset:
                duration = j[1]
                frames = j[2]
                break
        
        for k in presetWiseQualityDetails:
            if k[0] == preset:
                avgPSNR = k[1]
                avgSSIM = k[2]
                avgVIFP = k[3]
                break

        file.write('\n' + features[0] + ',' + details[2] + ',' + details[3] + ',' + details[0] + ',' + details[4] + ',' + frames + ',' + details[1] + ',' + details[5] + ',' + features[1] + ',' + features[2] + ',' + features[3] + ',' + preset + ',' + duration + ',' + bitrate + ',' + size + ',' + avgPSNR + ',' + avgSSIM + ',' + avgVIFP)
    print('done')