
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imresize 


is_display = True  # swith to use SLM or not 

if(is_display):
    import slmpy
    slm = slmpy.SLMdisplay(isImageLock = True, monitor = 2)
    resX, resY = slm.getSize()

resX, resY = 1920, 720
resX_disp, resY_disp = 1920, 720

# We use images twice smaller than the resolution of the slm
ImgResX = resX//2
ImgResY = resY//2


mydistance = 10 # distance between peaks 
npattern = 50 # how many times the pattern has to be displayed along X/Y
i = 0;
dx = 0
dy = 0
for dx in range(mydistance):
        for dy in range(mydistance):
                subpattern = np.zeros((mydistance, mydistance))
                subpattern[dx,dy] = 1
                mypattern = np.tile(subpattern, (npattern, npattern))
                testIMG = np.zeros((resY, resX))
                if False:
                    plt.imshow(mypattern)
                    plt.show()

                testIMG[int(ImgResY-np.floor(mydistance*npattern/2)):int(ImgResY+np.floor(mydistance*npattern/2)), int(ImgResX-np.floor(mydistance*npattern/2)):int(ImgResX+np.floor(mydistance*npattern/2))] = mypattern
                
                # testIMG = imresize(testIMG, (resY_disp, resX_disp), 'bicubic')
                testIMG = np.round(testIMG*(2**8-1))
                testIMG = np.dstack((testIMG, testIMG, testIMG))
                
                if(is_display):
                    slm.updateArray(np.transpose(testIMG))
                    time.sleep(0.05)
                else:
                    plt.imsave('./raw/image_'+str(i)+'.png', testIMG)
                i=i+1
                print(str(i))
if(is_display):
    slm.close()
    
    
    
myimage = np.zeros((1280,720))    
mypattern = (0, 1)
mypattern = np.tile(mypattern, (1280/2, 720))
#myimage[:,0]=mypattern 
testIMG = np.round(myimage*(2**8-1))
testIMG = np.dstack((testIMG, testIMG, testIMG))
plt.imsave('testimage.png', testIMG)
                