video_dataset <- read.csv(file="D:\\Academics\\Sem-7(2018-19)\\Project\\Code\\data_final.csv", header=TRUE, sep = ',')
#library(ggplot2)
#library(dplyr)

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



# RATIO1 = (PSNR + SSIM + VIFp) BY DURATION
video_dataset$Ratio1 <- round((video_dataset$Normalized.PSNR + video_dataset$Normalized.SSIM + video_dataset$Normalized.VIFp)/video_dataset$Normalized.Duration, digits = 7)
ratio1_max <- setNames(aggregate(video_dataset$Ratio1, by = list(video_dataset$Video.Name), max), c("Video.Name", "Ratio1"))
ratio1_preset <- merge(ratio1_max, video_dataset, c("Video.Name","Ratio1"))[,c("Video.Name", "Compression.Preset", "Ratio1")]

# RATIO2 = RATIO1 / COMPRESSED SIZE(in MBs)
video_dataset$Ratio2 <- round( video_dataset$Ratio1*1024*1024/video_dataset$Normalized.Size, digits = 7)
ratio2_max <- setNames(aggregate(video_dataset$Ratio2, by = list(video_dataset$Video.Name), max), c("Video.Name", "Ratio2"))
ratio2_preset <- merge(ratio2_max, video_dataset, c("Video.Name","Ratio2"))[,c("Video.Name", "Compression.Preset", "Ratio2")]

# RATIO3 = (PSNR + SSIM + VIFp) / 3
video_dataset$Ratio3 <- round((video_dataset$Normalized.PSNR + video_dataset$Normalized.SSIM + video_dataset$Normalized.VIFp)/3, digits = 7)
ratio3_max <- setNames(aggregate(video_dataset$Ratio3, by = list(video_dataset$Video.Name), max), c("Video.Name", "Ratio3"))
ratio3_preset <- merge(ratio3_max, video_dataset, c("Video.Name","Ratio3"))[,c("Video.Name", "Compression.Preset", "Ratio3")]

# DELETING COLUMNS FROM DATASET
drops <- c("Normalized.Size")
video_dataset <- video_dataset[ , !(names(video_dataset) %in% drops)]

# OLD FORMULAS
max_psnr <- setNames(aggregate(video_dataset$Average.PSNR, by = list(video_dataset$Video.Name), max), c("Video.Name", "Normalized.PSNR"))
max_ssim <- setNames(aggregate(video_dataset$Average.SSIM, by = list(video_dataset$Video.Name), max), c("Video.Name", "Normalized.SSIM"))
max_vifp <- setNames(aggregate(video_dataset$Average.VIFp, by = list(video_dataset$Video.Name), max), c("Video.Name", "Normalized.VIFp"))
min_duration <- setNames(aggregate(video_dataset$Compression.Duration, by = list(video_dataset$Video.Name), min), c("Video.Name", "Normalized.Duration"))
min_size <- setNames(aggregate(video_dataset$Compressed.Size, by = list(video_dataset$Video.Name), min), c("Video.Name", "Normalized.Size"))

#summary(video_dataset)

# ALL PLOTS

qplot(x = Compression.Preset, y= Average.PSNR, data = video_dataset) +
  facet_wrap(~Video.Name, scales="free_y")

qplot(x = Compression.Preset, y= Average.SSIM, data = video_dataset) +
  facet_wrap(~Video.Name, scales="free_y")

qplot(x = Compression.Preset, y= Average.VIFp, data = video_dataset) +
  facet_wrap(~Video.Name, scales="free_y")


qplot(x = Compression.Preset, y= Average.VIFp*Average.SSIM*Average.PSNR, data = video_dataset) +
  facet_wrap(~Video.Name, scales="free_y")

# GRAPH AVG PSNR vs DURATION
qplot(y = Compression.Duration, x= Average.PSNR , color = Compression.Preset, data = video_dataset) +
  facet_wrap(~Video.Name, scales="free_y")

# GRAPH NORM PSNR vs DURATION
qplot(y = Compression.Duration, x= Normalized.PSNR , color = Compression.Preset, data = video_dataset) +
  facet_wrap(~Video.Name, scales="free_y")

qplot(y = Ratio2, x= Compression.Preset, data = video_dataset) +
  facet_wrap(~Video.Name, scales="free_y")
