# IMPORTING ESSENTIAL LIBRARIES
library(ggplot2)

# VIDEO WISE PLOT FOR QUALITY METRICES VS PRESETS
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

# VIDEO WISE PLOT FOR METRIC VS PRESETS
qplot(x = Metric, y= Compression.Preset, data = video_dataset)+
  facet_wrap(~Video.Name, scales="free_y") 

qplot(data = dataset_with_output_preset, x = Ratio2, y =Avg.Motion, color = Compression.Preset)

qplot(data = dataset_with_output_preset, x = Ratio2, y =Avg.PCC, color = Compression.Preset)
