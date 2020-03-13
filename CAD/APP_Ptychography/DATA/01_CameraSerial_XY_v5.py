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

# camera paramters 
myexp_time = 17750849 #200000  # min=177293 max=2147483647 step=5434 default=18137798 value=18136663 flags=slider
mycamera = '/dev/video0'
# parameters for the x/y stage 
stepsize = 17.27 # One STEPSIZE in X/Y of the cheap-stage  is 17.27 µm
myoffsetx = 10  # offset steps for the x dirrection
myoffsety = 20 # offset steps for the y dirrection
mybacklashx = 15
mybacklashy = 30
##

# create folder for measurements
todaystr = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
myfolder = './ptycho_'+todaystr
os.mkdir(myfolder)


# Initilizae the Camera
print('Opening camera: '+mycamera+' with t_exp='+str(1000000/1e6)+'s')
#cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)
#cap = cv2.VideoCapture('gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, format=BGRx ! ximagesink')#
mycam_cmd = 'v4l2src device='+ mycamera+ ' extra-controls='+'"'+'c,exposure='+str(myexp_time)+',exposure_auto=1'+'"' +' ! video/x-raw, format=BGRx ! videoconvert ! appsink'
#v4l2src device=/dev/video0 extra-controls="c,exposure=200000,exposure_auto=1" ! video/x-raw, format=BGRx ! ximagesink

print(mycam_cmd)
# open camera object and display object
cap = cv2.VideoCapture(mycam_cmd, cv2.CAP_GSTREAMER)
cap.set(cv2.CAP_PROP_CONVERT_RGB, False);          # Request raw camera data
window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)


# take a background image first! 
print("Blank the beam for five seconds") 
#time.sleep(1)
#ret_val, img = cap.read()

# write out the image information
if(False):#ret_val):
	print(ret_val)
	frame_16 = img.view(dtype=np.int16)       # reinterpret data as 16-bit pixels
	frame_sh = np.right_shift(frame_16, 2)      # Shift away the bottom 2 bits
	frame_8  = frame_sh.astype(np.uint8)        # Keep the top 8 bits       
	img      = frame_8.reshape(img.shape[0], img.shape[1])        # Arrange them into a rectangle

#cv2.imwrite(myfolder+'/background.tif', img)
try:
    cv2.imshow("CSI Camera", img)
except:
    print('Could not display frame?!')


# Initialize position of the XY-stages
myxStepper = xy.xyStepper(myserial=serial, mycurrentposition=0, mystepper='x', backlash=mybacklashx)
myyStepper = xy.xyStepper(myserial=serial, mycurrentposition=0, mystepper='y', backlash=mybacklashy)

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


print('Start programm')

# Flush anything which is on the pipe..
serial.flushInput()

# move stepper forward/backward in X
myposlist = []
for i_scan in range(0, len(myscanpoints)):
    # compute the correct scan position
    ix = int(myscanpoints[i_scan,0]*maxpos[0]/stepsize)
    iy = int(myscanpoints[i_scan,1]*maxpos[1]/stepsize)
    myposlist.append((ix,iy))
    print('Scan-number: '+str(i_scan)+' :-> x/y' + str(ix)+'/'+str(iy))

    # go to x-step
    myxStepper.go_to(ix+myoffsetx)
    # go to y-step    
    myyStepper.go_to(iy+myoffsety)

    time.sleep(4)


    # grab a frame and wait until the camera settles
    print('Grabbing frame')
    ret_val, img = cap.read()

    # write out the image information
    cv2.imwrite(myfolder+'/'+str(i_scan)+'.tif', (img))

# Reset position of X/Y stepper
mycmd = myxStepper.reset_pos()
mycmd = myyStepper.reset_pos()

# write pos-vlaues to list
print('Writing poslist-file')
np.savetxt(myfolder+'/myscanlist.csv', np.array(myposlist), delimiter=';')


print('Done')
exit()
