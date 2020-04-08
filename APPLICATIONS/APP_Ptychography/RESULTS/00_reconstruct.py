#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:44:07 2020

@author: bene
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.ndimage import gaussian_filter


# Set file-path
mypath = './ptycho_2020-03-02_18-36-35_DIATOMES/'
mypath = './ptycho_2020-03-02_16-59-15_Mouseemryo/'
mypath = './ptycho_2020-03-02_16-59-15_MAIZE_STEM_ZEA_MAYS/'
mypath = './ptycho_2020-02-29_19-29-56_USAF/'
mypath = './ptycho_2020-03-10_15-19-08/'


myfile = glob.glob(mypath+"*.csv")[0]
mypixelsize = 17.27
mypositions = np.genfromtxt(myfile, delimiter=';')
mypositions/=mypixelsize 
mypositions = np.uint32(mypositions)
# generate bitmap grid

myminx = np.min(mypositions[:,0])
myminy = np.min(mypositions[:,1])
mymaxx = np.max(mypositions[:,0])
mymaxy = np.max(mypositions[:,1])
myresult = np.zeros((mymaxx+1, mymaxy+1))

#%
for ifile in range(mypositions.shape[0]):
    myiImage = plt.imread(mypath+str(ifile)+'.tif')
    myiSum = np.sum(myiImage)
    
    myresult[mypositions[ifile,0],mypositions[ifile,1]] = myiSum
    
    print('Computing: ' + str(ifile) + '/' + str(mypositions.shape[0]))
# display the result
plt.subplot(121)
plt.imshow(myresult)
plt.subplot(122)
plt.imshow(gaussian_filter(myresult, sigma=1))
    
    