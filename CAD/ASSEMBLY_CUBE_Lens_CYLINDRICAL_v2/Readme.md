# Generic Lensholder Cube
This is a lens-holder for rectangular (e.g. cylindrical) lenses.

The stl-files can be found in the folder [STL](./STL).

### Purpose
It adapts the cylindrical lenses from COMAR optics to the UC2 system.

<p align="center">
<img src="./IMAGES/Assembly_Cube_Objectiveholder.png" width="600">
</p>


### Cylindrical lens (in the lightsheet)
Like any other lens, a cylindrical lens focuses the incoming light. In case of a positive focal length, the focal spot can be found right after the lens inside the back focal plane (BFP), usually measured as the focal length of the lens. In case of a cylindrical lens, the focus spot is not a single point as in a rotationally symmetric lens, but rather a line like focus. This is because an incoming parallel beam gets focussed only in one direction. In the eye this sometimes happens and hinders clear eysigth by introducing astigmatism (greek: point-less)

More information:

* [What are cylindrical lenses?](https://www.edmundoptics.com/resources/application-notes/optics/what-are-cylinder-lenses/)
* Comar Optics, 63 YE 25, cylindrical lens 63, coated
*

### Properties
* design is derived from the base-cube
* the adapter can hold a large variety of different lenses (differnt diameters/threads)
* the spiral automatically centers the lens to the optical axis
* the here used objective lens has the following parameters:
	* Thread: RMS
	* Magnification: 4x
	* NA: 0.1
	* Finite Corrected Optics



## Parts

### <img src="./IMAGES/P.png" height="40"> 3D printing parts
The Part consists of the following components.

* **The Lid** where the Arduino + Electronics finds its place ([LID](./STL/10_Lid_1x1_v2.stl))
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/10_Cube_1x1_v2.stl))
* **The Lens Holder** which holds a rect. lens ([HOLDER](./STL/20_Cube_Insert_Lens_Cylindrical.stl))

### <img src="./IMAGES/B.png" height="40"> Additional parts
* 8x DIN912 M3*12 screws (non stainless steel)
* Comar cylindrical lens

## Remarks and Tips
### 3D Printing:
* No support required in all designs
* Carefully remove all support structures (if applicable)

## <img src="./IMAGES/A.png" height="40"> Assembly
* Put the lens inside the insert
* Add the insert to the Cube
* Add screws to the Cube
* Done!


###Tutorial with images (LENSHOLDER)
Don't insert batteries in the laser yet!!

1. All parts for this model
<p align="center">
<img src="./IMAGES/CUBE_LENS_CYLINDRICAL_0.jpg" width="300">
</p>

2. Put all parts together
<p align="center">
<img src="./IMAGES/CUBE_LENS_CYLINDRICAL_1.jpg" width="300">
</p>


## Safety
Attention, don't cut your fingers while removing the lens from the iPhone sensor!

Never (!) look into the laser pointer! It will damage your eye immediately!


* ATTENTION: NEVER WATCH DIRECTLY INTO THE LASER! EYE WILL BE DAMAGED DIRECTLY
* NEVER SWITCH ON THE LASER WITHOUT INTEDED USE
* BEAM HAS TO GO AWAY FROM ONESELF - ALWAYS!
