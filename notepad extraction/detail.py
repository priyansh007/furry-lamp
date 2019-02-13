# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:04:12 2019

@author: PRIYANSHZALAVADIYA
"""

f = open("20170825_100649_fast_25_staxrip.log", "r")
searchlines = f.readlines()
f.close()

for line in searchlines:
    if "Bit rate" in line: 
        r=line
        break
for line in searchlines:
    if "Width" in line: 
        r1=line
        break
for line in searchlines:
    if "Height" in line: 
        r2=line
        break
for line in searchlines:
    if "mdhd_Duration" in line: 
        r3=line
        break
c=0
for line in searchlines:
    if "Frame rate" in line: 
        r4=line
        c=c+1
        if c is 2 :
            break
for line in searchlines:
    if "Stream size" in line: 
        r5=line
        break


#print(r5)
flag=0
vbitrate=""
for i in r:
    if i is ":":
        flag=1
        continue
    if flag is 1:
        vbitrate+=i
    if i is "s":
        break


fr=vbitrate.replace(" ", "")
vbitrate=''
for i in fr:
    if i is 'M' or i is 'k':
        break
    vbitrate+=i
vbitrate=float(vbitrate)
if 'M' in fr :
    vbitrate=vbitrate*1024        
print(vbitrate)



flag=0
width=''
for i in r1:
    if i is ':':
        flag=1
        continue
    if flag is 1:
        width+=i
    if i is 's':
        break


widt=width.replace(" ", "")
width=''
for i in widt:
    if i is 'p':
        break
    width+=i
width=int(width)    
print(width)


flag=0
height=""
for i in r2:
    if i is ":":
        flag=1
        continue
    if flag is 1:
        height+=i
    if i is "s":
        break

hei=height.replace(" ", "")
height=''
for i in hei:
    if i is 'p':
        break
    height+=i
height=int(height)        
print(height)

flag=0
duration=""

for i in r3:
    if i is ":":
        flag=1
        
        continue
    if flag is 1:
        duration+=i
    if i is int:
        break

duration=duration.replace(" ", "")


duration=int(duration)  
m=duration/100000
s=duration/1000
duration=int(m)*60+int(s)      
print(duration)


flag=0
framerate=""
for i in r4:
    if i is ":":
        flag=1
        continue
    if flag is 1:
        framerate+=i
    if i is "S":
        break

fr=framerate.replace(" ", "")
framerate=''
for i in fr:
    if i is 'F':
        break
    framerate+=i
framerate=float(framerate)        
print(framerate)

flag=0
streamsize=""
for i in r5:
    if i is ":":
        flag=1
        continue
    if flag is 1:
        streamsize+=i
    if i is ")":
        break

fr=streamsize.replace(" ", "")
streamsize=''
for i in fr:
    if i is 'M' or i is 'K':
        break
    streamsize+=i
streamsize=float(streamsize)
if 'M' in fr :
    streamsize=streamsize*1024        
print(streamsize)





for line in searchlines:
    if "Bit rate" in line: 
        rr1=r
        r=line
flag=0
cvbitrate=""
for i in rr1:
    if i is ":":
        flag=1
        continue
    if flag is 1:
        cvbitrate+=i
    if i is "s":
        break
fr=cvbitrate.replace(" ", "")
cvbitrate=''
for i in fr:
    if i is 'M' or i is 'k':
        break
    cvbitrate+=i
cvbitrate=float(cvbitrate)
if 'M' in fr :
    cvbitrate=cvbitrate*1024        
print(cvbitrate)





for line in searchlines:
    if "Stream size" in line: 
        rr3=r
        r=line
flag=0
cstreamsize=""
for i in rr3:
    if i is ":":
        flag=1
        continue
    if flag is 1:
        cstreamsize+=i
    if i is ")":
        break
fr=cstreamsize.replace(" ", "")
cstreamsize=''
for i in fr:
    if i is 'M' or i is 'K':
        break
    cstreamsize+=i
cstreamsize=float(cstreamsize)
if 'M' in fr :
    cstreamsize=cstreamsize*1024        
print(cstreamsize)



for line in searchlines:
    if "Duration" in line: 
        rr4=line

flag=0
tduration=""
flagg="0"
for i in rr4:
    if i is ":" and flagg is "0":
        flag=1
        continue
    if flag is 1:
        flagg="1"
        tduration+=i
    if i is "s":
        break


def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

tduration=get_sec(tduration)
print(tduration)
import csv

csvData = [['videobitrate','width','height','duration','framerate','streamsize','compressedvideobitrate','compressedvideostreamsize','compressionduration',], [vbitrate,width,height,duration,framerate,streamsize,cvbitrate,cstreamsize,tduration,]]

with open('main.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()
