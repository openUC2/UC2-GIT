# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:55:03 2021

@author: diederichbenedict
"""
# rename the following pattern:
#   *v3_XXX.stl -> *v3.stl    
#       or
#   *_XXX.stl -> v3 (more generic!)


import os

delimiter = '_'
filetype = '.stl'
basefolder = 'C:\\Users\\diederichbenedict\\Dropbox\\Dokumente\\Promotion\\PROJECTS\\UC2-GIT\\CAD\\RAW\\STL\\'
basefolder = '/Users/bene/Dropbox/Dokumente/Promotion/PROJECTS/UC2-GIT/CAD/RAW/STL/'

import glob, os
os.chdir(basefolder)
for filename in glob.glob("*"+filetype):
    filename_final = ''
    
    filename_split = filename.split(delimiter)
    for i in range(len(filename_split)-1):
        if not filename_split[i] == 'v3':
            filename_final += (filename_split[i] + delimiter)
        
    filename_final += 'v3'+filetype
        
    print(filename + " -> " + filename_final)
    
    # rename
    os.rename(filename,filename_final)
