# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 07:51:03 2019

@author: diederichbenedict
"""

import numpy as np
import matplotlib.pyplot as plt 
import skvideo.io
import NanoImagingPack as nip
import tifffile as tif
import cv2 

#define some parameters
mysize = (460, 640) # worked good!
mysize = (360, 640) # worked good!


n_periods = 35

ringdiameter = 150


# create the patterns
rot_offset = 1*np.pi/5
iterator = 0
for rot_dim in range(3):#((0,0,0)):#range(3):
    for shift_dim in range(3):
        mypattern_i = np.sin(2*np.pi*(np.cos(np.pi*rot_dim/3+rot_offset)*nip.xx(mysize, freq='ftfreq')+np.sin(np.pi*rot_dim/3+rot_offset)*nip.yy(mysize, freq='ftfreq'))*n_periods+shift_dim*np.pi/3)
        mypattern_i *= (nip.rr(mypattern_i.shape)<ringdiameter)
        mypattern_i = 1-np.float32(mypattern_i>=0)
        cv2.imwrite('./IMAGES/'+str(iterator)+'.bmp', mypattern_i/np.max(mypattern_i)*255)
        plt.imshow(mypattern_i), plt.colorbar(), plt.show()
        
                
        iterator += 1
        print(iterator)
    
