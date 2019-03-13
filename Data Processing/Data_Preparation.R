# IMPORT DATASET FROM CSV
video_dataset <- read.csv(file="D:\\Academics\\Sem-7(2018-19)\\Project\\Code\\Data Preparation\\data_final.csv", header=TRUE, sep = ',')

# IMPORTING ESSENTIAL LIBRARIES
library(ggplot2)
library(dplyr)

# SUMMARY OF DATASET
summary(video_dataset)

# FACTOR COMPRESSION PRESETS IN THE CORRECT ORDER
video_dataset$Compression.Preset <-factor(video_dataset$Compression.Preset, levels=unique(video_dataset$Compression.Preset))

# NORMALIZING PSNR
minmax_psnr <- video_dataset %>% group_by(Video.Name) %>%
  summarize(min_psnr = min(Average.PSNR), max_psnr = max(Average.PSNR))
temp_dataset <- merge(video_dataset[,c("Video.Name","Compression.Preset","Average.PSNR")], minmax_psnr, by="Video.Name")
video_dataset$Normalized.PSNR <- (video_dataset$Average.PSNR - temp_dataset$min_psnr)/(temp_dataset$max_psnr - temp_dataset$min_psnr) + 1

# NORMALIZING SSIM
minmax_ssim <- video_dataset %>% group_by(Video.Name) %>%
  summarize(min_ssim = min(Average.SSIM), max_ssim = max(Average.SSIM))
temp_dataset <- merge(video_dataset[,c("Video.Name","Compression.Preset","Average.SSIM")], minmax_ssim, by="Video.Name")
video_dataset$Normalized.SSIM <- (video_dataset$Average.SSIM - temp_dataset$min_ssim)/(temp_dataset$max_ssim - temp_dataset$min_ssim) + 1

# NORMALIZING VIFp
minmax_vifp <- video_dataset %>% group_by(Video.Name) %>%
  summarize(min_vifp = min(Average.VIFp), max_vifp = max(Average.VIFp))
temp_dataset <- merge(video_dataset[,c("Video.Name","Compression.Preset","Average.VIFp")], minmax_vifp, by="Video.Name")
video_dataset$Normalized.VIFp <- (video_dataset$Average.VIFp - temp_dataset$min_vifp)/(temp_dataset$max_vifp - temp_dataset$min_vifp) + 1

# NORMALIZING DURATTION
minmax_duration <- video_dataset %>% group_by(Video.Name) %>%
  summarize(min_duration = min(Compression.Duration), max_duration = max(Compression.Duration))
temp_dataset <- merge(video_dataset[,c("Video.Name","Compression.Preset","Compression.Duration")], minmax_duration, by="Video.Name")
video_dataset$Normalized.Duration <- (video_dataset$Compression.Duration - temp_dataset$min_duration)/(temp_dataset$max_duration - temp_dataset$min_duration) + 1

# NORMALIZING SIZE
minmax_size <- video_dataset %>% group_by(Video.Name) %>%
  summarize(min_size = min(Compressed.Size), max_size = max(Compressed.Size))
temp_dataset <- merge(video_dataset[,c("Video.Name","Compression.Preset","Compressed.Size")], minmax_size, by="Video.Name")
video_dataset$Normalized.Size <- (video_dataset$Compressed.Size - temp_dataset$min_size)/(temp_dataset$max_size - temp_dataset$min_size) + 1

# PSNR BY NORMALIZED DURATION
video_dataset$PSNR.By.Duration <- video_dataset$Normalized.PSNR/video_dataset$Normalized.Duration

# SSIM BY NORMALIZED DURATION
video_dataset$SSIM.By.Duration <- video_dataset$Normalized.SSIM/video_dataset$Normalized.Duration

# VIFp BY NORMALIZED DURATION
video_dataset$VIFp.By.Duration <- video_dataset$Normalized.VIFp/video_dataset$Normalized.Duration

# METRIC = (PSNR + SSIM + VIFp)/ (DURATION * COMPRESSED SIZEvideo_dataset$Ratio1 <- round((video_dataset$Normalized.PSNR + video_dataset$Normalized.SSIM + video_dataset$Normalized.VIFp)/video_dataset$Normalized.Duration, digits = 7)
video_dataset$Metric <- round( (video_dataset$Normalized.PSNR + video_dataset$Normalized.SSIM + video_dataset$Normalized.VIFp) / (video_dataset$Normalized.Duration * video_dataset$Normalized.Size), digits = 7)
metric_max <- setNames(aggregate(video_dataset$Metric, by = list(video_dataset$Video.Name), max), c("Video.Name", "Metric"))
dataset_with_output_preset <- merge(video_dataset, metric_max,c("Video.Name","Metric"))

# EXPORT OUTPUT TO CSV
write.csv(dataset_with_output_preset, file = "D:\\Academics\\Sem-7(2018-19)\\Project\\Code\\Data Preparation\\data_final_with_output_presets.csv")

# EXPORT NORMALIZED FULL DATA TO CSV
write.csv(video_dataset, file = "D:\\Academics\\Sem-7(2018-19)\\Project\\Code\\Data Preparation\\data_final_normalized_full.csv")


