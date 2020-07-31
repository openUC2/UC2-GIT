# Rectangular Aperture Cube
This is the repository for a rectangular aperture incorporated into the basic Cube.

The stl-files can be found in the folder [STL](./STL).

## Purpose
The aperture can limit the light beam in X and Y independently and asymmetrically from both sides.  

<p align="center">
<img src="./IMAGES/Assembly_Cube_Rect_Aperture_v2.png" width="300">
</p>

<p align="center">
<img src="./IMAGES/Assembly_Cube_Rect_Aperture_v2_01.png" height="250">
<img src="./IMAGES/Assembly_Cube_Rect_Aperture_v2_02.png" height="250">
</p>

### Properties
* the opening of the aperture goes from fully closed to approximately 20 mm
* The mechanism is still a little fragile and suggestions for improvements are warmly welcome!

## Design
The original design files are in the [INVENTOR](./INVENTOR) folder. These files were generated using Autodesk Inventor 2019 Student Version.

To start working on it, you have to do the following steps:
1. Download the `Assembly_Cube_Rect_Aperture_v2.zip` and unzip it
1. Open Inventor and import existing project
1. Select filename `Assembly_Cube_Rect_Aperture_v2.ipj`
1. Now you can modify the parts
1. If you have a cool improvement for this part, please let us know! ([CONTRIBUTING](../../CONTRIBUTING.MD))


## Parts

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

* **The Lid** which closes the Cube ([LID](./STL/10_Lid_1x1_v2.stl))
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/10_Cube_1x1_v2.stl))
* **The Aperture Insert** which holds the mechanism in place ([INSERT](./STL/20_Cube_Insert_RectAp_v2.stl))
* **The Aperture Door - sliding part** which is the part of the door that does most of the movement. You need four of them ([DOOR SLIDE](./STL/20_Rect_Aperture_door_slide.stl))
* **The Aperture Door - hinge part** which is the part of the door that supports the movement. You need four of them ([DOOR HINGE](./STL/20_Rect_Aperture_door_hinge.stl))

### <img src="./IMAGES/B.png" height="40"> Additional parts
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
* 8× DIN912 M3×12 screws (galvanized steel) [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)

## <img src="./IMAGES/A.png" height="40"> Assembly
* Assemble the aperture
* Add the insert to the Cube
* Add screws to the Cube
* Done!

### <img src="./IMAGES/A.png" height="40"> Assembly Tutorial with images
1. All parts for this model
<p align="center">
<img src="./IMAGES/RectAp_01.jpg" width="300">
</p>

1. There are in total four doors and the assembly is the same for all of them. Firstly, insert the DOOR-HINGE into the slit in the insert part. You should be able to move the hinge when it's done correctly. The slits might need some filing, especially on the bottom-printed side of the insert (depending on your 3D printer).
<p align="center">
<img src="./IMAGES/RectAp_02.jpg" width="300">
<img src="./IMAGES/RectAp_03.jpg" width="300">
</p>

1. Now comes the sliding part of the door. Insert the pins in the slit that will lead the sliding movement of this part.
<p align="center">
<img src="./IMAGES/RectAp_04.jpg" width="300">
<img src="./IMAGES/RectAp_05.jpg" width="300">
<img src="./IMAGES/RectAp_06.jpg" width="300">
</p>

1. Connect the two parts of the door. Be careful not to break the little 'wings' that hold the hinge mechanism. Insert fist one side and then press it into the other, as shown in the pictures.
<p align="center">
<img src="./IMAGES/RectAp_07.jpg" width="300">
<img src="./IMAGES/RectAp_08.jpg" width="300">
<img src="./IMAGES/RectAp_09.jpg" width="300">
</p>

1. Follow the same step for the other door on the same side and for the doors on the other side of the insert.
<p align="center">
<img src="./IMAGES/RectAp_10.jpg" width="300">
<img src="./IMAGES/RectAp_11.jpg" width="300">
</p>

1. Insert the insert into the Cube, add screws - Done!
<p align="center">
<img src="./IMAGES/RectAp_12.jpg" width="300">
<img src="./IMAGES/RectAp_13.jpg" width="300">
<img src="./IMAGES/RectAp_14.jpg" width="300">
</p>

1. Open/close the doors using a hex key or a thin screwdriver.
<p align="center">
<img src="./IMAGES/RectAp_14.jpg" width="300">
</p>
