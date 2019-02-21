def output_video(video_name_only):
    name_and_extension = video_name_only.split('.')
    # print(name_and_extension)
    output_folder =  "E:/Project/Output_videos/"
    container = "faster"
    final_destination = output_folder+name_and_extension[0]+"_"+container+"."+name_and_extension[1]
    print("Output Video - " + final_destination)
