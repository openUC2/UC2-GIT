#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:24:49 2020

@author: bene
"""
#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import serial
import time
import cv2
import csv
import numpy as np
import time, datetime, os
import xystepper as xy
import buf_cam as bufcam

# This is the Publisher
MQTT_BROKER = "192.168.43.9"
MQTT_TOPIC = "opensim/pattern"
CAMERA = '/dev/video0'
NPATTERN = 9
EXTENSION = ".bmp"

# connect to display-server
client = mqtt.Client()
client.connect(MQTT_BROKER,1883,60)

# camera paramters 
myexp_time = 500000 # 180849 #200000  # min=177293 max=2147483647 step=5434 default=18137798 value=18136663 flags=slider
myexp_time = input('Enter a exposure time (in milliseconds, default=500ms): ')
myexp_time=100000*int(myexp_time)

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

#ake a background image first! 
print("Blank the beam for five seconds") 
time.sleep(5)
# grab a frame and wait until the camera settles
print('Darkframe was acquired frame')
mydarkframe = cap.read()
print('Remove the Beamblocker')
mydarkframe = cv2.cvtColor(mydarkframe, cv2.COLOR_BGR2GRAY)
cv2.imwrite(myfolder+'/background.tif', mydarkframe)



print('Start programm')

# move stepper forward/backward in X
myposlist = []
try:
    for i_PATTERN in range(0, NPATTERN):
        print('ADDRESSING PATTERN#: '+str(i_PATTERN)+' :-> x/y ' + str(ix)+'/'+str(iy))
        client.publish(MQTT_TOPIC, str(i_PATTERN)+EXTENSION);
        time.sleep(2)
        
	    # grab a frame and wait until the camera settles
	    #print('Grabbing frame')
	    img = cap.read()

	    # write out the image information
	    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    cv2.imwrite(myfolder+'/'+str(i_PATTERN)+'.tif', (img))
except:
	print('I will first shut down the programm properly')

cap.cap.release

print('Done')
client.disconnect();
exit()
