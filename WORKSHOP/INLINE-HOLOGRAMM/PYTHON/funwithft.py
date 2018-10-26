#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:41:07 2018

@author: bene
"""


# manage the imports
import numpy as np
import matplotlib.pyplot as plt
import os
import time



# load image
my_holo_file = 'test_microplastic.jpg'

# read the raw-hologram
myholo = 1.*plt.imread(my_holo_file);

myholo = np.squeeze(myholo[:,:,2])
mysize = np.min(myholo.shape)
myholo = myholo[0:mysize, 0:mysize]

plt.imshow(myholo, cmap='gray');

# now do the fourier transform 
myftholo = np.fft.fftshift(np.fft.fft2(myholo))
plt.imshow(np.log(1+np.abs(myftholo)), cmap='gray')

# creating phase mask
myramp = np.linspace(0, myftholo.shape[1])/myftholo.shape[1]-.5
