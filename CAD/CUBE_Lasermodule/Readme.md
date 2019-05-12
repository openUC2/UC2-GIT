# LASER Mount Cube
This is the repository for the Laser Mount Cube. 

The stl-files can be found in the folder [STL](./STL).

### Purpose
It adapts a laser-pointer to the to the UC2 system.

![](./IMAGES/Assembly_Cube_Lasermount.png)

The laser-pointer is permanently switched on/off using a 3D printed clamp. It is inserted in a Thorlabs-like adapter which centers the laser on the optical axis. Using a set of rods, this adapter can be mounted inside the base-cube. Having two of these adapters makes the design very robust! 

## Properties
* design is derived from the base-cube
* the adapter for the laser can be adjusted to individual laser-pointer diameters
* the 4 screws make centering of the laser w.r.t. the optical axis easy
* Diode-laser, Multimode lineprofile, Beam
* Peak-Wavelength: ***446 nm ***

	
### Laser Spectrum
The measured sepctrum from the 450nm laser pointer we used for the Lightsheet setup can be found below:
![](./IMAGES/LASER_spectrum.png)

### Laser Power
We measured a mean power of ***0.546 mW*** in continous mode. We used new batteries. 

## Parts

### 3D printing parts 
The Part consists of the following components. 

* **The Lid** where the Arduino + Electronics finds its place ([LID](./STL/Assembly_Cube_Lasermount_10_Lid_el_v0_1.stl))
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/Assembly_Cube_Lasermount_10_Cube_v0_2.stl))
* **The Laser Mount Adapter** which holds the laser and adapts it to the base cube ([INLET](./STL/Assembly_Cube_Lasermount_11_Cube_Adapter_LASER_11.stl))
* **The Laser Clamp** allows switching the laser permanently  ([clamp](./STL/Assembly_Cube_Lasermount_01_Laser_Clamp_OnOffSwitch_15.stl))



### Additional parts 
* 8x DIN912 M3*12 screws (non stainless steel)
* Laserlands 450 nm laser-pointer
* 2x Rod's (50mm*6mm Diameter)

## Remarks and Tips 
### 3D Printing:
* No support required in all designs 
* Carefully remove all support structures (if applicable)

## Assembly
* Prepare the laser-pointer by inserting the batteries
* Insert the 4 screws in the Laser Mount Adapter and screw them thus far so the they are not visible in the inner hole
* Insert the Laserpointer inside the adapter
* Fix the laser by precisely rotate all 4 screws so that the laserpointer is centered
* Insert the rods on one side of the cube
* Put the Laser Mount Adapter inside the cube and mount them on the rods by sliding the rods throught the holes 
* Add the lid to the cube and fix it with the 4 M3 screws
* Done! 

## Safety
Never (!) look into the laser pointer! It will damage your eye immediately!

* ATTENTION: NEVER WATCH DIRECTLY INTO THE LASER! EYE WILL BE DAMAGED DIRECTLY
* NEVER SWITCH ON THE LASER WITHOUT INTEDED USE 
* BEAM HAS TO GO AWAY FROM ONESELF - ALWAYS!
