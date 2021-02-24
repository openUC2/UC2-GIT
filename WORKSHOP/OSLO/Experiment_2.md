## Experiment – 2
Build a device to see the effect of Fourier-filtering (e.g. "ABBE-Experiment")

The idea is to see the effect of Fourier filtering during image formation by placing an aperture inside the back focal plane (BFP) of the imaging lens.

All information about the setup can be found [here](../../APPLICATIONS/APP_Abbe_Setup)


## Steps

First of all you have to fuse two boxes since you need more optical elements than a single box can provide. So fuse with your neighbor

1. Look for the right lenses which have a focal-length of ~40-50mm
2. Align the illumination: Take the LED-module (blue) and a lens which collimates it
3. Take the sample mount (looks like comp) and place it right after the first lens so that the sample gets illuminated by the illumination
4. Take a second lens as the imaging lens so that the sample is roughly within the focal plane of it
5. Now take the beam-splitter cube and place it directly behind the comb-like cube
6. Two additional lenses have to be placed after the BS-cube to form an image and access the Fourier plane on two different cameras (have a look at the figure from the link above)
7. Turn on the Raspberry PI where you have connected the Cameras and start the camera using: ```raspistill -k```for constant-mode from the Raspberry PI Terminal
8. Taking image can be achieved by doing the following steps:
	- go to home-folder ```cd ./data```
	- take images using ```raspistill -o myimage_1.jpg```where ```myimage_1``` is a name of your choice


## Tasks

First think about what could happened; Does this go hand-in-hand of what happens in the experiment? :-)

- Vary illumination source shape by taking aluminum foil and stitch different patterns in it to vary the degree of coherence
	- What happens on the Fourier-cam?
- Take a piece of paper and place it in the BFP of the imaging lens, try different shapes.
	- What happens to the image on the raspberry pi camera?
