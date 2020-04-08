# Mechanical Z-Stage (Objective) Cube
This is the repository for the mechanical Z-Stage (Objective) Cube.

The stl-files can be found in the folder [STL](./STL).

## Purpose
In microscopy one often needs the ability to move the objective along the optical axis in order to refocus a given 3D sample.This is a mechanical-only version of our [Z-stage](../ASSEMBLY_CUBE_Z-STAGE_v2). It allows for course and fine focussing by hand.

<p align="center">
<img src="./IMAGES/Assembly_Z-Focus_Linearbearing_mechanical_v0.png" width="300">
</p>

**The mechanism is the following:**

**Course movement:** The objective is mounted on a ring which has a screw on one side and the screw head is inserted in a slot in the focussing insert. The movement range for this is 35 mm - the full length of th slot.
<p align="center">
<img src="./IMAGES/Z-stage_principle_01.jpg" width="300">
<img src="./IMAGES/Z-stage_principle_02.jpg" width="300">
<img src="./IMAGES/Z-stage_principle_03.jpg" width="300">
</p>

**Fine movement:** For fine focussing the linearbearing lever is moved by (in this case) a mechanical gear. When the screw pushes or pulls the lever, due to a rotation of the gear, the objective mount moves with it.
<p align="center">
<img src="./IMAGES/Z-stage_principle_04.jpg" width="300">
<img src="./IMAGES/Z-stage_principle_05.jpg" width="300">
<img src="./IMAGES/Z-stage_principle_06.jpg" width="300">
</p>

### Properties
* theoretically no play due to the use of flexure berings
* moving range
	* fine: around +/- 6mm (when using 30 mm long screw for the gear mechanism)
	* coarse: around 30 mm (shifting the objective mount inside the slot)
* very low cost by relying on off-the-shelf components

## Parts

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

* **The Lid (2x1)** which closes the Cube ([LID](./STL/Assembly_Z-Focus_Linearbearing_mechanical_v0_10_Lid_el_2x1_v2_6.stl))
* **The Cube (2x1)** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/Assembly_Z-Focus_Linearbearing_mechanical_v0_10_Cube_2x1_v2_5.stl))
* **The Z-Stage Focussing Insert** which moves the objective agains a fixed plate ([INSERT](./STL/Assembly_Z-Focus_Linearbearing_mechanical_v0_20_focus_inlet_linearflexure_v0_1.stl))
* **The Bottom Plate** which prevents the gear from moving up and down ([BOTTOM PLATE](./STL/Assembly_Z-Focus_Linearbearing_mechanical_v0_20_focus_inlet_plate_bottom_2.stl))
* **The Top Plate** which prevents the gear from moving up and down ([TOP PLATE](./STL/Assembly_Z-Focus_Linearbearing_mechanical_v0_20_focus_inlet_plate_top_3.stl))
* **The Gear** which, when rotated, pushes the lever arm via the screw and hence moves the objective up and down  ([GEAR](./STL/Assembly_Z-Focus_Linearbearing_mechanical_v0_00_large_gear_4.stl))
* **The Objective Lens Mount** which holds the objective lens (RMS thread) ([OBJECTIVE MOUNT](./STL/Assembly_Z-Focus_Linearbearing_mechanical_v0_30_focus_inlet_objective_mount_v7_7.stl))
* **The Sample Plate** which provides the optimal spacing between the objective lens and the sample ([SAMPLE PLATE](./STL/Assembly_Z-Focus_Linearbearing_mechanical_v0_30_Z_Stage_Sampleplate_8.stl))

