# Generic Lensholder Cube
This is a lens-holder for rectangular (e.g. cylindrical) lenses.

The stl-files can be found in the folder [STL](./STL).

## Purpose
It adapts the cylindrical lenses from COMAR optics to the UC2 system.

<p align="center">
<img src="./IMAGES/Assembly_Cube_Objectiveholder.png" width="300">
</p>

### Cylindrical lens (in the light sheet)
Like any other lens, a cylindrical lens focuses the incoming light. In case of a positive focal length, the focal spot can be found right after the lens inside the back focal plane (BFP), usually measured as the focal length of the lens. In case of a cylindrical lens, the focus spot is not a single point as in a rotationally symmetric lens, but rather a line like focus. This is because an incoming parallel beam gets focussed only in one direction. In the eye this sometimes happens and hinders clear eyesight by introducing astigmatism (greek: point-less)

More information:

* [What are cylindrical lenses?](https://www.edmundoptics.com/resources/application-notes/optics/what-are-cylinder-lenses/)
* Comar Optics, 63 YE 25, cylindrical lens 63, coated


### Properties
* design is derived from the base-cube
* the adapter can hold a large variety of different lenses (different diameters/threads)
* the spiral automatically centers the lens to the optical axis
* the here used objective lens has the following parameters:
	* Thread: RMS
	* Magnification: 4x
	* NA: 0.1
	* Finite Corrected Optics

## Parts

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

* **The Lid** where the Arduino + Electronics finds its place ([LID](./STL/10_Lid_1x1_v2.stl))
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/10_Cube_1x1_v2.stl))
* **The Lens Holder** which holds a rect. lens ([HOLDER](./STL/20_Cube_Insert_Lens_Cylindrical.stl))

### <img src="./IMAGES/B.png" height="40"> Additional parts
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
* 8× DIN912 M3×12 screws (galvanized steel) [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* Comar cylindrical lens, f' = 63 mm (63 YQ 40) [🢂](https://www.comaroptics.com/components/lenses/cylindrical-lenses/quality-planoconvex-cylindrical-lenses-visibleuv#row-63_yq_40)


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
Don't touch the lens' surfaces!
