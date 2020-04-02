# Camera Cube (Allied Vision Alvium)
This is the repository for the Camera Cube which hosts an embedded vision camera from Allied Vision (Alvium).

The stl-files can be found in the folder [STL](./STL).



### Purpose
It adapts an Allied Vision Camera to the UC2 system.

<p align="center">
<img src="./IMAGES/Assembly_Cube_AlliedVision_Alvium_v2.png" width="300">
</p>

The sensor is put into an adapter which holds the camera in the center of the cube. The height can be varied by sliding the adapter along the slides.

## Properties
* design is derived from the base-cube
* camera adapter can be adjusted to individual needs

## Parts

### <img src="./IMAGES/P.png" height="40"> 3D printing parts
The Part consists of the following components.

* **The Lid** where the Arduino + Electronics finds its place ([LID](./STL/10_Lid_1x1_v2.stl))
* **The Cube** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/10_Cube_1x1_v2.stl))
* **The Camera Insert** which holds the camera and makes it adaptable to the base-cube ([INSERT](./STL/20_Cube_insert_AlliedVision_Alvium.stl))

### <img src="./IMAGES/B.png" height="40"> Additional parts
* 7x DIN912 M3*12 screws (non stainless steel)
* Allied Vision Camera: CSI ALVIUM 1800 C-158


## Remarks and Tips

### Making it work

We use the following configuration:

- Nvidia Jetson Nano (100€)
- CSI ALVIUM 1800 C-158 (250€)
- Adapter Board CSI-2 (30€)
- Adapter Cable CSI-2 420 mm (10€)
- USB 5V charger (5€)
- USB Micro cable for the Adapter-Board supply voltage (!)
- SD Card, 64 GB (15€)

#### Assembly
Put all the components together as this here

<p align="center">
<img src="./IMAGES/IMG_20200220_193838.jpg" width="600">
</p>

#### Jetson Nano Preparation

1.) Prepare the SD card following this link: [https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) (use Etcher and format the SD card before installing firmware!)

2.) Install all necessary packages + PYthon following this link [https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html)
(Tensorflow/Keras, etc. is not required yet)

3.) Install the Video4Linux2 (V4L2) support for python
[https://pypi.org/project/pyv4l2/](https://pypi.org/project/pyv4l2/)
```sudo apt-get install qv4l2```
```sudo apt-get install libv4l-dev```
and
```pip3 install pyv4l2```


4.) A package to detect the camera is this here:
```sudo apt-get install v4l-utils```
find the camera (```/dev/video0```) by typing:
```v4l2-ctl --list-devices​```

it may give you something like this:

```
vi-output, avt_csi2 6-003c (platform:54080000.vi:0):
        /dev/video0
```

5.) Install some further python packages:
[v4l2capture](https://pypi.org/project/v4l2capture/)
[pyv4l2](https://pypi.org/project/pyv4l2/)

6.) Test Allied Vision Examples:

```
cd ~Downloads

git clone https://github.com/alliedvision/examples

cd GStreamer

sudo ./gstreamer_install.sh

./gstreamer_live.sh -b nvidia -d /dev/video0
```

you should now see a live-stream of the camera. Eventually reboot before this step.



### Things to do
- Control camera acquisition parameters through python/opencv (i.e. gain, exposure time) for still-image acquisition
	- V4L2 allows Register Access, so we should be able to do that?
- We would like to use the ```cv2.CaptureVideo``` method to load frames from the camera insid the MAT container. How could we do that?

### 3D Printing:
* No support required in all designs

## <img src="./IMAGES/A.png" height="40"> Assembly
* Mount the camera to the insert using 3x M3 screws
* Take the mounted camera adapter inlet and slide it into the base-cube
* Take the cube lid and mount it using the 4 hex screws
* Done!

Once it's done it looks like this:

<p align="center">
<img src="./IMAGES/IMG_20200220_193843.jpg" width="600">
</p>
