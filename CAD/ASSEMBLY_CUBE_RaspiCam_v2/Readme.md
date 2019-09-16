# Camera Cube
This is the repository for the Camera Cube. 

The stl-files can be found in the folder [STL](./STL).



### Purpose
It adapts a standard Raspberry Pi Camera (v1, v2) to the UC2 system.
<p align="center">
<img src="./IMAGES/Assembly_Cube_cameracube.png.jpg" width="300">
</p>

![](./IMAGES/)

The sensor (w/wo lens) is put into an adapter which holds the camera in the center of the cube. The height can be varied by sliding the adapter along the slides. It is designed to eventually hold (flourescent) filters. The camera need to be fixed with a set of screws. M2x10mm in combination with nuts work best. 


## Properties
* design is derived from the base-cube
* camera adapter can be adjusted to individual needs
	
## Parts

### 3D printing parts 
The Part consists of the following components. 

* **The Lid** where the Arduino + Electronics finds its place 
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place 
* **The Camera Insert** which holds the camera and makes it adaptable to the base-cube

### Additional parts 
* 4x DIN912 M3*12 screws (non stainless steel)
* Raspi Camera (v1, v2) 
* 2x M2*10 screws (best: plastic)
* 2x M2 nuts (best: plastic) 

## Remarks and Tips 
### 3D Printing:
* No support required in all designs 

## Assembly
* Mount the flex cable to the raspi-cam
* Mount the camera board to the Camera-Inlet using the 2 M2 screws
* Fix the position by mounting the 2 nuts. Take care to not destroy the camera'S PCB 
* Take the mounted camera adapter inlet and slide it into the base-cube 
* Take the cube lid and mount it using the 4 hex screws
* Done! 

###Tutorial with images

1. All parts for this model
<p align="center">
<img src="./IMAGES/CUBE_RASPICAM0.jpg" width="300">
</p>

2. Remove the Lens of the raspberry pi camera using the tool which comes with it. Optional: Add a longer camera cable to it.
<p align="center">
<img src="./IMAGES/CUBE_RASPICAM1.jpg" width="300">
</p>

3. Add the camera to the insert using some M2 crews + nuts. Be careful and try not to destroy the camera! It's fragile.
<p align="center">
<img src="./IMAGES/CUBE_RASPICAM2.jpg" width="300">
</p>

4. Add the screws - Done!
<p align="center">
<img src="./IMAGES/CUBE_RASPICAM3.jpg" width="300">
</p>

## Safety
Be carefule with the camera's PCB. It's sensible to electronic static discharge! 