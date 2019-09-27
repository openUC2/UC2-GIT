## In-Incubator Microscope with fuorescence module
This is the repository for the in-incubator microscope. It is capable to acquire Time-Lapse videos from living cells inside an incubator.

The current version of the Z-stage is inspired by the flexure-bearing Z-stage from Richard Bowman's openflexure microscope design. Their open-source project can be found [here](https://openflexure.org).


<p align="center">
<img src="./IMAGES/Assembly_UKJ_Microscope_v4.png" width="500">
</p>


Each functional block has an Arduino acting as a BUS-communicator. Therefore it's possible to control (i.e. swith on/off) devices from the MASTER-device (i.e. Raspberry pi). We aim to build a low-cost solution for high throughput acquisitions, acting as a new tools for (not only) biologists.

It is a very early developer version. Please feel free to contribute to the documentation and device development.

<p align="center">
<img src="./IMAGES/Assembly_UKJ_Microscope_v4_2.png" width="500">
</p>

Fluorescence version:
<p align="center">
<img src="./IMAGES/UC2_Setups_4_fluorescence.png" width="400">
</p>

## 3D Printing Files
Please have a look at the folder [STL](./STL). All files need to be printed.

* 1× [Base-Plate 4×2](./STL/Assembly_base_4x2.stl)
* 4× [1×1 Cube](./STL/10_Cube_1x1_v2.stl)
* 4× [1×1 Cube Lid](./STL/10_Lid_1x1_v2.stl)
* 1× [2×1 Cube](./STL/10_Cube_2x1_v2.stl)
* 1× [2×1 Cube Lid](./STL/10_Lid_el_2x1_v2.stl)
* 1× [Z-Stage](./STL/20_focus_inlet_triangle_spiral_v6.stl)
* 1× [Coupling Screw M4](./STL/30_Coupling_Screw_28BYJ_M4.stl)
* 1× [Z-Stage Fluomodule](./STL/30_Z_Stage_Fluomodule_12.stl)
* 1× [Z-Stage Adapterplate](./STL/30_Z_Stage_Adapterplate_11.stl)
* 1× [Z-Stage Microscope Slide Clamp](./STL/40_XY_Stage_Clamp_Slide_9.stl)
* 1× [Cube LED Star Holder](./STL/ASSEMBLY_CUBE_LED_20_Cube_insert_LED_holder.stl)
* 1× [Cube Dichroic Beamsplitter](./STL/20_Cube_Insert_Beamsplittercube_Base.stl)
* 1× [Cube Dichroic Filter Retain plate](./STL/20_Cube_Insert_Beamsplittercube_Dichroicmirror_Retainplate.stl)
* 1× [Cube Filter Retain ring](./STL/20_Cube_Insert_Beamsplittercube_Retainring_25mm.stl)
* 1× [Cube Raspicam Insert](./STL/20_Cube_Insert_RaspiCam.stl)
* 1× [Thorlabs Mirror Insert](./STL/20_Cube_Insert_Mirror_Holder_v2.stl) or [30×30 Mirror Insert](./STL/20_Cube_Insert_Mirror_Holder_30x30Mirror_v2.stl)

## Devices features:

* X/Y/Z/t Acquisitions possible
* Fluorescent imaging
* Quantitative Phase Imaging
* modularized design
* Low-cost acquisition
* based on off-the-shelf components (please see the bill of materials in the (./../DOCUMENTS) DOCUMENTS folder)
* Open-Source
