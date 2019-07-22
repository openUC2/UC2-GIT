## In-Incubator Microscope
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

## 3D Printing Files
Please have a look at the folder [STL](./STL). All files need to be printed.

* 1x [Base-Plate](./STL/Assembly_UKJ_Microscope_Assembly_base_4x2.stl)
* 3x [1x1 Cube Lid](./STL/Assembly_UKJ_Microscope_v4_10_Lid_el_v0.stl)
* 1x [Z-Stage](./STL/Assembly_UKJ_Microscope_v4_00_focus_inlet_triangle_spiral_v6.stl)
* 1x [Motor Coupler](./STL/Assembly_UKJ_Microscope_v4_01_28BYJ_Coupling_ScrewM4.stl)
* 1x [Base-Plate](./STL/Assembly_UKJ_Microscope_v4_10_Cube_2x_v0_no-rods.stl)
* 1x [Cube LED Matrix Adapter](./STL/Assembly_UKJ_Microscope_v4_10_Cube_LED_Array.stl)
* 1x [Cube Raspicam Adapter](./STL/Assembly_UKJ_Microscope_v4_11_Mirror_Adapter_for_RaspiCam.stl)
* 1x [Cube Raspicam Adapter](./STL/Assembly_UKJ_Microscope_v4_11_Mirror_Adapter_for_RaspiCam.stl)
* 1x [Cube](./STL/Assembly_UKJ_Microscope_v4_10_Cube_v0.stl)
* 1x [Magnetic Sample adapter](./STL/Assembly_UKJ_Microscope_v4_40_XY_Stage_Chipclamp.stl)
* 1x [1x1 Cube](./STL/Assembly_UKJ_Microscope_v4_10_Cube_v0_21.stl)
* 1x [Z-STage Adapter Plate](./STL/Assembly_UKJ_Microscope_v4_40_Z_Stage_Adapterplate.stl)
* 1x [2x1 Cube Lid ](./STL/Assembly_UKJ_Microscope_v4_10_Lid_el_2x_v0.stl)




## Devices features:

	* X/Y/Z/t Acquisitions possible
	* Fluorescent imaging 
	* Quantitative Phase Imaging
	* modularized design
	* Low-cost acquisition
	* based on off-the-shelf components (please see the bill of materials in the (./../DOCUMENTS) DOCUMENTS folder)
	* Open-Source