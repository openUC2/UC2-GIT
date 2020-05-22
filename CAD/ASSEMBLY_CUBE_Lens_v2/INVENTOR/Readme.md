# Design your own Lens Holder  
## For any lens or round filter from ⌀9 mm to ⌀42 mm
Note: [The holder we designed in openSCAD](../OPENSCAD) is a bit different from THIS ONE - and better. The update of the STLs and Inventor files will be done in a near future ;)

### Shortly, for any lens you have at hand:
* Download the [Lens Insert Folder](./Lens_Insert), adapt the .ipt files to the dimensions of your lens, export .stl and print your own holders.
* The clamp is adaptive to the holder - it is enough to change a single parameter - the diameter of your lens.
* Open the file called "Assembly_Insert_Lens_mount_fixed.iam" → 20_Lens_holder.ipt → Manage → Parameters → Lens_Diameter → Done → Return → Update → Save Copy As → .stl → Options → One Part per File
* For a thick (often the case of concave lenses) increase the thickness of the holder (hint: thickness of your lens at the edge + 2-3 mm)

### Tutorial with images

1. Open the file called _Assembly_Insert_Lens_mount_fixed.iam_ from [_/Lens_Insert_](./Lens_Insert)

<p align="center">
<img src="../IMAGES/design_lens_holder_01.png" width="500">
</p>

2. Double-click the _20_Lens_holder.ipt_ in the Model bar on the right to enter the editing of the part

<p align="center">
<img src="../IMAGES/design_lens_holder_02.png" width="500">
<img src="../IMAGES/design_lens_holder_03.png" width="500">
</p>

3. In the top pannel choose _Manage_ and then _Parameters_. The Parameters window opens as shown in the picture

<p align="center">
<img src="../IMAGES/design_lens_holder_04.png" width="500">
</p>

4. In _User Parameters_ change the value of _Lens_diameter_ to the diameter of your lens, then close the _Parameters_ window by clicking on _Done_

<p align="center">
<img src="../IMAGES/design_lens_holder_05.png" width="500">
</p>

5. For a lens thicker than ~3 mm you need to adapt the thickness of the holder as well. In the _Parameters_ window in _Model Parameters_ there is a _thickness_ dimension in mm consumed by _Thickness_.


* The default thickness of our insert is 5 mm, which works for lenses with edge thickness < 3 mm
* For each milimeter above 3 mm of the edge thickness of your lens, add one milimeter to _thickness_  
* Example: Dublet Lens with edge thickness 5 mm -  _thickness_  = 7 mm
* Example: Biconcave Lens with edge thickness 7 mm -  _thickness_ = 9 mm


<p align="center">
<img src="../IMAGES/design_lens_holder_15.png" width="500">
</p>

6. In the top pannel bar choose _Return_ to exit the part editing. The dimensions update automatically. If not, click on _Update_ in the top pannel

<p align="center">
<img src="../IMAGES/design_lens_holder_06.png" width="500">
<img src="../IMAGES/design_lens_holder_07.png" width="500">
</p>

7. From the top pannel choose _File_, _Export_ and then _CAD format_

<p align="center">
<img src="../IMAGES/design_lens_holder_08.png" width="500">
</p>

8. In the _Save As_ window choose data type _STL_ and then click on _Options..._

<p align="center">
<img src="../IMAGES/design_lens_holder_09.png" width="500">
</p>

9. In the _STL File Save As Options_ under _Structure_ choose _One File per Part Instance_

<p align="center">
<img src="../IMAGES/design_lens_holder_10.png" width="500">
</p>

10. You might find it useful to add the diameter to the name of the file before you _Save_ it, especially if you're going to print many different holders

<p align="center">
<img src="../IMAGES/design_lens_holder_11.png" width="500">
</p>

11. Both the Lens holder and clamp are saved by the assembly name and part name by default

<p align="center">
<img src="../IMAGES/design_lens_holder_12.png" width="500">
</p>

12. Place both _.stl_ files in the 3D printer slicer. The clamp is usually exported in a bad orientation for printing. Rotate the clamp if necessary - always print it with the "flowery" rim lying on the build plate. Slice it, print it, use it ;)

<p align="center">
<img src="../IMAGES/design_lens_holder_13.png" width="500">
<img src="../IMAGES/design_lens_holder_14.png" width="500">
</p>
