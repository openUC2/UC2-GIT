#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:50:58 2020

@author: bene
"""

#!/usr/bin/env python

import pygame
import time
from pygame.locals import *
import numpy as np
import os
import cv2
import time, datetime, os
import bufcam as bufcam

def create_ism_pattern(Nx=1920, Ny=1080, dillu=2, dpattern=10, color=[100,100,100], ipattern=0):
    #define some parameters
    mysize = (Nx, Ny) # worked good!
    R,G,B = color[0], color[1], color[2]
    mysize_pinhole = dillu
    myspacing_pinhole = dpattern
    rep_x = mysize[0]//myspacing_pinhole
    rep_y = mysize[1]//myspacing_pinhole
    
    #%% create the patterns
    mypattern_sub = np.zeros((myspacing_pinhole,myspacing_pinhole))
    mypattern_sub[0:mysize_pinhole, 0:mysize_pinhole] = 1
    mypattern_all = np.zeros((mysize[0],mysize[1],3))
    
    print('Creating ISM-patterns...')
    x_dim = ipattern%dpattern
    y_dim = ipattern//dpattern
    
    
    mypattern_i = np.tile(mypattern_sub, [rep_x, rep_y])
    mypattern_i = np.roll(mypattern_i, x_dim, axis=0) # shift along X
    mypattern_i = np.roll(mypattern_i, y_dim, axis=1) # shift along Y

    mypattern_all[:,:,0]=R*mypattern_i[0:mysize[0],0:mysize[1]]
    mypattern_all[:,:,1]=G*mypattern_i[0:mysize[0],0:mysize[1]]
    mypattern_all[:,:,2]=B*mypattern_i[0:mysize[0],0:mysize[1]]
    
    return mypattern_all


def display_image(imagefile):
    #https://www.raspberrypi.org/forums/viewtopic.php?t=121796
    try:
        myfile = DIR_NAME+imagefile
        image = pygame.image.load(myfile)
        size = image.get_rect()
        width = size[2]
        height = size[3]
        # fullscreen
        windowSurfaceObj = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
        
        windowSurfaceObj.blit(image,(0,0))
        pygame.display.update()
        print("display image!")
    except Exception as e: 
        print('Could not display image: '+myfile )
        print(e)

 
# camera paramters 
myexp_time = 500000 # 180849 #200000  # min=177293 max=2147483647 step=5434 default=18137798 value=18136663 flags=slider
myexp_time = input('Enter a exposure time (in milliseconds, default=500ms): ')
myexp_time=100000*int(myexp_time)
CAMERA = '/dev/video0'

# create folder for measurements
mydatafolder = './RESULTS/'
try: 
	os.mkdir(mydatafolder)	
except: 
	print('Folder already exists')
todaystr = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
myfolder = mydatafolder + 'ptycho_'+todaystr
os.mkdir(myfolder)

# Initilizae the Camera
print('Opening camera: '+CAMERA+' with t_exp='+str(1000000/1e6)+'s')
CAMERA_PIPELINE = 'v4l2src device='+ CAMERA+ ' extra-controls='+'"'+'c,exposure='+str(myexp_time)+',exposure_auto=1'+'"' +' ! video/x-raw, format=BGRx ! videoconvert ! appsink'
print("Camera Pipeine: "+CAMERA_PIPELINE)

# open camera object and display object
cap = bufcam.VideoCapture(CAMERA_PIPELINE) 



# Setup Image display stuff
# MAXIMUM picture display sizes
max_width = 1920
max_height = 1080
dillu = 1
dpattern = 9
color = [255,255,255]


# display time in seconds
display = 20

# generate the pictures

NPATTERN = dpattern**2

print('Start programm')

# move stepper forward/backward in X
myposlist = []
# run remotely_ type_ export DISPLAY=:0
# https://raspberrypi.stackexchange.com/questions/83245/pygame-run-on-external-screen-using-ssh
try:
    for i_PATTERN in range(0, NPATTERN):
        print('ADDRESSING PATTERN#: '+str(i_PATTERN))
        mypattern=create_ism_pattern(Nx=max_width, Ny=max_height, dillu=dillu, dpattern=dpattern, color=color, ipattern=i_PATTERN)
        display_image(mypattern)
        time.sleep(2)
        # grab a frame and wait until the camera settles
        #print('Grabbing frame')
        img = cap.read()
        # write out the image information
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(myfolder+'/'+str(i_PATTERN)+'.tif', (img))
except:
    print('I will first shut down the programm properly')
    pygame.quit()
    cap.cap.release
    
cap.cap.release

print('Done')


        

