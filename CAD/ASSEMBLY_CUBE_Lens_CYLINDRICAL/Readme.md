# Cylindrical Lens holder Cube
This is a lens-holder for rectangular (e.g. cylindrical) lenses.

To acquire the STL-files use the [UC2-Configurator](https://uc2configurator.netlify.app/). The files themselves are in the [RAW](../RAW/STL) folder. The module can be built using injection-moulded (IM) or 3D-printed (3DP) cubes.

## Purpose
It adapts the cylindrical lenses from COMAR optics to the UC2 system.

<p align="center">
<img src="./IMAGES/Assembly_Cube_Lens_Cylindrical_v3.png" width="300">
</p>

### Cylindrical lens (in the light sheet)
Like any other lens, a cylindrical lens focuses the incoming light. In case of a positive focal length, the focal spot can be found right after the lens inside the back focal plane (BFP), usually measured as the focal length of the lens. In case of a cylindrical lens, the focus spot is not a single point as in a rotationally symmetric lens, but rather a line like focus. This is because an incoming parallel beam gets focussed only in one direction. In the eye this sometimes happens and hinders clear eyesight by introducing astigmatism (greek: point-less)

More information:

* [What are cylindrical lenses?](https://www.edmundoptics.com/resources/application-notes/optics/what-are-cylinder-lenses/)
* Comar Optics, 63 YE 25, cylindrical lens 63, coated


### Properties
* design is derived from the base-cube
* the adapter can hold a rectangular lens

## Parts
The [Bill of Materials](https://docs.google.com/spreadsheets/d/1U1MndGKRCs0LKE5W8VGreCv9DJbQVQv7O6kgLlB6ZmE/edit?usp=sharing) is always the most up-to-date version!

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

#### Default:
* **IM Cube** which houses the insert and adapts it into a UC2 setup.
* **The Lens Holder** which holds a rect. lens ([20_Cube_Insert_Lens_Cylindrical_v3.stl](../RAW/STL))

#### Alternatives:
* **3DP Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([10_Cube_1x1_v3.stl](../RAW/STL)) and **3DP Lid** which closes the Cube ([10_Lid_1x1_v3.stl](../RAW/STL)) - find the details in [ASSEMBLY_CUBE_Base](../ASSEMBLY_CUBE_Base)

### <img src="./IMAGES/B.png" height="40"> Additional parts
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
* Comar cylindrical lens, f' = 63 mm (63 YQ 40) [🢂](https://www.comaroptics.com/components/lenses/cylindrical-lenses/quality-planoconvex-cylindrical-lenses-visibleuv#row-63_yq_40)


## <img src="./IMAGES/A.png" height="40"> Assembly
* Put the lens inside the insert
* Add the insert to the Cube
* Close the cube accordingly (IM/3DP)
* Done!


### Tutorial with images (LENSHOLDER)
:grey_exclamation: This tutorial shows a UC2_v2 cube but the assembly of the insert is still the same. For assembly of the cube (IM/3DP) check the [ASSEMBLY_CUBE_Base](../ASSEMBLY_CUBE_Base).

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
