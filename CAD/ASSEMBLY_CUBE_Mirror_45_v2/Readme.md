# Mirror Holder Cube
This is the repository for the Adjustable Mirror Holder Cube.

The stl-files can be found in the folder [STL](./STL).

### Purpose
It adapts a 30×30 mm ² fold-mirror to the UC2 system. Alternatively, we also have a design for a 1-inch mirror holder.
Old Image:
<p align="center">
<img src="./IMAGES/Assembly_Cube_Mirror_Tilt.png" width="300">
</p>


Due to limited space, we need to fold the beam using a mirror. This is done by reflecting the incoming light under an angle of 45°. It follows in a change of the optical axis by 90°


## Properties
* design is derived from the base-cube
* the adapter holds a 30×30 mm ² toy-mirror or a 1 inch circular mirror (e.g. Thorlabs part) at 45 degrees in a UC2 base cube
* the here used mirror has the following parameters:
	* Diameter: 25,4mm
	* Reflectance
	* Surface Flatness: (Peak to Valley) λ/10 @ 633 nm
	* Substrate Fused: Silica
	* Thickness: 6.0 mm (0.24")

## Parts

### <img src="./IMAGES/P.png" height="40"> 3D printing parts
The Part consists of the following components.

* **The Lid** where the Arduino + Electronics finds its place ([LID](./STL/10_Lid_1x1_v2.stl))
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/10_Cube_1x1_v2.stl))
* **The Mirror Insert** which holds a 1-inch Mirror from Thorlabs ([INSERT](./STL/20_Cube_Insert_Mirror_Holder_30x30Mirror_v2.stl)) or a 30x30mm Mirror from Amazon ([INSERT](./STL/20_Cube_Insert_Mirror_Holder_v2.stl)) and adapts it to the base cube

### <img src="./IMAGES/B.png" height="40"> Additional parts
* 8x DIN912 M3*12 screws (non stainless steel)
* 1x Thorlabs PF10-03-P01 - Protected Silver Mirror or
* 1x 30x30 Mirror from Amazon  

## Remarks and Tips
### 3D Printing:
* No support required in all designs
* Carefully remove all support structures (if applicable)

## <img src="./IMAGES/A.png" height="40"> Assembly
* Add the mirror to the Insert
* Add the insert to the Cube
* Add the screws to the Cube
* Done!

## Assembly Video Tutorial
[![UC2 YouSeeToo - How to assemble the Mirror Cube?](./IMAGES/UC2-Assembly_Cube_Mirror_45.png)](https://www.youtube.com/watch?v=IG7ws6ZtL6E)


### Tutorial with images (30×30 mm² mirror)

1. All parts for this model
<p align="center">
<img src="./IMAGES/CUBE_MIRRORMOUNT_45_0.jpg" width="300">
</p>

2. Stick the mirror to the insert.
<p align="center">
<img src="./IMAGES/CUBE_MIRRORMOUNT_45_1.jpg" width="300">
</p>

3. Put the insert inside the cube and close the lid using the screws.
<p align="center">
<img src="./IMAGES/CUBE_MIRRORMOUNT_45_2.jpg" width="300">
</p>

4. Add screws to the other side of the cube - Done!

## Safety
Don't touch the silver surface!

Never (!) look into the laser pointer! It will damage your eye immediately!

* ATTENTION: NEVER WATCH DIRECTLY INTO THE LASER! EYE WILL BE DAMAGED DIRECTLY
* NEVER SWITCH ON THE LASER WITHOUT INTENDED USE
* BEAM HAS TO GO AWAY FROM ONESELF - ALWAYS!
