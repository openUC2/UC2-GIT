## Inline Holographic Microscope
This is the repository for the inline hographical microscope. This will be part of the workshop which can be found in WORKSHOP.

It acquires the interference of the spherial wave coming from a pinhole, illuminated by an LED, and the scattered wave from a transparent (phase) sample. 

<p align="center">
<img src="./IMAGES/INLINE_HOLOGRAM.png" width="500">
</p>


For reconstructing the Hologram, acquired on-chip (Raspi-Cam, left) one only needs to "deconvolve" it with the free propagator at a certain z-distance (i.e. fresnel propagator). 

A more in-detail documentation can be found [here](./../../WORKSHOP/INLINE-HOLOGRAMM)

## 3D printing

<p align="center">
<img src="./IMAGES/Print_CURA_Capture.PNG" width="500">
</p>

Parts to printing 

* 1x [Base-plate](./STL/INLINE_HOLOGRAM_00_Base_4x1_v0.stl)
* 2x [Cube base](./STL/INLINE_HOLOGRAM_10_Cube_v0.stl)
* 2x [Cube lid](./STL/INLINE_HOLOGRAM_10_Lid_el_v0.stl)
* 1x [Cube Insert Camera](./STL/INLINE_HOLOGRAM_11_Mirror_Adapter_for_RaspiCam.stl)
* 1x [Cube Insert for the LED+Aluminium foil](./STL/INLINE_HOLOGRAM_10_Inlet_LED_Reflector)



## Additional components
* 1x Raspberry Pi
* 1x Raspberry Pi Camera v2 NoIR
* 8x 5mm Ball magnets
* 8x DIN 906 M3x18mm Screws 
* 1x wired LED (blue) 
* 1x button
* 1x Power Supply for Raspberry Pi

## Devices features:

	* Lensless
	* Explain Interference
	* Low-cost acquisition
	* Open-Source
	* Compatible with Educational purposes