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
  
##  1.1 Applications
Video sharing platforms like YouTube, Facebook, Instagram process and store millions of
videos every day. This requires exabytes and petabytes of storage on servers [2]. On a similar
ground, Online Streaming Services like Netflix, Amazon Prime, Hotstar aim to provide best
video quality to users for streaming. But the download rates on user’s network fails to cope
with the bitrate of higher quality videos because of slow internet speed. In such a situation
users have no other option but to watch videos in low quality for uninterrupted streaming. <p>
Video Compression Optimization can help to reduce the size of videos while maintaining
maximum quality. This leads to a number of benefits for storage as well as streaming. Even
the slightest of size reductions on each video online can save exabytes of storage. Whereas a
compressed video having a subsequently lower bitrate can help to improve user experience on the same network speed available.
## 1.2 Motivation
The amount of data flow on the internet is growing exponentially every year. This creates a
demand for exponential increase in storage space. Adding to it the fact that rapid developments
in the field of video recording equipment are leading to extremely high qualities, but large-insize videos. Therefore, the overall result increases the costs of buying and maintaining storage
space.<p>
Streaming such high-quality videos becomes an even bigger havoc, given the condition of
network speed in most of the countries. User has to wait for high-quality videos to get buffered
on slow internet speed, creating discomfort. Or else they have to watch videos on low quality
to keep the video uninterrupted from buffering while ruining the user experience.
The need of the hour is to realize that growing video data and improving quality are creating
a strain on the current architecture and must be tackled in the best ways by employing video
compression tools to the fullest.<p>
## 1.3 Objectives
There are a number of video compression tools and algorithms available that can compress
videos, resulting in appreciable loss in size without significant loss in visual information fidelity. This is achieved by varying the parameters used in x265. What makes this process
challenging is identifying the ideal values for all the parameters in order to achieve the best
possible results for a specific video. The optimal values of parameters vary from video to video
depending on the features of the video. A good level of expertise and understanding of the the
x265 encoder is required in order to identify these parameter values.<p>
The objective of this project is to build a Supervised Machine Learning model based on
the training data of optimal compression preset from the encoder. The input for the model will
be any video that has to be compressed and the output will be the optimal compression preset
to achieve maximum possible size reduction, in minimum time with minimal quality loss in
video.<p>
The video datasets available publicly for working are uncategorised. Thus the secondary
objective of the project is preparation of dataset, based on width, height, length of video, frames
per second, bitrate, size of video, motion, intensity and correlation between consecutive frames, so that the resulting labelled dataset can be used for training of model.
## 1.4 Organization of Project Report
Chapter-1 Introduction, provides the essence of the entire project, the need for Video Compression Optimization, it’s applications, objectives and motivation.<p>Chapter-2 Literature Survey, comprises the survey from research papers about various Codecs based Analysis, Container based Analysis, Supervised Machine Learning models and existing Video Compression
approaches using Machine Learning. <p>Chapter-3 Proposed Work, contains insights about parameter prediction using Machine Learning and proposed framework of project. <p>Chapter-4
Simulation and Results, shares information about dataset preparation, the machine learning
models applied and their comparison. <p>Chapter-5 Summary and Future Work, provides the
overall conclusion of the project and the scope of improvement in future.
  
# Chapter 2 Literature Survey
With the advancement of Video related technologies, lots of video compression techniques
and video storage formats have become available. The primary idea that one must understand
is that video compression results in loss of data from original video. So there will be either
significant or negligible difference between the output and the input videos, depending on the
compression method used. The main goal is to achieve maximum possible size reduction with
the minimal quality loss in video in minimum time possible.<p>
A digital video file consists of two parts, a “codec” and a “container”. The codec is used in
compressing and decompressing video. At present, the widely used codecs are H.264, H.265,
VP9 [3]. On the other hand, a container is a collection of files that hold information about both
audio and video data. MKV, AVI and MP4 are some of the popular container types. <p>
There are various efficient and popular machine learning algorithms such as Neural network, random forest, gradient boosting, etc. Here, gradient boosting and random forest are
very useful in small datasets. These machine learning algorithm can be used to improve video
compression methods which is discussed in coming sections. <p>
## 2.1 Codecs based analysis
### 2.1.1 AVC H.264
H.264 is a block-oriented, open source motion-compensation-based standard for video
compression. H.264 standard compares different part of video frames and finds the areas that
are redundant within the subsequent frames. Later on, these areas are replaced by shorter information. These areas are of maximum block-size of 16x16 pixels. It is a lossy compression
method and has the ability to lower the bit rates compared to previous standards such as H.263,
MPEG-4 and Divx. It is mostly used when fast encoding is desired.

