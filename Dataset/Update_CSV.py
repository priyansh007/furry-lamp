import csv

def push_data_to_csv(presets, features, details, bitrate_and_size, duration_and_frames):
    for preset in presets:
        with open('video_data.csv', mode='a') as csv_file:
            fieldnames = ['Video Name','Width', 'Height', 'Video Length', 'Frames per Second','Frame Count', 'Original Bitrate', 'Original Size', 'Scene Count', 'Avg Motion %', 'Avg PCC', 'Compression Preset','Compression Duration', 'Compressed Bitrate', 'Compressed Size']

            # fileObject = csv.reader(csv_file)
            # data = list(fileObject)
            # row_count = len(data)

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

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(
                {
                    #'Sr.No.': 1,
                    'Video Name': features[0],
                    'Width' : details[2],
                    'Height' : details[3],
                    'Video Length' : details[0],
                    'Frames per Second': details[4],
                    'Frame Count' : frames,
                    'Original Bitrate' : details[1],
                    'Original Size' : details[5],
                    'Scene Count' : features[1],
                    'Avg Motion %' : features[2],
                    'Avg PCC' : features[3],
                    'Compression Preset' : preset,
                    'Compression Duration' : duration,
                    'Compressed Bitrate' : bitrate,
                    'Compressed Size' : size
                })

# For Test Run
# presets = ['superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower']
# features = ["./Videos/asdsf.mp4",2,"35.16%","80%"]
# details = [11,22,33,44,55,66]
# bitrate_and_size = [ ['superfast',1,2], ['veryfast',3,4], ['faster',5,7], ['fast',8,7], ['medium',5,7], ['slow',3,4], ['slower',9,10] ]
# duration_and_frames = [ ['superfast',2,2], ['veryfast',4,4], ['faster',9,9], ['fast',6,6], ['medium',5,5], ['slow',4,4], ['slower',9,9] ]
#
# push_data_to_csv(presets, features, details, bitrate_and_size, duration_and_frames)
