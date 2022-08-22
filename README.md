# Abstract
A video is the most efficient way of representing various types of information, be it visual or audio. The video
traffic on the internet along with the size of these videos is increasing day by day. Here, x265 is identified as
the most suitable encoder. But for encoding the video, preset and parameters have to be passed which requires
expertise. The primary focus of the project is to automate the compression method for the x265 encoder. A
machine learning approach can be used to predict the preset for the x265 encoder by learning some features
about the video. The set of features that are found to affect video compression include video resolution, object
motion, picture clarity, level of detail, correlation between consecutive frames and dynamic background. Based
on the set of videos, a custom dataset is prepared for training the model, comprising of encoded videos under
various presets used in x265 encoder that optimizes the trade-off between encoding speed, visual quality loss and
compression efficiency. This dataset will include the presets used for encoding, size of the output video, time
required for compression, metrics used to identify quality loss after compression. A Machine Learning model
is prepared, that provides the optimal preset to be used by x265 encoder for efficient compression of any given
video.
- Keywords- Video Compression - Machine Learning - x265 encoder

# Chapter 1 Introduction

In today’s world of fast-growing technology, Video is becoming the primary form of media
among all sorts of users, accounting to the amount of knowledge that a user gets easily from
a video, as compared to that from audio, photo or textual media. A report by Forbes provides
some interesting figures about the exploding growth of the Video market [1]. Video traffic on
the internet will account for 80% of the whole internet traffic worldwide by 2019. YouTube
generates a 2 fold increase in mobile video consumption every year. Facebook registers 8
billion views on videos per day approximately. <p>
With that enormous increase in data flow of video, the subsequent costs that follow are
the storage of millions of videos along with the highest retainable quality. This creates a bottleneck for the growth of video media industries, as they look towards ‘Video Compression’
for reducing the storage size while making compromises with video quality, that may lead to
customer dissatisfaction, as the users often wish to view their videos in the highest possible
quality. Here’s where video compression optimization comes into the picture, as the project
exploits x265 encoder in order to achieve maximum compression while minimizing quality loss and in videos.

