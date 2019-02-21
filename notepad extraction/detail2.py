# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:00:44 2019

@author: PRIYANSHZALAVADIYA
"""

mypath = "F:/project/furry-lamp/notepad extraction/"
video_name="main.log"
video_name2="main2.log"
f = open(mypath+video_name, "r")
searchlines = f.readlines()
f.close()




logname=video_name
for line in searchlines:
    if "Complete name" in line:
        ro=line
        break
flag=0
name=""
ro=ro.replace(" ", "")
ro = ro.strip('\n')
for i in ro:
    if i is ":":
        flag=1
        continue
    if flag is 1:
        name+=i
print(name)
c=0
for line in searchlines:
    if "Bit rate" in line: 
        r=line
        c=c+1
        if c is 3 :
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
    if "Duration" in line: 
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
    
    
     
    

flag=0
vbitrate=""
r=r.replace(" ", "")
r = r.strip('\n')
for i in r:
    if i is ":":
        flag=1
        continue
    if flag is 1:
        vbitrate+=i
fr=vbitrate
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
r3=r3.replace(" ", "")
r3=r3.strip('\n')
for i in r3:
    if i is ":":
        flag=1
        
        continue
    if flag is 1:
        duration+=i
    
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



f = open(mypath+video_name2, "r")
searchlines2 = f.readlines()
f.close()
for line in searchlines2:
    if "encoded" in line:
        r6=line
        break
print(r6)
flag=0
fram=""
totaltime=""
c=2
for i in r6:
    if i is " " and flag is 0:
        flag=1
        continue
    if flag is 1:
        if i is " ":
            flag=2
            continue
        fram+=i
    if flag is 2:
        if i is " ":
            c-=1
        if c is 0:
            if i is 's':
                break
            totaltime+=i
totaltime=totaltime.replace(" ", "")                
print(totaltime)        
totalframes=fram.replace(" ", "")                
print(totalframes)    
