# Inline Holographic Microscope
This is the repository for the inline holographical microscope.

This is be part of the workshop which can be found in WORKSHOP. Note that the designs has been updated since the last workshop was organized. The files and linked on this page are up to date. The files in the workshop document follow the old version of the cube.

It acquires the interference of the spherical wave coming from a pinhole, illuminated by an LED, and the scattered wave from a transparent (phase) sample.

<p align="center">
<img src="./IMAGES/Application_Inline_Holographic_Microscopy_v3.png" width="700">
</p>


For reconstructing the Hologram, acquired on-chip (Raspi-Cam, left) one only needs to "deconvolve" it with the free propagator at a certain z-distance (i.e. Fresnel propagator).

A more in-detail documentation can be found [here](../../WORKSHOP/INLINE-HOLOGRAMM)

## <img src="./IMAGES/F.png" width="40">Devices' features:

* Lensless
* Explain Interference
* Low-cost acquisition
* Open-Source
* Compatible with Educational purposes


## <img src="./IMAGES/D.png width="40">Parts
The [Bill of Materials](https://docs.google.com/spreadsheets/d/1U1MndGKRCs0LKE5W8VGreCv9DJbQVQv7O6kgLlB6ZmE/edit?usp=sharing) is always the most up-to-date version!

### Modules for this setup

|  Name | Properties  |  Price | Link  | # |
|---|---|---|---|---|
|  Baseplate puzzle| - | 5€  | [Base-plate](../../CAD/ASSEMBLY_Baseplate/)  | 4|
|  Module: Raspberry Pi Camera | -  | 20 €  | [Raspi Camera Cube](../../CAD/ASSEMBLY_CUBE_RaspiCam)  | 1|
|  Module: LED + Pinhole  | - | 10€  | [LED + Pinhole](../../CAD/ASSEMBLY_CUBE_LED)  | 1|

### <img src="./IMAGES/P.png" width="40"> 3D-printing
To acquire the STL-files use the [UC2-Configurator](https://uc2configurator.netlify.app/). The files themselves are in the [RAW](../../RAW/STL) folder. The module can be built using injection-moulded (IM) or 3D-printed (3DP) cubes.


## <img src="./IMAGES/B.png" width="40"> Additional components
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
*  16× 5mm Ball magnets [🢂](https://www.magnetmax.de/Neodym-Kugelmagnete/Magnetkugel-Kugelmagnet-O-5-0-mm-Neodym-vernickelt-N40-haelt-400-g::158.html)
* 8× - 16× Screws DIN912 ISO 4762 M3×12 mm [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* 2× M2×12 mm and 2× M2 nut - non-magnetic
* 1× Raspberry Pi Camera [🢂](https://www.amazon.de/Raspberry-Pi-v2-1-1080P-Kamera-Modul/dp/B01ER2SMHY/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1LUZK9XHFS5CX&keywords=raspberry+pi+camera+v2.1&qid=1565008837&s=gateway&sprefix=raspberry+pi+camera+%2Caps%2C163&sr=8-4)
* 1x Raspberry Pi
* 1x wired LED (blue)
* 1x button
* 1x Power Supply for Raspberry Pi

## <img src="./IMAGES/A.png" width="40"> Assembly and alignment
For assembly instructions of the respective modules refer to the links in Modules for this setup.

## <img src="./IMAGES/L.png" width="40"> Electronics
🢂 Find more in the [Electronics section](../../ELECTRONICS)

## <img src="./IMAGES/W.png" width="40"> Software
🢂 Find the software for this setup in our dedicated [UC2-Software-GIT](https://github.com/bionanoimaging/UC2-Software-GIT)

## <img src="./IMAGES/E.png" width="40"> Quick-start

This assumes you have built the Inline-holographical microscope already.

Soon we will provide a browser-plugin for the image reconstruction using found in our **ImJoy** [Github-Repository](https://github.com/bionanoimaging/UC2-ImJoy-GIT).

<p align="center">
<img src="./IMAGES/Inline_Beads.png" width="500">
</p>

This is an example for an acquired inline hologram.

### <img src="./IMAGES/E.png" width="40"> Image Acquisition

In order to use this setup one has to take a picture with the Raspberry Pi camera module. This can conveniently be done using the command-line tool ```raspistill``` which can be called from the Terminal in the Raspberry Pi.

A more in-detail documentation can be found [here](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md).

We use a very basic setting with auto-white-balance, auto-exposure and jpeg compression by typing

```
cd ~
mkdir inlineholo
cd inlineholo
raspistill -f my_inline_test.jpg
```

This will open the camera, capture an image and saves it as ```my_inline_test.pg```in the folder ```inlineholo``` in the Pi-home directory. Using a USB-drive one can copy the file to a computer for further processing.

## <img src="./IMAGES/E.png" width="40"> Image Reconstruction

We have created an ```iPython-Notebook``` for this task which can be found [here](CODE/Listings_1_ReconHoloInline.ipynb).


### <img src="./IMAGES/E.png" width="40"> Tutorial for installing the Inline-Hologram Reconstruction software

Install Anaconda 3.6 (latest version for windows).
Therefore follow the tutorial in this link: [Anaconda Installation](https://docs.anaconda.com/anaconda/install/) (external).

0. After you've installed Anacoda, download the ipython notebook file: ```Listings_1_ReconHoloInline.ipynb``` by clicking this [link](./Listings_1_ReconHoloInline.ipynb) and type control+s for saving it somewhere on the computer
<p align="center"><img src="./IMAGES/Tut1.png" width="400"></p>

1. Copy Image in the same folder as the ```.iypnb```-file
<p align="center"><img src="./IMAGES/Tut2.png" width="400"></p>

2. ```Windows+R``` => Run prompt
3. enter ```CMD``` and hit enter
4. The Terminal opens
5. Copy the path where you have the image and script file (e.g. C:\Users\diederichbenedict\Downloads\HOLOGRAM)
<p align="center"><img src="./IMAGES/Tut3.png" width="400"></p>
6. Enter: cd "C:\Users\diederichbenedict\Downloads\HOLOGRAM" (or whatever path; right click is paste in the terminal)
<p align="center"><img src="./IMAGES/Tut4.png" width="400"></p>
7. Type "ipython notebook" -> enter
<p align="center"><img src="./IMAGES/Tut5.png" width="400"></p>
8. Browser opens at http://localhost:8888 (copy paste if not opening automatically)
9. Go to the field "Define experimental parameters" and change the variable name "my_holo_file" to the filename you acquired (e.g. "hologram_mouse.jpg"
<p align="center"><img src="./IMAGES/Tut6.png" width="400"></p>
10. Go to Cell and hit "run all" and keep your fingers crossed!!
11. Vary the position of the slider in the
<p align="center"><img src="./IMAGES/Tut7.png" width="400"></p>



If you're not happy with the region of interest (ROI) change the center coordinates ```center_x``` and ```center_y``` to what you would like to see in the RAW-hologram.
Rerun the programm by hitting "run all"

If you want to process a bigger field of view or ROI change the variable "mysize" to a bigger number, but take into account, that the processing time increasing!

If you think, that the refocussing range is either too small or too large (i.e. too close or too far away), than change the parameters:

```
# Creating costume widget
FocusSlider = widgets.FloatSlider(
    min = 0,
    max = .01,
    step = 1e-3,
    value=0,
    description = 'ZPos',
    continuous_update = True
)
```


```min```, ```max``` and step which describe the minimal/maximal focal distance between the sensor and the sample as well as the stepsize where the algorithm calculates the refocussed hologram.

## <img src="./IMAGES/E.png" width="40"> Results
None yet. Be the first to share yours!

## <img src="./IMAGES/S.PNG" width="40"> Contribution
If you find this piece usefull or you want to improve it, please feel free to file an issue or write us a message!
