# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 12:09:54 2017

@author: Matt
"""

import os
from glob import glob
from shutil import copyfile
import ntpath

ntpath.basename("a/b/c")

files = []
start_dir = "F:/Storage/White Computer/"
pattern   = "*.jpg"

for dir,_,_ in os.walk(start_dir):
    files.extend(glob(os.path.join(dir,pattern)))
    
files_stripped = [os.path.basename(file) for file in files]

for i in range(len(files)):
    copyfile(files[i],"E:/Unsorted pictures/" + files_stripped[i])