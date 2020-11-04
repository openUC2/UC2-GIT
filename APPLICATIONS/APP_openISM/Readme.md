## openISM

This is the repository for the openISM project which integrates a laser-scanning module for image-scanning microscopy (ISM) to the UC2-system.

<p align="center">
<img src="./IMAGES/Application_openISM_v2.png" width="500">
</p>

***Fig 1:*** *This is the ready-to-print module which clicks into the UC2-system*


This module is based on the work about Image Scanning Microscopy (ISM) by Enderlein et al. [1] and instant Structured Illumination Microscopy (iSIM) by A. York et al. [2]. It uses a low-cost MEMS-based laser-scanning video-project (Sony MHL  (532 nm) and a Raspberry Pi driven DMD module to generate a structured illumination for microscopy. Since we use coherent illumination, we can create pattern suitable for SIM in order to increase the lateral resolution. So far we're not aiming for any super-resolutio, but rather give a proof of principle.  

<p align="center">
<img src="./IMAGES/Application_openISM_v2_2.png" width="500">
</p>

***Fig 2:*** *A beam-expander magnifies the collimated beam which hits the DMD displaying a set of gratings*

The angle between the collimated and expanded Laser-beam and the DMD is 25° in order to get the maximum in the diffracted orders.




## Device's features:

- Super-Resolution by confining the signal
- Very low cost:  ~300€
- Easy to align
- Open-Source


## Optical System

<p align="center">
<img src="./IMAGES/DSC_2023.jpg" width="400">
</p>

***Fig 3:*** *The full system based on the modular cubes*

In recent years portable devices to experience entertainment "on-the-go" like video-projectors or movie screens have found their ways to the consumer market. Many of these produce like portable projectors share the same components as their scientific counterparts (e.g. digital mirror devices, DMD) but for a much lower price since components are mass-produced. Besides wide-field projection system based on LCoS (liquid crystal on silica), LCD or DMD displays, more exotic laser-scanning based systems like the here used Sony MP.CL1A (Japan) enable the creation of laser-scanning microscopes for a very low price (e.g. 300\, Euro).

To display a color image on a screen (e.g. wall), a small MEMS (Micro-Electro-Mechanical Systems) scans a set of RGB Blue=450nm, Green}=530, Red = 650, laser-beams over the 2D (e.g. X/Y) plane with a frame-rate of 60fps at a spatial resolution of 1920*720 pixel^2. \\
This device can easily be integrated in the UC2-system by providing a customized  adapter which makes the device compatible with the 50*5 mm^2 grid. Following the work by Enderlein et al. (ISM) (Muller2010a) and York et al. (iSIM)  (York2012) we displayed an incoherent grid of point sources in the sample plane, which can be used to create a better optical sectioning and improve optical resolution. This is done in a post-processing step, where each 2D image gets divided in a series of tiles of the size of the PSF-extend around one illumination position. Each tile corresponds to a confocal-like measurement, where the information can computationally be confined, when a de-centred detection pinhole is assumed. The resulting signal is placed on a canvas with twice the sampling of the original measurement, which creates an optical super-resolution up to a factor of $\sqrt{2}$ (McGregor2015).\\

Since this device is not meant to be used for scientific instrumentation, there are only limited information available. Also, since the resolution of 1920*720 pixels^2 is not very common, ordinary computers to generate a display on this device where interpolating the images. Connecting the device to a Apple Macbook (USA) at a display-resolution of 720p ensured a one-to-one pixel mapping, where we created a customized Python-script to generate and display the ISM-patterns full-screen. The monochromatic cellphone-camera (Huasei P20, China) was driven using the open-source software FreeDCam (Fuchs2018), where the exposure time $t_{exp}=1/60\,s$ matches the frame-rate of the laser-scanning projector in order to reduce bouncing effects of both refresh-rates.

## Optical Setup

