# IMPORTING ESSENTIAL LIBRARIES
library(dplyr)

# RATIO1 = (PSNR + SSIM + VIFp) BY DURATION
video_dataset$Ratio1 <- round((video_dataset$Normalized.PSNR + video_dataset$Normalized.SSIM + video_dataset$Normalized.VIFp)/video_dataset$Normalized.Duration, digits = 7)
ratio1_max <- setNames(aggregate(video_dataset$Ratio1, by = list(video_dataset$Video.Name), max), c("Video.Name", "Ratio1"))
ratio1_preset <- merge(ratio1_max, video_dataset, 
                       c("Video.Name","Ratio1"))[,c("Video.Name", "Compression.Preset", 
                                                    "Ratio1","Avg.Motion","Avg.PCC",
                                                    "Original.Bitrate","Original.Size")]
# RATIO3 = (PSNR + SSIM + VIFp) / 3
video_dataset$Ratio3 <- round((video_dataset$Normalized.PSNR + video_dataset$Normalized.SSIM + video_dataset$Normalized.VIFp)/3, digits = 7)
ratio3_max <- setNames(aggregate(video_dataset$Ratio3, by = list(video_dataset$Video.Name), max), c("Video.Name", "Ratio3"))
ratio3_preset <- merge(ratio3_max, video_dataset, c("Video.Name","Ratio3"))[,c("Video.Name", "Compression.Preset", "Ratio3")]
#[,c("Video.Name", "Compression.Preset", "Ratio2","Avg.Motion","Avg.PCC", "Original.Bitrate","Original.Size")]

# DELETING COLUMNS FROM DATASET
drops <- c("Ratio1","Ratio2")
video_dataset <- video_dataset[ , !(names(video_dataset) %in% drops)]

# COUNT OF VIDEOS UNDER EACH BEST PRESET
dataset_with_output_preset %>% 
  group_by(Compression.Preset) %>% 
  summarise(n = n())

# OLD FORMULAS
max_psnr <- setNames(aggregate(video_dataset$Average.PSNR, by = list(video_dataset$Video.Name), max), c("Video.Name", "Normalized.PSNR"))
max_ssim <- setNames(aggregate(video_dataset$Average.SSIM, by = list(video_dataset$Video.Name), max), c("Video.Name", "Normalized.SSIM"))
max_vifp <- setNames(aggregate(video_dataset$Average.VIFp, by = list(video_dataset$Video.Name), max), c("Video.Name", "Normalized.VIFp"))
min_duration <- setNames(aggregate(video_dataset$Compression.Duration, by = list(video_dataset$Video.Name), min), c("Video.Name", "Normalized.Duration"))
min_size <- setNames(aggregate(video_dataset$Compressed.Size, by = list(video_dataset$Video.Name), min), c("Video.Name", "Normalized.Size"))
