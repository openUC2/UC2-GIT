# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:59:24 2019

@author: diederichbenedict
"""

import numpy as np
import rawpy

import NanoImagingPack as nip
import tifffile as tif

mycropsize = 1024
mybinning = 1
iFile = 1

myfilename = 'I_obj'

allFilesStack = []

while 1:
    # determine path for files
    readpath = myfilename+ ' ('+ str(iFile)+').dng'
    writepath = myfilename+ ' ('+ str(iFile)+').tif'
    
    try:
        print('Reading file: ' + str(iFile))
        # read filepath
        with rawpy.imread(readpath) as raw:
            rgb = raw.raw_image# ()#gamma=(1,1), no_auto_bright=True, output_bps=16)
            rgb = np.array(rgb)
        
        # convert bayer pattern to green channel
        mysize = rgb.shape
        mygreen = rgb[1:-1:2,0:-1:2]
    
        
        # bin image and save it
        mygreenframe = nip.resample(mygreen, (1/mybinning,1/mybinning))
        mygreenframe = nip.extract(mygreenframe,(mycropsize,mycropsize), (1528,1343))
        #nip.view(np.log(nip.ft(mygreenframe)))
        #nip.view(mygreenframe)
        
        tif.imsave(writepath, mygreenframe)
    
        allFilesStack.append(mygreenframe)
        iFile += 1
        

    except:
        print('All files have been read')
        break

myallfiles = np.array(allFilesStack)
tif.imsave(writepath+'_stack.tif', myallfiles)
nip.v5(nip.ft2d(myallfiles))
nip.v5((myallfiles))