# Generic Lens Holder Cube
This is the repository for the Generic Lens Holder Cube.

The .stl files can be found in the folder [STL](./STL).

## Purpose
Spiral holder: It adapts any circular symmetric lens with varying diameter to the UC2 system.
<p align="center">
<img src="./IMAGES/Assembly_Cube_Objectiveholder.png" width="300">
</p>

Fixed holder: For the common lenses we also offer a more stable solution.
<p align="center">
<img src="./IMAGES/Assembly_Cube_Lens_Mount.png" width="400">
</p>

### Properties
* design is derived from the base-cube
* the adapter can hold a large variety of different lenses (different diameter/thickness)
* Spiral holder: the spiral automatically centers the lens to the optical axis
* Fixed holder: The lens is safely fixed in the holder without the risk of being disassembled by some curious user

## Parts

Note: [The holder we designed in openSCAD](./OPENSCAD) is a bit different and better than the one designed with [Inventor](./INVENTOR). The update of the STLs and Inventor files will be done in a near future ;)

### <img src="./IMAGES/P.png" height="40"> 3D printing parts
The Part consists of the following components.

* No support needed in all designs
* Carefully remove all support structures (if applicable)

#### Spiral holder
* **The Lid** where the Arduino + Electronics finds its place ([LID](./STL/10_Lid_1x1_v2.stl))
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/10_Cube_1x1_v2.stl))
* **The Objective/Lens Holder** which holds a lens with varying diameter and adapts it to the base cube ([HOLDER](./STL/20_Cube_Insert_Objective_Holder.stl))

#### Fixed holder
For a convex 1 inch lens:
* **The 1" Lens Holder** which holds a lens with 1 inch (25,4 mm) diameter and adapts it to the base cube ([HOLDER](./STL/1inch_Assembly_Insert_Lens_mount_fixed_20_Lens_holder.stl))
* **The 1" Lens Clamp** which holds a lens with 1 inch (25,4 mm) diameter in the holder ([CLAMP](./STL/1inch_Assembly_Insert_Lens_mount_fixed_20_Lens_holder_clamp.stl))

For a convex 25 mm lens:
* **The 25 mm Lens Holder** which holds a lens with 25 mm diameter and adapts it to the base cube ([HOLDER](./STL/25mm_Assembly_Insert_Lens_mount_fixed_20_Lens_holder.stl))
* **The 25 mm Lens Clamp** which holds a lens with 25 mm diameter in the holder ([CLAMP](./STL/25mm_Assembly_Insert_Lens_mount_fixed_20_Lens_holder_clamp.stl))

## Design your own Lens Holder  
For any lens or round filter from ⌀9 mm to ⌀42 mm  
* [INVENTOR TUTORIAL with images](./INVENTOR)  
* [OPENSCAD](./OPENSCAD)

### <img src="./IMAGES/B.png" height="40"> Additional parts
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
* 8× DIN912 M3×12 screws (galvanized steel) [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* alternatively: 4× M3×12 and 4× M3×8
* Microscope Objective lens (spiral holder) [🢂](https://de.aliexpress.com/item/4X-10X-20X-40X-60X-100X195-Augenmikroskops-System-Bio-Mikroskop-Biologische-Mikroskop-Lab-Labor-Achromatische-Objektiv/32947647522.html?spm=a2g0x.search0104.3.54.6cf57a4c3DwsTO&transAbTest=ae803_3&ws_ab_test=searchweb0_0%2Csearchweb201602_6_10065_10130_10068_10890_10547_319_10546_317_10548_10545_10696_10084_453_454_10083_10618_10307_537_536_10902_10059_10884_10887_321_322_10103%2Csearchweb201603_6%2CppcSwitch_0&algo_pvid=06d972be-b176-4446-8665-56d9e61a8d2c&algo_expid=06d972be-b176-4446-8665-56d9e61a8d2c-7)
* or any lens with corresponding diameter (fixed holder)

## <img src="./IMAGES/A.png" height="40"> Assembly of the Spiral Lens Holder
* Mount the lens inside the insert
* Put the Insert inside the Cube
* Add all screws to the Cube
* Done!

### Tutorial with images (Spiral Lens Holder)

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

## <img src="./IMAGES/A.png" height="40"> Assembly of Fixed Lens Holder
* Mount the lens inside the holder
* Put the clamp in, to hold the lens
* Put hot glue in the groove between the clamp and the holder - this way it will fix it permanently. The glue must never touch the lens!
* Put the Insert in the Cube
* Add all screws to the Cube
* Done!

### Tutorial with images (Fixed Lens Holder)

1. All parts for this model
<p align="center">
<img src="./IMAGES/Lens_Holder_01.jpg" width="300">
</p>

1. Put the lens inside the holder. When using plano-convex lenses, put the plano-surface in the holder with the convex surface in the direction where the clamp will be. That way, your lens will be completely sunken in the holder and therefore more protected from scratching.
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

## <img src="./IMAGES/Y.png" height="40">Safety
Don't touch the optical surfaces - fingerprints and scratches are bad for lenses!

Be careful not to burn yourself with the hot glue gun!