The optical setup shown in Fig. 1 is straight-forward. The resonating MEMS in the projector needs to be imaged into the BFP of the microscope objective lens. In order to get high-resolution images, the BFP is over-filled by the mirror ideally. We assumed a diameter of the aluminium mirror of d_{mirror}=1.5mm and a diameter of the BFP of around d_{BFP}=5.5mm which requires a telescope, created by a lens f'_1=30mm and a following tube-lens f'_2=180mm. The low-cost infinity-corrected microscope objective (Optika, 20x, NA=0.4,  N-plan, [here](https://www.optik-pro.de/fuer-mikroskope/optika-objektiv-20x-0-40-infinity-n-plan-pol-b-383pol-m-146p/p,56893#tab_bar_1_select) was put in a motor-driven Z-stage to allow focussing the objective relative to the sample. A set of different dichroic-mirror cubes with suitable filters allows the switching between different fluorophores and excitation wave-lengths.


## Parts

### Bill of material

|  Type | Details  |  Price | Link  |
|---|---|---|---|
| Laser |  12V 532nm 200mw Green Laser Dot Module Fan Cooling TTL 0-30KHZ-Long time working |  90 € | [Lilly Electronics](http://www.lillyelectronics.com/12v-532nm-200mw-green-laser-dot-module-fan-cooling-ttl-0-30khz-long-time-working)  |
| DMD |  Evaluierungsmodul (EVM) DLP® LightCrafter™ Display 2000 |  90 € | [Digikey](https://www.digikey.de/product-detail/de/texas-instruments/DLPDLCR2000EVM/296-47119-ND/7598640)  |
| Raspberry Pi | Raspi+SD-Card+Case+Powersupply(for DMD+Raspi, 5V, >=3A!) |  70 € | [Reichelt](https://www.reichelt.de/raspberry-pi-4-b-4x-1-5-ghz-1-gb-ram-wlan-bt-rasp-pi-4-b-1gb-p259874.html?PROVID=2788&gclid=Cj0KCQiAz53vBRCpARIsAPPsz8X9hCOt9yVVB_WqLCmKSs2e-KuThVnrMEtl2TRbAUTqtVoNZU3zM3YaAg2ZEALw_wcB&&r=1)  |
| Tube-lens | Lens, f=180mm |  10 € | [PGI-Versand](https://www.pgi-versand.de/?id=47&mode=artdet&artnr=564.OA.64)  |
| Telescope-lens | 2x Achromatic 1inch Lens, f=50mmmm |  82 € | [Thorlabs](https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-050-A)  |
| Dichroics  |  Various |  200 € | [Thorlabs]()  |
| Mirror | 1inch Silver Mirror, Protected |  50 € | [Thorlabs]()  |
| iPhone Lens | iPhone 5 lens for the telescope  (optional) |  5 € | [Amazon]()  |
| Lens | 25mm lens for the telescope (optional) |  5 € | [Amazon]()  |
| Dichroics  |  Various |  200 € | [Thorlabs]()  |
| PCB for Raspi-DMD connection  |  Various |  8 € | [See below]()  |

* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!


### 3D printed parts

Parts to print:

* 1× [SIM-Module 2×4](./STL/Assembly_openSIM_module_v2_30_CUBE_openSIM_base_v2_1.stl)
* 1× [Telescope for Beam Expansion](./STL/Assembly_openSIM_module_v2_30_CUBE_OpenSIM_Beamexpander_v2_9.stl)
* 1x [DMD Adapter](./STL/Assembly_openSIM_module_v2_30_CUBE_openSIM_DLP2000_Holder_mirrored_3.stl)

### Additional parts for the whole setup
- 1x Kinematic Mirror Mount (for 1inch Silver mirror!) [here](../ASSEMBLY_CUBE_Mirror_Kinematic_45_v2)
- 1x Mirror Mount (for 1inch Silver mirror!) [here](../ASSEMBLY_CUBE_Mirror_45_v2)
- 1x OpenFlexure Delta-Stage (by Richard Bowman et al.) + Adapter + Objective lens (you can choose!)  [here](../ [here](../CUBE_INSERT_OpenFlexure_Deltastage))
- Dichroic Mirror Cube [here](../ASSEMBLY_CUBE_Dichroic_Beamsplitter_v2)
- Basler-Camera + Adapter [here](../ASSEMBLY_CUBE_BaslerCam)




## Software  

This will come in the future.


### Install the Anybeam Nebra with the Raspberry Pi

Open the file ```/boot/config.txt``` and add the following lines:

```
# Additional overlays and parameters are documented /boot/overlays/README
dtoverlay=dpi24
overscan_left=0
overscan_right=0
overscan_top=0
overscan_bottom=0
framebuffer_width=1280
framebuffer_height=720
enable_dpi_lcd=1
display_default_lcd=1
dpi_group=2
dpi_mode=85
dpi_output_format=0x070027
```


## Further reading

This will come in the future.



## Result

This is just one frame of some fluorescent pollen grains:
<p align="center">
<img src="./IMAGES/IMG_20190917_094835.jpg" width="400">
</p>



## Participate!

Do you want to show your own results? Do you have ideas for improvements? Let us know!
