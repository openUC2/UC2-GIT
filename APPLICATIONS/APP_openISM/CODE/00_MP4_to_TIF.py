# -*- coding: utf-8 -*-
import skvideo.io
import skvideo.datasets
import numpy as np
import tifffile as tif
import matplotlib.pyplot as plt
import NanoImagingPack as nip 



#myvideofile = '2019-06-13_15.07.46_Fluctuation_Cardio_Mayoblast_Cellphone_Largelens.mp4'

myvideopath = 'C://Users//diederichbenedict//Dropbox//STORMonAcheaip//STORM-on-a-chea(i)p//'
myvideofile = 'MOV_2019_07_09_17_24_52.mp4'
myvideofile = 'MOV_2019_07_09_17_24_24.mp4'

myvideopath = 'C://Users//diederichbenedict//Dropbox//Camera Uploads//'

myvideofile = '2019-08-06 16.57.35.mp4'
myvideofile = '2019-08-06 16.46.29.mp4'

#myvideopath = 'C:/Users/diederichbenedict/Downloads/'
myvideofile = 'MOV_2019_08_12_10_41_31.mp4'

myvideofile = '2019-08-16 12.55.06.mp4'
myvideofile = '2019-08-16 17.42.44.mp4'
myvideofile = '2019-08-23 19.26.06.mp4'
myvideopath = '/Users/bene/Downloads/'
myvideofile = '2019-08-30 18.21.47.mp4' #     gray = nip.extract(gray, ROIsize=(512,512), centerpos=(600,2000))
myvideofile = '2019-08-30 18.19.11.mp4' # gray = nip.extract(gray, ROIsize=(512,512), centerpos=(650,2100))
myvideofile = '2019-08-16 18.02.15.mp4' #     gray = nip.extract(gray, ROIsize=(512,512), centerpos=(950,2300))

# HeLas from Haoran:
myvideopath = 'C://Users//diederichbenedict//Dropbox//Camera Uploads//'
myvideofile = '2019-09-17 10.09.27.mp4'
myroisize = 1024
mycenterpos=(850,2000)

outputfile = myvideofile+'.tif'
myvideofile = myvideopath+myvideofile
videogen = skvideo.io.vreader(myvideofile)


iiter = 0
myimlist = []
for frame in videogen:
    #%%
    gray = np.mean(frame, 2)
    gray = nip.extract(gray, ROIsize=(myroisize,myroisize), centerpos=mycenterpos)
    #nip.view(gray)
    #%%
    #tif.imsave(outputfile, np.uint8(gray), append=True, bigtiff=True) #compression='lzw',     
    iiter+=1
    #kljh
    
    print(iiter)
    myimlist.append(gray)

myimage = np.array(myimlist[230:-1])
tif.imsave(outputfile, np.uint8(myimage), append=False, bigtiff=True) #compression='lzw',     


myres = np.max(myimage, axis=0)+np.min(myimage, axis=0)-2*np.mean(myimage, axis=0)
myres_bf = np.mean(myimage, axis=0)
plt.imshow(myres,cmap='gray'), plt.title('hyperconfocal'), plt.show()
plt.imshow(myres_bf,cmap='gray'), plt.title('brightfield'), plt.show()
tif.imsave(outputfile+"hyperconfocal.tif", myres, append=False, bigtiff=True) #compression='lzw',     
tif.imsave(outputfile+"bf.tif", myres_bf, append=False, bigtiff=True) #compression='lzw',     

nip.v5(myres)