### 2.1.2 High Efficiency Video Coding (HEVC) or H.265
H.265 is a royalty-encumbered successor of H.264 standard. It works same as H.264 but instead of blocks, H.265 uses coding tree units (CTU). CTU sizes vary from 4x4 to 64x64 pixels.
So improved CTU segmentation along with better spatial prediction and motion compensation
results in way better bitrate reduction than the H.264. Because of this reason hardware specifications of HEVC is high to compress the data. This allows the users having compatible devices
with required processing power, view 4K videos even on low bandwidth and average network
speed. This compression method drops the bandwidth and storage requirement by roughly 50%
[4].
### 2.1.3 VP9
VP9 is an open source coding format developed by Google working principles of VP9 and
H.265 are same. It is also almost similar to H.265 in terms of encoding quality but it has
a significant advantage when it comes to encoding and decoding speed [5]. Reason for this
is HEVC is much more complex than the VP9. So VP9 can be used with relatively lesser
hardware specifications then H.265. VP9 is widely used in YouTube [6].
### 2.1.4 AV1
AV1 is an open source video coding format. Unlike other codecs, AV1 focuses on the
encoding quality rather than the speed. So the encoding time for AV1 is much higher than that
for VP9 and HEVC but it is a perfect compression standard when the time is not of concern and
highest quality possible is desired [7]. It is used in the transmission of videos over the internet.
The output of video compression using various codecs like HEVC, VP9 or AV1 results in
various qualities and sizes for a specific video. According to a report based on High Definition
(HD) and Ultra High Definition (UHD) videos, HEVC and VP9 are compared for video quality
difference using PSNR [8]. It is concluded that HEVC implementation produces higher PSNR
values as compared to that using VP9 for the same targeted bitrates, under similar encoding
parameters.
## 2.2 Container Based Analysis
1. AVI(Audio Video Interlaced) - It is the most universally supported container but faces
compression limitations. Because of that, video having AVI containers result in large file size. It can contain video and audio tracks only.
2. MP4(MPEG-4 Version 2)-It is widely used with H.264 for video encoding. Subtitle
tracks are also supported in this format.
3. MKV(Matroska Video Container)- It can hold all kinds of audio and video formats
including multiple subtitle tracks, menus and chapters. Thus, it is the most versatile
container.<p>
MP4 is a widely supported container, but MKV is the most popular one because of its
flexibility and broad range of features. Containers don’t affect the quality of the video, but they
limit the encoding method. Therefore, choosing a flexible container such as MKV is the right
choice when one wants better compression.
## 2.3 x265 Encoder Library
To utilize the HEVC/H.265 codec for video, the need for a suitable video encoder application library arises. The most popular x265 is available as an open source library, published
under the GPLv2 license and aims to provide the most efficient, highest performance HEVC
video encoder. <p>
The various encoding parameters used in x265 are categorized in ten predefined presets that
affect the trade-off between compression efficiency and encoding speed. The presets are :
- ultra fast
- super fast
- very fast
- faster
- fast
- medium (default)
- slow
- slower
- very slow
- placebo
<p>These presets include 32 parameters which are varied differently. The most significant
parameters are shown in Table 2.1
 <p> <img width="791" alt="Screen Shot 2022-08-22 at 11 26 34 AM" src="https://user-images.githubusercontent.com/28559153/185992699-145507bb-0047-41c0-bc5e-8c6f3fd46c6f.png">

### 2.3.1 Experiment
A 58 seconds long video of size 128 MB, having a bit rate of 17.3 Mb/s, with the total
frame count of 1759 and resolution of 1920x1080 was compressed with x265 encoder using
above mentioned presets. By using the Video Quality Measurement Tool (VQMT), metrics like
PSNR, SSIM and VIFP were generated by comparing original video and compressed video.<p>
PSNR - Peak Signal to Noise Ratio. It is used to compare quality between compressed
image and the original image. Higher PSNR suggests that quality loss was minimal.<p>
SSIM - Structural Similarity Index. It is a metric which gives image quality degradation
caused by compression. The value lies between -1 and 1, where the value corresponding to 1
signifies similar images.<p>
VIFP - Visual Information Fidelity in pixel domain. It is part of the Human Visual System
(HVS). It is derived from two quantities: when no distortion channel is present then the mutual
information between the input and the output of the HVS channel and information between the
input of the distortion channel and the output of the HVS channel for the image.<p>
Comparison of different presets for every metric is provided as follows.
  
