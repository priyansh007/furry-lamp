# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:04:12 2019

@author: PRIYANSHZALAVADIYA
"""

from os import listdir
from os.path import isfile, join
mypath = "F:/project/compression details/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    
