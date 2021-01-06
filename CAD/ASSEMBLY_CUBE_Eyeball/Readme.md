# Eyeball Cube
This is the repository for the Eyeball Cube.

To acquire the STL-files use the [UC2-Configurator](). The files themselves are in the [RAW](../RAW/STL) folder. The module can be built using injection-moulded (IM) or 3D-printed (3DP) cubes.

### Purpose
It can serve as an aid for demonstrations and experiments done with the [SimpleBOX](../../TheBOX/SimpleBOX) or [CourseBOX](../../TheBOX/CourseBOX).

<p align="center">
<img src="./IMAGES/Assembly_Cube_Eyeball_v2_01.png" width="300">
</p>

The lens holder holds a lens in a fixed distance from the back of the "eye". This distance equals the focal length of this lens. Therefore this simplified "eye" just focusses any image from infinity on the back side. It works best when printed using white material.
<p align="center">
<img src="./IMAGES/Assembly_Cube_Eyeball_v2_02.png" width="300">
</p>

You can nicely see the magnification effect of a telescope when you "look" out of the window using the Eyeball cube alone and then placing in [behind a telescope](../../APPLICATIONS/APP_SIMPLE-Telescope).

<p align="center">
<img src="./IMAGES/Assembly_Cube_Eyeball_v2_03.jpg" width="300">
</p>

## Properties
* design is derived from the base-cube
* in principle, any short *f'* can be used, if the distance is adjusted for it

## Parts
The [Bill of Materials](https://docs.google.com/spreadsheets/d/1U1MndGKRCs0LKE5W8VGreCv9DJbQVQv7O6kgLlB6ZmE/edit?usp=sharing) is always the most up-to-date version!

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

#### Default:
* **IM Cube** which houses the insert and adapts it into a UC2 setup.
* **The Eye Insert** which serves as the back of the eye - it works bes when printed using white material ([INSERT EYE](./STL/Assembly_Cube_Eyeball_v2_20_Cube_Insert_Eye_1.stl))
* **The Lens Insert** which holds the lens ([INSERT LENS](./STL/Assembly_Cube_Eyeball_v2_20_Cube_Insert_Eye_Lens_2.stl)) and adapts it to the base cube

#### Alternatives:
* **3DP Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([10_Cube_1x1_v3.stl](../RAW/STL)) and **3DP Lid** which closes the Cube ([10_Lid_1x1_v3.stl](../RAW/STL)) - find the details in [ASSEMBLY_CUBE_Base](../ASSEMBLY_CUBE_Base)

### <img src="./IMAGES/B.png" height="40"> Additional parts
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
* 1× Lens, *f' = 25 mm**

## <img src="./IMAGES/A.png" height="40"> Assembly
* Add the lens to the Lens Insert
* Glue the Lens insert to the back of the eye
* Place the inserts inside the Cube
* Close the cube accordingly (IM/3DP)
* Done!
