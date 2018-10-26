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
myramp = np.linspace(-.5, .5, myftholo.shape[1])
plt.plot(myramp)
myramp = np.tile(myramp, (mysize, 1))

# lets now shift our image in fourier space 
shiftamount = 100
myshift = myftholo*np.exp(1j*myramp*2*np.pi*shiftamount)
plt.imshow(np.angle(np.exp(1j*myramp*2*np.pi*10)))
myshift = np.fft.ifft2(np.fft.ifftshift(myshift))
plt.imshow(np.abs(myshift))

# circ puil
x = np.linspace(-.5, .5, myftholo.shape[1])
y = np.linspace(-.5, .5, myftholo.shape[1])
xx,yy = np.meshgrid(x, y)
plt.imshow(xx)
plt.imshow(yy)



# filter our object spectrum 
mycirc = (xx**2 + yy**2)<.1;
myfiltered = myftholo*mycirc
myfiltered  = np.fft.ifft2(np.fft.ifftshift(myfiltered ))
plt.imshow(np.abs(myfiltered ))