# SIM alignment tutorial

This tutorial is aming to align the openSIM module of the UC2 modular 3D printed microscope. The fundamental is a set of full prepared components in hand, which listed in the ```readme.md``` for openSIM. The parts used for aligning the system are:

  - openSIM module
  - optical components
  - UC2 cubes and inserts
  - target sample
  - magical hands

## Align the camera
In the openSIM setup, the camera module is arranged on the bottom layer, therefore, it needs to focus to infinity first. Try to find a far away object (e.g a building or mountain) and image it with the camera clearly by adjusting the distance between the camera and the tube lens. Following image shows an example image took by an infinity-focused camera.

<p align="center">
<img src="./IMAGES/CameraToInfinity.jpg" width="500">
</p>

***Fig. 1*** *An example image of an infinity-corrected camera. The mountain on the picture is far away from our office.*

When the camera is infinity-focused, the bottom layer of the system can be placed as shown here:

<p align="center">
<img src="./IMAGES/BottomLayer.png" width="500">
</p>

***Fig. 2*** *A top view of the system's bottom layer which contains camera module. This layer consists of camera and some empty cubes as support.*
	
In this layer, it has some empty cubes spread around in order to support the upper layers.

## Align the illumination laser source
The laser we used is a 638 nm diode laser. In order to get a bigger spot size to illuminate the active area of the DMD, the collimation lens in front of the laser is removed and a 20 mm lens collimating the convergent beam again is set in front of this assembly. Move the laser on its mount back and forth to collimate the laser. Check the beam size in front of the lens as well as far away, it should keep the same size and larger than the mirror array of the DMD. For more information, please also have a look in this [tutorial](../CAD/ASSEMBLY_CUBE_Beamexpander_v2).

<p align="center">
<img src="./IMAGES/CollimatedLaserSource.jpg" width="500">
</p>

***Fig. 3*** *The laser beam is collimated by the 20 mm lens and the beam size doesn't change with the propagation distance.*

## Prepare Fourier mask 

The telescope consists of two 50mm achromatic lenses and a fourier mask, which block the zero-order illumination and regenerate the intermediate image of the DMD at the focus the second lens. The telescope is fixed in the openSIM module.

<p align="center">
<img src="./IMAGES/FirstLayer.png" width="500">
</p>

***Fig. 4*** *Illumination part of the openSIM setup. The laser beam is expanded and illuminates on the DMD mirror area. The zero-order of the beam is blocked in the first telescope, the two first-order beam will focus and interference at the sample plane with the tube lens and objective.*

A 3D printed Fourier mask is applied in the telescope, the 3D model of the mask case can be found in the ``STL`` repository. One thin copper wire is splitted from electric cable, first make a small knot on the wire which is roughly the size of the desired tin drop. Then solder a small drop of soldering tin onto the knot.

<p align="center">
<img src="./IMAGES/KnotOnWire.png" width="800">
</p>

***Fig. 5*** *A single copper wire is taken from an electrical cable (left), a knot is crossed on the wire and can easliy add correct size of soldering tin on it.*