### <img src="./IMAGES/B.png" height="40"> Additional parts
* 10× - 20× DIN912 M3×12 screws (galvanized steel) [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* 2× DIN912 M3×8 screws (galvanized steel)
* 2× DIN912 M3×18 screws (galvanized steel)
* 1× M3 Nut
* 1× M3 Screw, 30 mm or longer (non-magnetic)
* 1× Microscope Objective, RMS thread [🢂](https://de.aliexpress.com/item/4X-10X-20X-40X-60X-100X195-Augenmikroskops-System-Bio-Mikroskop-Biologische-Mikroskop-Lab-Labor-Achromatische-Objektiv/32947647522.html?spm=a2g0x.search0104.3.54.6cf57a4c3DwsTO&transAbTest=ae803_3&ws_ab_test=searchweb0_0%2Csearchweb201602_6_10065_10130_10068_10890_10547_319_10546_317_10548_10545_10696_10084_453_454_10083_10618_10307_537_536_10902_10059_10884_10887_321_322_10103%2Csearchweb201603_6%2CppcSwitch_0&algo_pvid=06d972be-b176-4446-8665-56d9e61a8d2c&algo_expid=06d972be-b176-4446-8665-56d9e61a8d2c-7)


## <img src="./IMAGES/A.png" height="40"> Assembly

### Tutorial with images (Z-Stage)
This is the assembly guide for the mechanical Z-Stage.

1. All parts for this model (some parts in this picture might not be according to the latest design but the assembly is the same)
<p align="center">
<img src="./IMAGES/Z-stage_mech_01.jpg" width="300">
</p>

1. Place the head of the M3×30 screw in the end of the lever of the linear bearing insert.  
<p align="center">
<img src="./IMAGES/Z-stage_mech_02.jpg" width="300">
</p>

1.  Place the bottom plate, which will house the gear, on the insert. The M3×30 screw goes through it.
<p align="center">
<img src="./IMAGES/Z-stage_mech_03.jpg" width="300">
</p>

1.  Insert the M3 nut in the gear.
<p align="center">
<img src="./IMAGES/Z-stage_mech_04.jpg" width="300">
</p>

1. Screw the gear with the nut on the M3×30 screw. The gear should lie on the bottom plate but it should not pull the lever up for now.
<p align="center">
<img src="./IMAGES/Z-stage_mech_05.jpg" width="300">
</p>

1. Place the top plate over the gear. The M3×30 screw goes through it.
<p align="center">
<img src="./IMAGES/Z-stage_mech_06.jpg" width="300">
</p>

1. Using two M3×12 screws, fix the top and bottom plate to the focussing insert. Now the gear can only rotate and it doesn't move up or down.
<p align="center">
<img src="./IMAGES/Z-stage_mech_07.jpg" width="300">
</p>

1. In order to pull and push the lever, the head of the M3×30 screw has to be fixed in it. Fix it using two M3×8 screws from both sides. Firstly insert one screw. Tighten is using a hex key through the hole in the side of the focussing insert.
<p align="center">
<img src="./IMAGES/Z-stage_mech_08.jpg" width="300">
</p>

1. Then add the screw from the opposite side. Tighten both screws equally. The M3×30 must not rotate.
<p align="center">
<img src="./IMAGES/Z-stage_mech_09.jpg" width="300">
</p>

1. Do not overtighten the screws, you might break the lever. This should be the result:
<p align="center">
<img src="./IMAGES/Z-stage_mech_10.jpg" width="300">
</p>

1. Insert a M3×8 screw in the objective mount as shown in the picture. Don't screw it all the way in but leave roughly 1 mm between the head of the screw and the flat side of the objective mount.
<p align="center">
<img src="./IMAGES/Z-stage_mech_11.jpg" width="300">
</p>

1. Insert the objective lens into its mount.
<p align="center">
<img src="./IMAGES/Z-stage_mech_12.jpg" width="300">
</p>

1. Insert the objective mount into the focussing insert. The head of the M3×8 screw goes into the slot in the insert. In case the screw is too tighten to the objective mount, it won't go into the slot - loosen the screw a little. In case the head of the screw is too far from the objective mount, it won't hold in the slot but fall through - tighten the screw a little.
<p align="center">
<img src="./IMAGES/Z-stage_mech_13.jpg" width="300">
</p>

1. The optimal case: the objective mount holds the objective in any position within the slot. You should be able to shift the objective but it shouldn't not move on its own. Adjust the screw of the objective mount if necessary.
<p align="center">
<img src="./IMAGES/Z-stage_mech_14.jpg" width="300">
</p>

1. Place the insert inside the cube. For optimal use, the lid of the cube should be sideways from the insert, as shown in the picture. Close the cube using four M3×12 screws.
<p align="center">
<img src="./IMAGES/Z-stage_mech_15.jpg" width="300">
</p>

1. Add the sample plate above the objective lens. It is designed to give proper spacing between the objective lens and the sample - therefore the stage is already pre-aligned when assembled. Use two M3×18 screw to fix in to the cube - positioned left in the following picture. On the right side of the plate, use two M3×12 screws.
<p align="center">
<img src="./IMAGES/Z-stage_mech_16.jpg" width="300">
</p>

1. Fix the sample plate. Add as many M3×8 screws as possible to both the lid and the bottom of the cube-body - Done!
<p align="center">
<img src="./IMAGES/Z-stage_mech_17.jpg" width="300">
</p>

## Safety
Be careful!
