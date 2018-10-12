# -*- coding: utf-8 -*-
# This code reconstructs an in-line hologram captured with the Raspberry Pi Setup

# manage the imports
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import FresnelPropagator as FP
import MultiSliceViewer as MSV



# Taken from this link: https://matplotlib.org/2.1.2/gallery/animation/image_slices_viewer.html

class IndexTracker(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('use scroll wheel to navigate images')

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices//2

        self.im = ax.imshow(self.X[:, :, self.ind])
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()



# define some experimental parameters
my_holo_file = 'beads_holo_3.jpg'
my_background_file = 'test2bg.jpg'
mychannel = 2 # select the color channel 0,1,2
mysize = 1024 # region of interest around the center coordinate 

# define acquisition parameters
pixelsize = 1.4e-6; #0.6e-6#.2e-6#3.000e-6;
lambda0 = 440e-9; # in nanometer #530e-9;

# start and stop z-focus measure
stepsize = 0.0001;

# read the raw-hologram
myholo = 1.*plt.imread(my_holo_file);
                      
# select only the blue channel (because we used the blue LED)                     
myholo = myholo[:,:,mychannel ]

# if we acquired the background, subtract it! 
if(0):
    mybak = 1.*imread(my_background_file)
    mybak = mybak[:,:,mychannel ]
    myholo = myholo/(20+mybak) # add some value to avoid dividing by zero

# crop out the ROI around the center to speed up computation (RADIX 2 please!)
holosize = myholo.shape
myholo =  myholo[int(holosize[0]/2-mysize/2):int(holosize[0]/2+mysize/2), int(holosize[0]/2-mysize/2):int(holosize[0]/2+mysize/2)]

# display intermediate result 
plt.imshow(myholo)
plt.colorbar()
plt.show()

# normalize hologram
myholo = myholo/np.max(myholo);

# estimate hologram's amplitude
myamplitude = np.sqrt(myholo); 

j = 0;
## Backpropagate the Hologram
# Fresnel Propagation - test out a range of z-values to find the one that
# brings the bug into focus
myholo_rec = [];
for i in range(0,100):
    #     [Ef, H] = fresnelprop(hologram,lambda,i,ps);
    zpos = i*stepsize;
    Ef = FP.FresnelPropagator(myholo, pixelsize, lambda0, zpos)
    
    myholo_rec.append(FP.abssqr(Ef))
    
    print("Now processed z-slice number"+str(i)+" at z-position (mum) "+str(zpos))
    
# convert list to numpy array  
myholo_rec = np.array(myholo_rec)
myholo_rec = np.transpose(myholo_rec, [1,2,0]) # make sure Z-axis is the last one

# now create a 3D image-stack viewer
fig, ax = plt.subplots(1, 1)
tracker = IndexTracker(ax, myholo_rec)


fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
plt.show()
   