<img width="775" alt="Screen Shot 2022-08-22 at 11 29 06 AM" src="https://user-images.githubusercontent.com/28559153/185993405-95451ae5-db24-40a6-bfbc-c3c3be8667d6.png">

<img width="847" alt="Screen Shot 2022-08-22 at 11 29 17 AM" src="https://user-images.githubusercontent.com/28559153/185993220-e7671d82-1c5e-4205-84fe-8330712f1c9e.png">
<img width="838" alt="Screen Shot 2022-08-22 at 11 29 28 AM" src="https://user-images.githubusercontent.com/28559153/185993235-a5d23de2-9c09-4c2c-95b9-ef26c1425003.png">
  
<p>The result is determined from the graphs in Figures 2.1 to 2.6 and shown in the Table 2.2. It
includes Average PSNR, Standard Deviation of PSNR, Average SSIM, Standard Deviation of
SSIM, Average VIFP, Standard Deviation of VIFP, Bitrate of compressed file and time required
for compression for every preset of x265 encoder.<p>
It is clear that preset Placebo gives the highest value of PSNR, SSIM and VIFP. It means
that it retains most quality in the compressed video, as compared to other presets. Deviation
of Placebo is very high, suggesting that it varies frame to frame. Faster and Very Fast presets
give similar and lowest value for every metric. Also, bitrate is low for them which results in
less size, as the bitrate is directly proportional to the size. Super Fast takes less time but still,
average PSNR value is higher compared to other fast presets. Placebo requires the highest time
for compression while Ultra Fast requires the lowest.<p>
Hence time, size and quality are the three measures of video compression. If the requirement is to retain maximum quality, then Placebo is the suitable preset, but it trades off with
longest encoding time. If a smaller size of video is required then Faster preset is useful and if
faster encoding time is required then Ultra Fast preset is useful.<p>
  Another parameter that is varied in x265 encoder is CRF. It stands for Constant Rate Factor
and is used to set the quality factor of the output video. Comparing two different videos with
CRF values set at 25 and 28 while keeping same presets, it can be easily noticed from the
graphs of PSNR, SSIM, VIFP as shown in Figures 2.7,2.8 and 2.9 that video encoded with
CRF 25 has a significantly lower loss in quality as compared to CRF 28.
  <img width="683" alt="Screen Shot 2022-08-22 at 11 32 51 AM" src="https://user-images.githubusercontent.com/28559153/185993728-e737df4b-5017-4bb1-8d74-c2ccc5e53dc2.png">

## 2.4 Working of H.265/HEVC
The HEVC standard is based on a hybrid model which incorporates motion estimation and
compensation, transforms and quantization, and entropy encoding[9]. The two models used are
the prediction model and the spatial model.<p>
The prediction model utilizes the redundancies present in the spatial and temporal domain.
The inter prediction of the frames is done based on two factors: 1) Motion Estimation(ME):
finding the best match between regions of reference and past or future frames, and 2) Motion
Compensation(MC): finding the difference between matching regions. The output of the prediction model is residuals and motion vectors. Residual is the difference between a matched
region and the reference region. A motion vector is a vector that indicates the direction in
which block is moving and it determines the offset by which a reference block to the current
block is located in the past or future picture.<p>
The spatial model deals with transformation and quantization. Here transformation reduces
the dependency between sample points, and quantization reduces the precision at which samples are represented. The most commonly used transformation is the Discrete Cosine Transform(DCT). The output from DCT is coefficients that are further quantized to reduce the number of bits required for coding it. Quantization could be scalar or vector based. Scalar quantization maps the range of values to scalars, while vector quantization maps a group of values,
such as image samples, into a codeword. Further Run-Length Encoding(RLE) is used to store
consecutive occurrences of a digit as a single value together with digit’s count.<p>
From the above topics, it can be said that compression revolves around the presence of motion in the video.
 ### 2.4.1 Experiment
