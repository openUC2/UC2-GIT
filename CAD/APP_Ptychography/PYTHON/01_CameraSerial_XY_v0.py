# -*- coding: utf-8 -*-

 GNU nano 2.9.3                                        main.py

'''
IMPORTANT: Execute as sudo
copyright@Bene
License GPLv3
'''
import serial
import time
mport cv2

# https://blog.miguelgrinberg.com/post/fun-with-the-arduino-esplora-a-digital-picture-frame

# Initialize the USB-Serial connection
serial = serial.Serial("/dev/ttyUSB0",9600)

# Initilizae the Camera
cap = cv2.VideoCapture(0)


if cap.isOpened():
    window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
    
    
#time.sleep(1)
print('Start programm')

# Flush anything which is on the pipe..
serial.flushInput()



 


# move stepper forward/backward in X
for ix in range(0,10):
    for iy in range(0,10):
        ret_val, img = cap.read()
        cv2.imwrite('myimg'+str(ix)+'.png', img)
        serial.write(b'x10')
        time.sleep(1)
    serial.write(b'y10')
    time.sleep(1)

serial.write(b'Y100')
time.sleep(2)
serial.write(b'X100')

print('Done')
exit()
