# Integrated Telescope/Beam-Expander Cube
This is the repository for the Integrated Telescope Cube.

The stl-files can be found in the folder [STL](./STL).

### Purpose
It adapts a very small beam-expander to the UC2 system.

<p align="center">
<img src="./IMAGES/Assembly_Cube_Beamexpander_v2.png" width="400">
</p>

Sometimes one need to increase the diameter of an illuminating beam. This is necessary for the Light-sheet microscopy setup for example. Here we have a laser-pointer which comes with a relatively small beam-diameter of about 2mm. By using a telescope, this can be magnified by a factor of e.g. 8 which results in a beam-diameter of 16 mm. This is necessary to overfill the aperture of the following illumination objective lens.

In order to achieve this, we first need to focus the beam with a low focal length lens (e.g. cellphone lens, f'=3mm) and then re-collimate the lens with a second lens with a larger focal length e.g. f'=25 mm.

We designed a telescope where an iPhone 5 lens and an ordinary 25mm lens can be inserted in an adapter, which finds its place inside an ordinary UC2-cube as visualized in the image above.

## Properties
* design is derived from the base-cube
* the adapter for the telescope can be adjusted for different magnifications and lenses
* the beam height can be adjusted by sliding the the telescope along the axis
* the degree of collimation can be adjusted beforehand  * very cost-efficient beam-expander at a fairly good quality as the cellphone lens is diffraction limited (overall costs ~15€)
* Magnification : m=f<sub>tl</sub>/f<sub>ep</sub> = 25/3 = 8.33

## Parts

### 3D printing parts
The Part consists of the following components.

* **The Lid** where the Arduino + Electronics finds its place ([LID](./STL/Assembly_Cube_Beamexpander_10_Lid_1x1_v2.stl))
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/Assembly_Cube_Beamexpander_10_Cube_1x1_v2.stl))
* **The Telescope** which holds the two lenses and  adapts them to the base cube ([TELESCOPE](./STL/Assembly_Cube_Beamexpander_20_Cube_Insert_Beamexpander.stl))

### Additional parts
* 4x DIN912 M3*12 screws (non stainless steel)
* iPhone 5 lens (separated from an iPhone camera spare part), f'=3mm
* biconvex/plan-convex lens, f'=25mm, diameter=20mm, thickness=4mm

## Remarks and Tips
### 3D Printing:
* No support required in all designs
* Carefully remove all support structures (if applicable)

## Assembly
* Remove the iPhone lens from the camera (a dedicated tutorial can be found in the [UC2 Tutorial-Section](/TUTORIAL).
* Insert the lenses inside the telescope adapter (orientation of the iPhone has to be the way, that the small aperture - hole - has to face the other bigger lens as indicated by the photo)
![](./IMAGES/Beamexpander_Assembly_1.png)

* Take the laser-pointer
* Point the laser towards the iPhone Lens
* Adjust the distance between the two lenses, so that the beam is collimated (=the beam diameter right after the telescope should not change over any distance)
* Put the telescope inside the cube by sliding it along the slides

![](./IMAGES/Beamexpander_Assembly_2.png)

* Add the lid to the cube and fix it with the 4 M3 screws
* Done!

![](./IMAGES/Beamexpander_Assembly_3.png)

### Tutorial with images (for UC2 v0)
Don't insert batteries in the laser yet!!

1. All parts for this model
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube1.jpg" width="300">
</p>

1. Mount the first lens
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube2.jpg" width="300">
</p>

1. Mount the cellphone lens
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube3.jpg" width="300">
</p>

1. Fix the cellphone lens with blutek
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube4.jpg" width="300">
</p>

1. Insert the telescope into the cube
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube7.jpg" width="300">
</p>

1. Insert the telescope into the cube II
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube8.jpg" width="300">
</p>

1. Assemble the cube with screws
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube9.jpg" width="300">
</p>

1. Assembled:
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube10.jpg" width="300">
</p>

#### Finetune the lens-distance (collimate the beam)

1. Add the centered laser to the grid like so:
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube5.jpg" width="300">
</p>

1. Turn on the laser:
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube6.jpg" width="300">
</p>

1. Optional: Align the laser (center with the screws)
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube11.jpg" width="300">
</p>

1. Check the beam on a white piece of paper
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube12.jpg" width="300">
</p>

1. Mark the position and diamter of the beam on the white piece of paper
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube14.jpg" width="300">
</p>

1. Compare distance and diameter of laser spot at a distance far away
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube15.jpg" width="300">
</p>

1. Adjust the position of the cellphone lens in the rail so that both spots have the same position and diameter (iterate - start at step 5 - until you're satisfied)
<p align="center">
<img src="./IMAGES/UC2_Tut_Beamexpandercube13.jpg" width="300">
</p>





## Safety
Attention, don't cut your fingers while removing the lens from the iPhone sensor!

Never (!) look into the laser pointer! It will damage your eye immediately!


* ATTENTION: NEVER WATCH DIRECTLY INTO THE LASER! EYE WILL BE DAMAGED DIRECTLY
* NEVER SWITCH ON THE LASER WITHOUT INTEDED USE
* BEAM HAS TO GO AWAY FROM ONESELF - ALWAYS!