To determine the impact of motion in compression, two 15 seconds long, different motion
videos were recorded with a smartphone in the same environment. Here one video has a static
background with a moving subject while another video has a moving background with moving subject. Both videos are compressed with 3 different presets: faster, medium and slower.
Then the quality comparison is done using VQMT. We also compare the output sizes after
compression with the presets.<p>
As seen in Table 2.3, for all three presets, the PSNR, SSIM or VIFp values does not vary
much indicating that the compressed video quality is very similar. Similarly for the dynamic
video, from Table 2.4, the compressed quality remains similar regardless of the presets.<p>
  
<img width="569" alt="Screen Shot 2022-08-22 at 11 35 26 AM" src="https://user-images.githubusercontent.com/28559153/185994131-44790bb4-0867-49dd-a600-f9b560c12353.png">
<p>While the encoding time for the presets vary widely for both the videos. Then it can be said
that rather than choosing a slower preset we can select a faster preset, and have similar quality
with less time taken for the compression. Also from the Table 2.5, it can be seen that motion
affects the output size after compression. Under the same preset the size of the compressed
dynamic video is double to that of the compressed static video.
## 2.5 Neural Network
Neural network is a collection of interconnected artificial neurons. Each neuron transfers
information to the next layer. All these layers combine together to form a neural network.
Weights are assigned to each connection between neurons and the value of weights are tuned in
training phase of the model. A well-trained neural network will work efficiently in any image
classification domain. As shown in the Fig. 2.10, each layer has numerous neurons that have
different inputs from the previous layer and based on that they give different outputs to the next
layer.<p>
 First layer is called input layer which detects basic patterns from input image. Middle layers
are called hidden layers which work like biological neurons. They recognize patterns from the
input patterns. Last layer is output layer which gives classification factors based on patterns
detected.<p>
  

<img width="467" alt="Screen Shot 2022-08-22 at 11 36 17 AM" src="https://user-images.githubusercontent.com/28559153/185994326-43e6128b-e7ee-463a-a3b0-6a7683e8c603.png"><p>
### 2.5.1 Training With Back-propagation
A dataset consisting of labeled inputs with corresponding intended output, is required in
training process. Iterative methods are applied to neural networks which determines the weights
for each layers. In Fig. 2.13, a complete training process with back-propagation model is
shown.
  <p><img width="704" alt="Screen Shot 2022-08-22 at 11 37 38 AM" src="https://user-images.githubusercontent.com/28559153/185994530-2ea411d1-d8fa-4ee2-9679-d1d2aefdfec7.png"><p>

Initially, in Back-propagation method, random weights are assigned to all the nodes. Then,
based on those values outputs of each layer is calculated. At the output layer, error is calculated
with the help of desired output and predicted outputs. This error is propagated to the previous
layers and their weights are updated based on the Optimizer Function. This whole procedure is
repeated number of epoch times [10].
## 2.6 Ensemble Learning Algorithms: Bagging and Boosting
In any Machine Learning approach, difference in actual and predicted output comes because
of bias, variance and noise. Ensemble learning algorithms such as bagging and boosting help
to reduce these types of errors [11]. In general Machine Learning models, there is only one

predictor which tries to predict the output. But, ensemble uses the collection of predictors that
helps predict same output variable, causing increase in efficiency. There are two algorithms:
Bagging & Boosting, which can be used as Ensemble learning algorithms.
  <p>  <img width="640" alt="Screen Shot 2022-08-22 at 11 39 54 AM" src="https://user-images.githubusercontent.com/28559153/185995099-c2f29266-ed5c-4cae-be79-e63b03989bb8.png"><p>
 
### 2.6.1 Bagging
<p>It is a simple method of ensemble learning algorithm where there are number of predictors
or learners in parallel form and predict output using average techniques such as weighted average, normal average or majority vote. The main goal of bagging is reducing the variance of
decision tree. Random forest is an extension of the concept of bagging and uses multiple number of trees. Each tree takes a random subset of input data. Rather than employing all features,
a random selection of features is undertaken. So, the best feature for splitting node is identified,
instead of the most important feature. Therefore, by using Random forest for training the data
along with ensemble, the output is predicted with better accuracy under a weighted average.<p>

  ### 2.6.2 Boosting
<p>It is a method of ensemble learning algorithm which supports predictor or classifier in
sequential form such that every classifier can learn from previous classifier’s mistake and tries
to boost those errors. There is a chance of overfitting on training data. Gradient boosting is an
extension of boosting algorithm. Usually the ML models require the mean square error to be
minimum. In gradient boosting, gradient descent method is useful to reduce this error using
predictors.
