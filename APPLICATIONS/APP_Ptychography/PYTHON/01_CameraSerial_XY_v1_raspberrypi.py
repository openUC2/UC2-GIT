# -*- coding: utf-8 -*-

# GNU nano 2.9.3                                        main.py

'''
IMPORTANT: Execute as sudo
copyright@Bene
License GPLv3
'''
import serial
import time
import cv2
import picamera

# https://blog.miguelgrinberg.com/post/fun-with-the-arduino-esplora-a-digital-picture-frame

# Initialize the USB-Serial connection
serial = serial.Serial("/dev/ttyUSB0",9600)

# Initilizae the Camera
camera = picamera.PiCamera()

# Initialize position of the XY-stages
serial.write(b'Y100')
time.sleep(2)
serial.write(b'X100')


if cap.isOpened():
    window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
   
   
#time.sleep(1)
print('Start programm')

camera.start_preview()

# Flush anything which is on the pipe..
serial.flushInput()

# move stepper forward/backward in X
for ix in range(0,10):
    for iy in range(0,10):
        myfilename = 'myimg_x_'+str(ix)+'_y_'+str(iy)+'.png'
        camera.capture(myfilename)
        serial.write(b'x1')
        time.sleep(1)
    serial.write(b'X11')
    time.sleep(1)
    serial.write(b'y1')
    time.sleep(1)

camera.stop_preview()

serial.write(b'Y100')
time.sleep(2)
serial.write(b'X100')

print('Done')
exit()