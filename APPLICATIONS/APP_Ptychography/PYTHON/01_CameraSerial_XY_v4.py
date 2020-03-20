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
import csv
import numpy as np
import time, datetime, os
import xystepper as xy

# https://blog.miguelgrinberg.com/post/fun-with-the-arduino-esplora-a-digital-picture-frame

# define your positionfile here
mycsvfile = './DATA/Fermat_FOV1200um_step72um_202points.csv'
# Initialize the USB-Serial connection
serial = serial.Serial("/dev/ttyUSB0",9600)
time.sleep(1) # connect to ARduino

# parameters for the x/y stage 
stepsize = 17.27 # One STEPSIZE in X/Y of the cheap-stage  is 17.27 µm
myoffsetx = 10  # offset steps for the x dirrection
myoffsety = 20 # offset steps for the y dirrection
##

# create folder for measurements
todaystr = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
myfolder = './ptycho_'+todaystr
os.mkdir(myfolder)


# Initilizae the Camera
#cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)
#cap = cv2.VideoCapture('gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, format=BGRx ! ximagesink')
cap = cv2.VideoCapture('v4l2src device=/dev/video0 ! video/x-raw, format=BGRx ! videoconvert  ! appsink', cv2.CAP_GSTREAMER)
#cap = cv2.VideoCapture(0)

# Initialize position of the XY-stages
myxStepper = xy.xyStepper(myserial=serial, mycurrentposition=0, mystepper='x')
myyStepper = xy.xyStepper(myserial=serial, mycurrentposition=0, mystepper='y')

# Make sure we are at the edge of the stage 
mycmd = myxStepper.reset_pos()
mycmd = myyStepper.reset_pos()


# read in the file with all positions 
with open(mycsvfile, 'r') as f:
    data = list(csv.reader(f, delimiter=";"))
myscanpoints = np.array(data[1:-1], dtype=np.float)
maxpos = np.max(myscanpoints,axis=0)*2
myscanpoints/=maxpos
minpos = np.min(myscanpoints,axis=0)
myscanpoints-=minpos

# only if matplotlib is installed...
try:
    import matplotlib.pyplot as plt
    plt.plot(myscanpoints[:,1],myscanpoints[:,0],'x'), plt.show()
except:
    print('No matplotlib is installed..')

if cap.isOpened():
    window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
   
   
print('Start programm')

# Flush anything which is on the pipe..
serial.flushInput()

# move stepper forward/backward in X
for i_scan in range(0, len(myscanpoints)):
    # compute the correct scan position
    ix = int(myscanpoints[i_scan,0]*maxpos[0]/stepsize)+myoffsetx
    iy = int(myscanpoints[i_scan,1]*maxpos[1]/stepsize)+myoffsety
    print(str(ix)+'/'+str(iy))

    # go to x-step
    myxStepper.go_to(ix)
    # go to y-step    
    myyStepper.go_to(iy)

    # grab a frame and wait until the camera settles
    ret_val, img = cap.read()
    time.sleep(1)

    # write out the image information
    cv2.imwrite(myfolder+'/'+str(i_scan)+'.tif', img)



# Reset position of X/Y stepper
mycmd = myxStepper.reset_pos()
mycmd = myyStepper.reset_pos()

print('Done')
exit()
