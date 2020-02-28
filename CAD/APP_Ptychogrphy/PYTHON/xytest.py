'''
IMPORTANT: Execute as sudo
copyright@Bene
License GPLv3
'''
import serial
import time
import cv2
import csv
import numpy as np
from datetime import datetime
import os
import xystepper as xy

# https://blog.miguelgrinberg.com/post/fun-with-the-arduino-esplora-a-digital-picture-frame

# define your positionfile here
mycsvfile = './DATA/Fermat_FOV1200um_step72um_202points.csv'
# Initialize the USB-Serial connection
serial = serial.Serial("/dev/ttyUSB0",9600)
time.sleep(1) # wait until Arduino settles

# parameters for the x/y stage 
stepsize = 17.27 # One STEPSIZE in X/Y of the cheap-stage  is 17.27 µm

# Initialize position of the XY-stages
myxStepper = xy.xyStepper(myserial=serial, mycurrentposition=0, mystepper='x')
myyStepper = xy.xyStepper(myserial=serial, mycurrentposition=0, mystepper='y')

# Make sure we are at the edge of the stage 
mycmd = myxStepper.reset_pos()
mycmd = myyStepper.reset_pos()


# go to x-step
myxStepper.go_to(50)

# go to x-step
myyStepper.go_to(60)

# go to y-step    
myxStepper.go_to(10)

# go to y-step    
myyStepper.go_to(20)

# go home again
myxStepper.go_to(0)
myyStepper.go_to(0)
