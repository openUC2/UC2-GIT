#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:04:08 2019

@author: bene
"""

import NanoImagingPack as nip
import matplotlib.pyplot as plt


nip.config.setDefault('IMG_VIEWER', 'NIP_VIEW')

mysize = (720, 1920)
mycirc = nip.rr(mysize)<50

plt.imsave('optical_alignment.png', mycirc, cmap='gray')



myimage = nip.readim()
myimage_ft = np.abs(nip.ft(myimage))