Mount the wire on the 3D printed part with the help of glue or fix gum, such as [UHU Patafix](https://www.uhu.de/de/produkt.3311). In order to aviod unexpected reflextion of the soldering tin, we can use black color marker pen and paint on the tin drop. At the end, the tin drop should be positioned at the middle of the mask. 
 
<p align="center">
<img src="./IMAGES/FourierMaskInBlack.png" width="400">
</p>

***Fig. 6*** *A prepared Fourier mask which has a soldering tin painted with black on it. The copper wire is fixed with fix gum.*

## Alignement of the first Achromat

First we want to make sure, that the achromate lens which faces the DMD does a proper Fourier transform by means of placing it exactly one focal length away from the DMD. 
It is of great help to start with a collimated light source such as a Laser diode/pointer (or any other collimated light source) inside an [UC2 laser cube](../CAD/ASSEMBLY_CUBE_Beamexpander_v2) which will produce the focal spot within the focal lenght of the lens. The laser is placed directly in front of the exit of the openSIM module i.e. the position of the first reflecting mirror out of the SIM module. This has to coincide with the DMD mirror plane. In order to make the two planes matching, you have to move the achromatic lens back and forth. You will find the proper position, when the diffraction pattern of the DMD (reflection) has the smallest spots. 

## Alignment of the telescope

The goal is to have a plane wave in- and outcoming of the telescope consisting of the two 50mm achromates. Now, we have to insert the second achromatic lens. We use the collimated light source to  and heading to the DMD mirror, if the telescope is good calibrated, the laser beam should illuminate onto the DMD chip with its original spot size.

## Bring the system to the table

### Setup the Raspberry Pi
The DMD is controlled by Raspberry Pi, when the Raspberry Pi connected with the DMD we need to remote control it with a PC for display images. For transport the generated illunimation images or python code to raspberry pi, using [WinSCP](https://winscp.net/eng/download.php) on Windows or [Putty](https://www.putty.org/) on Mac makes it easier.

Turn on a WiFi Hotspot such as
```
SSID: Blynk
Password: 12345678
```
Turn on the Raspberry Pi and wait until it connects. Note the IP Address of the Pi (in our case ```192.168.43.9```). Connect to the Pi with SSH on you computer using the following line:
```
ssh pi@192.168.43.9
```
The default password of Raspberry Pi is ``raspberry``. Then we need to activate the external display of Raspi with the command:
```
export DISPLAY=:0
```
The grating pattern we used is generated by a python script ``pygame_grating.py``. The grating is default set in vertical direction and the grating constant is 6 pixel size of the DMD micromirror and rolling 1 pixel distance in each second. You can end the infinite loop with ``Ctrl + C``.

### Coarse adjustment of the mirrors
The setup has two mirrors to direct the illumination beam to the objective. The aim of adjust the mirrors is to reflect the laser beam straightly into the objective. The mirror has three directional flexibilities which can be changed by the screws behind the kinetic mirror mount. The mirrors should be plugged onto the base one by one, and after each mirror the propagation direction of the beam should stay the same with the optical axis.

When raw adjustment is done, set the tube lens and the dichroic mirror at their position, the frequency of the DMD image should be located and focused at the position of the back focal plane of the objective. When the python script ``pygame_grating.py`` is running on the Raspberry Pi, three beams should located at the center of the cube.
For proper alignment make sure the following steps are met:
- zero order is going through the center of each cube (i.e. optical axis)
- +/-1st diffraciton order is symmetrically oriented inside the BFP (e.g. place a paper in the position of the BFP and tune the mirrors 1/2)


<p align="center">
<img src="./IMAGES/ThreeBeamOnBFP.jpg" width="500">
</p>

***Fig. 7*** *Three beam pattern should locate at the center of the back focal plane of the objective.*

### Fine adjustment of the mirrors

Insert the [objective cube and linear z-stage](../CAD/ASSEMBLY_CUBE_Z-STAGE_v3) with bright LED illumination (***PLEASE UPLOAD ME***) above the dichroic mirror, use one surface reflecting sample, such as a [negative Thorlabs USAF Target](https://www.thorlabs.com/thorproduct.cfm?partnumber=R3L1S4N). Move some structures of the target into the field of view, and adjust the linear stage to focus on the structures sharply. At that time, it should be some unclear DMD illumination signal on the sample. (When not, it is recommanded to go back to adjust the direction of the two mirrors, make the propagation direction of the laser beam parallel to the axial direction of the objective.) Keep the target structure sharp and adjust the two mirrors, make the illumination pattern sharp at the sample plane. With a three beam interference, the image generated by ``pygame_grating.py`` with grating constant of 6 pixel size should look like this:

<p align="center">
<img src="./IMAGES/ThreeBeamInterferenceCamera.png" width="500">
</p>

***Fig. 8*** *Three beam interference at the sample plane. Left above is a structure from the USAF target, right grating is the illumination pattern from the DMD.*

***Troubleshooting***: 

- *Sample and illumination plane do not coincide:* Try to carefully move the 50mm achromatic lens (L2) 
- *I see a black bar blocking my sample on the camera:* Try to adjust the mirror facing the camera to move the picture that the center of the optical axis coincides with the camera chip.

## Adjustment of the Fourier-filter

Then remove the objective from the system and place a piece paper in the position of the BFP. Now insert the Fourier filter on the metal plate inside the openSIM module. Try adjusting the position of the Fourier mask in XY in the telescope to block such that the tin drop blocks the zero-order of the illumination. Make sure you block the zeroth "harmonic" of the diffracted light from the DMD (i.e. highest intensity in the Fourier plane). Make sure, that the thin wires won't block or disturb the first order signal (e.g. rotate it slightly). To check the process, hold a small piece of paper at the position of the back focal plan, their should be only two first-order spot left like this:

<p align="center">
<img src="./IMAGES/IlluWithoutZeroOrder.jpg" width="500" rotate="90">
</p>

***Fig. 9*** *Using the Fourier mask to block the zero-order illumination. You can easily check the block efficiency with a paper by removing the objective from the system.*

Place the objective back, put again a paper slightly above the sample plane, you should observe two same-shaped beam spot. 

<p align="center">
<img src="./IMAGES/TwoBeamOnTheObjective.jpg" width="500">
</p>

***Fig. 10*** *The two beam is interferencing at the sample plane and divergent above the sample plane.*

Refocus onto the target sample, the two beam interference pattern should be shown on the camera. If not, try to slightly tilt the mirror to refocus the both patterns on the sample plane. A example image is shown as below:

<p align="center">
<img src="./IMAGES/TwoBeamInterferenceCamera.png" width="500">
</p>

***Fig. 11*** *The expected two beam interference pattern on the camera. Right side is the detail of the interference pattern.*


## Ready for play

Now the openSIM setup is ready to play. Enjoy the new toy!

<p align="center">
<img src="./IMAGES/FullSetup.png" width='650'>
</p>

***Fig. 12*** *Overview of the SIM/ISM setup.*


