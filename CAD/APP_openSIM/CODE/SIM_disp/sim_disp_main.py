#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:50:58 2020

@author: bene
"""

#!/usr/bin/env python

import pygame
import sys
import time
import glob
from decimal import *
from pygame.locals import *
import paho.mqtt.client as mqtt
 

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

 
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("message received: ", msg)
    print("message topic: ", message.topic)
    display_image(msg)
 
def on_connect(client, userdata, flags, rc):
    client.subscribe('opensim/pattern')
 
BROKER_ADDRESS = "localhost"

# setup MQTT related stuff
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(BROKER_ADDRESS)
 
print("Connected to MQTT Broker: " + BROKER_ADDRESS)
 
# Setup Image display stuff
# MAXIMUM picture display sizes
max_width = 640
max_height = 320

# display time in seconds
display = 20

# randomise pictures, 0 = NO, 1 = YES
pic_rand = 1

# Directory name
DIR_NAME ="./IMAGES/"


# run remotely_ type_ export DISPLAY=:0
# https://raspberrypi.stackexchange.com/questions/83245/pygame-run-on-external-screen-using-ssh
try:
    client.loop_forever()
except:
    print('Shutting down the programm...')
    pygame.quit()
    exit()

        

