# Camera Cube
This is the repository for the Camera Cube.

The stl-files can be found in the folder [STL](./STL).

## Purpose
It adapts a Basler Camera  to the UC2 system.

<p align="center">
<img src="./IMAGES/Assembly_Cube_BaslerCam_acA1920_25gm_v2.png" width="600">
</p>

The sensor is put into an adapter which holds the camera in the center of the cube. The height can be varied by sliding the adapter along the slides.

### Properties
* design is derived from the base-cube
* camera adapter can be adjusted to individual needs

## Parts

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

* **The Lid** where the Arduino + Electronics finds its place ([LID](./STL/10_Lid_1x1_v2.stl))
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/10_Cube_1x1_v2.stl))
* **The Camera Insert** which holds the camera and makes it adaptable to the base-cube ([INSERTE](./STL/20_Cube_insert_Basler_acA1920_25gm.stl))

### <img src="./IMAGES/B.png" height="40"> Additional parts
* 7× DIN912 M3×12 screws (galvanized steel) [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* Basler Camera: a AC 1920_25ag


## <img src="./IMAGES/A.png" height="40"> Assembly
* Mount the camera to the insert using 3x M3 screws
* Take the mounted camera adapter inlet and slide it into the base-cube
* Take the cube lid and mount it using the 4 hex screws
* Done!
