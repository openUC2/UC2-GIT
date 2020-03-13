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
import bufcam as bufcam

# https://blog.miguelgrinberg.com/post/fun-with-the-arduino-esplora-a-digital-picture-frame

# define your positionfile here
mycsvfile = './DATA/Fermat_FOV1200um_step72um_202points.csv'
# Initialize the USB-Serial connection
serial = serial.Serial("/dev/ttyUSB0",9600)
time.sleep(1) # connect to ARduino
# camera paramters 



# parameters for the x/y stage 
stepsize = 17.27 # One STEPSIZE in X/Y of the cheap-stage  is 17.27 µm
myoffsetx = 10  # offset steps for the x dirrection
myoffsety = 20 # offset steps for the y dirrection
mybacklashx = 10
mybacklashy = 50 # this is required to offset the stage from the non-moving rim

# Initialize position of the XY-stages
myxStepper = xy.xyStepper(myserial=serial, mycurrentposition=0, mystepper='x', backlash=mybacklashx)
myyStepper = xy.xyStepper(myserial=serial, mycurrentposition=0, mystepper='y', backlash=mybacklashy)

# Make sure we are at the edge of the stage 
#myyStepper.reset_pos()
#myxStepper.reset_pos()

# read in the file with all positions 
with open(mycsvfile, 'r') as f:
    data = list(csv.reader(f, delimiter=";"))
myscanpoints = np.array(data[1:-1], dtype=np.float)
maxpos = np.max(myscanpoints,axis=0)
myscanpoints/=(maxpos*2)
minpos = np.min(myscanpoints,axis=0)
myscanpoints-=minpos

# only if matplotlib is installed...
try:
    a
    print('Please close the figure to start with the scanning!')
    import matplotlib.pyplot as plt
    plt.plot(np.int32(myscanpoints[:,1]*maxpos[0]/stepsize)*stepsize,np.int32(myscanpoints[:,0]*maxpos[0]/stepsize)*stepsize,'x')
    plt.show()
except:
    print('No matplotlib is installed..')


print('Start programm')

# Flush anything which is on the pipe..
serial.flushInput()

ix = int(myscanpoints[0,0]*maxpos[0]/stepsize)
iy = int(myscanpoints[0,1]*maxpos[1]/stepsize)
# go to x-step
myxStepper.go_to(ix+myoffsetx)
# go to y-step    
myyStepper.go_to(iy+myoffsety)
# move stepper forward/backward in X
myposlist = []
try:
	for i_scan in range(0, len(myscanpoints)):
	    # compute the correct scan position
	    ix = int(myscanpoints[i_scan,0]*maxpos[0]/stepsize)
	    iy = int(myscanpoints[i_scan,1]*maxpos[1]/stepsize)
	    myposlist.append((ix*stepsize,iy*stepsize))
	    print('Scan-number: '+str(i_scan)+' :-> x/y ' + str(ix)+'/'+str(iy))

	    # go to x-step
	    myxStepper.go_to(ix+myoffsetx)
	    # go to y-step    
	    myyStepper.go_to(iy+myoffsety)

except:
	print('I will first shut down the programm properly')

# write pos-vlaues to list
print('Writing poslist-file')
np.savetxt('myscanlist_texp_.csv', np.array(myposlist), delimiter=';')

myposlist.insert(0, ('y','x')) 
with open('myscanlist_xy_texp_.csv', 'w', newline='') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)#, delimiter=';')
	wr.writerow(myposlist) 

print('Done')
exit()
