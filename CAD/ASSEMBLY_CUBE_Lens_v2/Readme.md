# Generic Lens Holder Cube
This is the repository for the Generic Lensholder Cube.

The stl-files can be found in the folder [STL](./STL).

### Purpose
It adapts any circular symmetric lens with varying diameter to the UC2 system.
<p align="center">
<img src="./IMAGES/Assembly_Cube_Objectiveholder.png" width="700">
</p>

For the common lenses we also offer a more stable solution.
<p align="center">
<img src="./IMAGES/Assembly_Cube_Lens_Mount.png" width="400">
</p>


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
* **The Objective/Lens Holder** which holds a lens with varying diamater and adapts it to the base cube ([HOLDER](./STL/20_Cube_Insert_Objective_Holder.stl))

For a convex 1 inch lens:
* **The 1" Lens Holder** which holds a lens with 1 inch (25,4 mm) diamater and adapts it to the base cube ([HOLDER](./STL/1inch_Assembly_Insert_Lens_mount_fixed_20_Lens_holder.stl))
* **The 1" Lens Clamp** which holds a lens with 1 inch (25,4 mm) diamater in the holder ([CLAMP](./STL/1inch_Assembly_Insert_Lens_mount_fixed_20_Lens_holder_clamp.stl))

For a convex 25 mm lens:
* **The 25 mm Lens Holder** which holds a lens with 25 mm diamater and adapts it to the base cube ([HOLDER](./STL/25mm_Assembly_Insert_Lens_mount_fixed_20_Lens_holder.stl))
* **The 25 mm Lens Clamp** which holds a lens with 25 mm diamater in the holder ([CLAMP](./STL/25mm_Assembly_Insert_Lens_mount_fixed_20_Lens_holder_clamp.stl))

For any lens you have at hand:
* Download the [Lens Insert Folder](./STL/Lens_Insert), adapt the .ipt files to the dimensions of your lens, export .stl and print your own holders.
* The clamp is adaptive to the holder - it is enough to change a single parameter - the diameter of your lens.
* Open the file called "Assembly_Insert_Lens_mount_fixed.iam" → 20_Lens_holder.ipt → Manage → Parameters → Lens_Diameter → Done → Return → Update → Save Copy As → .stl → Options → One Part per File
* For a thick (often the case of concave lenses) increase the thickness of the holder (hint: thickness of your lens at the edge + 2-3 mm)

### <img src="./IMAGES/B.png" height="40"> Additional parts
* 8x DIN912 M3*12 screws (non stainless steel)
* Microscopic Objective lens, 4x, 0.1NA, RMS-Thread, Finite corrected or any lens < 35mm Diameter


## Remarks and Tips
### 3D Printing:
* No support required in all designs
* Carefully remove all support structures (if applicable)

## <img src="./IMAGES/A.png" height="40"> Assembly of the Generic Lens Holder
* Mount the lens inside the insert
* Put the Insert inside the Cube
* Add all screws to the Cube
* Done!

### Tutorial with images (Generic Lens Holder)

1. All parts for this model
<p align="center">
<img src="./IMAGES/CUBE_LENSHOLDER_0.jpg" width="300">
</p>

1. Put the lens inside the Spiral lens adapter (it auto centers)
<p align="center">
<img src="./IMAGES/CUBE_LENSHOLDER_1.jpg" width="300">
</p>

1. Insert the insert into the Cube, add screws - Done!
<p align="center">
<img src="./IMAGES/CUBE_LENSHOLDER_2.jpg" width="300">
</p>

## <img src="./IMAGES/A.png" height="40"> Assembly of Size-fitting Lens Holder
* Mount the lens inside the holder
* Put the clamp in, to hold the lens
* Put hot glue in the groove between the clamp and the holder - this way it will fix it permanently. The glue must never touch the lens!
* Put the Insert in the Cube
* Add all screws to the Cube
* Done!

### Tutorial with images (Size-fitting Lens Holder)

1. All parts for this model
<p align="center">
<img src="./IMAGES/Lens_Holder_01.jpg" width="300">
</p>

1. Put the lens inside the holder. When using plano-convex lenses, put the plano-surface in the holder with the convex surface in the direction where the clamp will be. That way, your lens will be completely sunken in the holder and therefore more protected from scatching.
<p align="center">
<img src="./IMAGES/Lens_Holder_02.jpg" width="300">
</p>

1. Put hot glue on the clamp as shown in the pictures. Do not use too much glue - you don't want to glue the clamp to the surface of the lens!
<p align="center">
<img src="./IMAGES/Lens_Holder_03.jpg" width="300">
<img src="./IMAGES/Lens_Holder_04.jpg" width="300">
</p>

1. Press the clamp in the holder. The glue will fill the groove between the holder and the clamp's "flowery" rim. Be careful not to put any glue on the surface of the lens!
<p align="center">
<img src="./IMAGES/Lens_Holder_05.jpg" width="300">
<img src="./IMAGES/Lens_Holder_06.jpg" width="300">
<img src="./IMAGES/Lens_Holder_07.jpg" width="300">
</p>

1. Insert the insert into the Cube, add screws - Done!
<p align="center">
<img src="./IMAGES/Lens_Holder_08.jpg" width="300">
<img src="./IMAGES/Lens_Holder_09.jpg" width="300">
<img src="./IMAGES/Lens_Holder_10.jpg" width="300">
</p>

## Safety
Never (!) look into the laser pointer! It will damage your eye immediately!

* ATTENTION: NEVER LOOK DIRECTLY INTO THE LASER! EYE WILL BE DAMAGED DIRECTLY
* NEVER SWITCH ON THE LASER WITHOUT INTEDED USE
* BEAM HAS TO GO AWAY FROM ONESELF - ALWAYS!
