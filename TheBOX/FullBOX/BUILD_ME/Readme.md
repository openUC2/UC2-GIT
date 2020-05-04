# Building The FullBOX

This is a guide for building the [FullBOX](../FullBOX). If you were looking for another BOX version, [click here](../../).

### Content
1. [Necessary Parts](#-necessary-parts)
1. [What's inside the FullBOX](#current-state-of-art)
1. [3D printing](#-3d-printing)
1. [Tools](#-which-tools-to-use)

## <img src="./IMAGES/D.png" height="40"><img src="./IMAGES/B.png" height="40"> Necessary Parts
The detailed up-to-date list of all components can be found in this [google-spreadsheet](https://docs.google.com/spreadsheets/d/1U1MndGKRCs0LKE5W8VGreCv9DJbQVQv7O6kgLlB6ZmE/edit?usp=sharing).

* Check out the [RESOURCES](../../../TUTORIALS/RESOURCES) for more information!

The overall price-tag is around 600€ including the Raspberry Pi, Camera, Optics, 3D printed parts and all additional components.

<p align=center>
<img src="./IMAGES/UC2_Setups_theBOX.png" width=400>
</p>

## Currect state-of-art
What is inside the Box?

Click on the arrow (🢂) to find the STLs and assembly tutorials of the respective cubes and baseplates.

<p align="center">
<img src=".\IMAGES\IMG_20190905_174601.jpg" height="400">
</p>
<p align="center">
<img src=".\IMAGES\IMG_20190905_174642.jpg" height="400">
</p>
<p align="center">
<img src=".\IMAGES\UC2_Setups_theBOX.png" height="400">
</p>
<p align="center">
<img src=".\IMAGES\IMG_20190905_175948.jpg" height="400">
</p>

  * Baseplate  4×4 [🢂](../../../CAD/ASSEMBLY_Baseplate_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180802.jpg" height="400">
  </p>

  * Baseplate 4×2 [🢂](../../../CAD/ASSEMBLY_Baseplate_v2)
  * Baseplate 4×1 - 2× [🢂](../../../CAD/ASSEMBLY_Baseplate_v2)
  * Raspberry Pi

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_175916.jpg" height="400">
  </p>

  * Cube 2×1: Z-stage with 10× objective and sample holder [🢂](../../../CAD/ASSEMBLY_CUBE_Z-STAGE_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180724.jpg" height="400">
  </p>

  * Fluomodule Cube [🢂](../../../CAD/ASSEMBLY_CUBE_Dichroic_Beamsplitter_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180650.jpg" height="400">
  </p>

  * LED Cube [🢂](../../../CAD/ASSEMBLY_CUBE_LED_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180526.jpg" height="400">
  </p>

  * Eyepiece Cube (20×) with Smartphone holder [🢂](../../../CAD/ASSEMBLY_CUBE_Cellphonemount) & [🢂](../../../CAD/ASSEMBLY_CUBE_Eyepiece_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180334.jpg" height="400">
  </p>

  * Laser Cube [🢂](../../../CAD/ASSEMBLY_CUBE_Laser_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180454.jpg" height="400">
  </p>

  * 45° mirror Cube - 2× [🢂](../../../CAD/ASSEMBLY_CUBE_Mirror_45_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180638.jpg" height="400">
  </p>

  * Kinematic mirror mount Cube – perpendicular to optical path [🢂](../../../CAD/ASSEMBLY_CUBE_Mirror_Kinematic_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180410.jpg" height="400">
  </p>

  * Kinematic mirror mount Cube – 45° to optical path [🢂](../../../CAD/ASSEMBLY_CUBE_Mirror_Kinematic_45_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180433.jpg" height="400">
  </p>

  * RaspiCam Cube [🢂](../../../CAD/ASSEMBLY_CUBE_RaspiCam_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180158.jpg" height="400">
  </p>

  * Beamsplitter Cube [🢂](../../../CAD/ASSEMBLY_CUBE_Beamsplitter_v2)
  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180252.jpg" height="400">
  </p>

  * Beamexpander Cube with an iPhone lens and +26 mm lens [🢂](../../../CAD/ASSEMBLY_CUBE_Beamexpander_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180309.jpg" height="400">
  </p>

  * Lens Cube - 2× [🢂](../../../CAD/ASSEMBLY_CUBE_Lens_v2) & [🢂](../../../CAD/ASSEMBLY_CUBE_Lens_CYLINDRICAL_v2)

    *  +100 mm – blue label holder, in cube

    * +39,5 mm – yellow label holder, in cube
    * Negative – white label holder with *f* written on the label
    * 4× Objective – green label holder
    * Cylindrical lens in its holder

  * Bag with three lenses - +156 mm, +40 mm, +25 mm in an adapter for Beamexpander

    <p align="center">
    <img src=".\IMAGES\IMG_20190905_180708.jpg" height="400">
    </p>
    <p align="center">
    <img src=".\IMAGES\IMG_20190905_175426.jpg" height="400">
    </p>

  * Generic sample holder Cube and Sample chamber [🢂](../../../CAD/ASSEMBLY_CUBE_Sample_Holder_v2)

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_180608.jpg" height="400">
  </p>

  * Generic sample holder – comb structure
  * LED array [🢂](../../../CAD/ASSEMBLY_CUBE_LED_Matrix_v2)
  * Sample stage [🢂](../../../CAD/ASSEMBLY_CUBE_S-STAGE_v2)
  * Flashlight
  * Blue laser pointer with switch

  <p align="center">
  <img src=".\IMAGES\IMG_20190905_175722.jpg" height="400">
  </p>

  * Long an short micro-USB cable
  * USB power cable
  * Short Raspi cable
  * Raspi C-power supply
  * Bag with extra screws – M3 with head: 8 mm, 12 mm, 18 mm, 30 mm; M3 no head 5 mm
  * Coupling screw for M3 and M4 screws (for Sample stage and Z-stage)
  * Z-stage sample clamp for microscope slides
  * Z-stage spiral fixing clamp
  * SD card

<p align="center">
<img src=".\IMAGES\IMG_20190905_175241.jpg" height="400">
</p>

## <img src="./IMAGES/P.png" height="40"> 3D Printing:

Completely new to 3D printing? Have a look into our [TUTORIALS](../../../TUTORIALS)!

Our quick printing tutorial can be found here:
[![UC2 YouSeeToo - How to print the base-cube?](./IMAGES/UC2_TutorialPrintYoutube.PNG)](https://www.youtube.com/watch?v=JswW8BexnC4&feature=youtu.be)

We have a good experience with this printer and settings:
* Prusa i3/MK3S
  * PLA 1,75 mm, for one Box: ??? kg = ??? m = ??? hours = ??? €
  * Profile Optimal 0,15 mm, infill 20%, no support, 215/60°C

## <img src="./IMAGES/A.png" height="40"> Which tools to use
Tool             |  Image|  Comment
:-------------------------:|:----------------------------:|:-------------------------:
[Electric screw driver with 2,5 mm hex bit](https://www.amazon.de/Bosch-Akkuschrauber-Generation-Bits-Ladeger%C3%A4t/dp/B00TTZU566/ref=asc_df_B00TTZU566/?tag=googshopde-21&linkCode=df0&hvadid=255989693737&hvpos=1o1&hvnetw=g&hvrand=6125749874385941808&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9042960&hvtargid=pla-421346020200&psc=1&th=1&psc=1) |<img src="./IMAGES/screwdriver.jpg" width="300"> | For putting the cubes together using M3×12 and M3×8 screws.
[2,5 mm hex key](https://www.amazon.de/Presch-Innensechskant-Satz-Kugelkopf-Innensechskantschl%C3%BCssel/dp/B079V335CR/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2K89GU3MY8P26&keywords=hex+key+set&qid=1575997133&s=diy&sprefix=hex+%2Cdiy%2C160&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRENMU0hKWkJRR0FEJmVuY3J5cHRlZElkPUEwMDIzMjIyMzFBWVIyOEpORU1FSCZlbmNyeXB0ZWRBZElkPUEwMzk0NjQwMlA0NFZDTVk0Tk9LUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) | <img src="./IMAGES/hex-keys.jpg" width="300">| For fine adjustment of all the M3 screws if needed.
[1,5 mm hex key](https://www.amazon.de/Presch-Innensechskant-Satz-Kugelkopf-Innensechskantschl%C3%BCssel/dp/B079V335CR/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2K89GU3MY8P26&keywords=hex+key+set&qid=1575997133&s=diy&sprefix=hex+%2Cdiy%2C160&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRENMU0hKWkJRR0FEJmVuY3J5cHRlZElkPUEwMDIzMjIyMzFBWVIyOEpORU1FSCZlbmNyeXB0ZWRBZElkPUEwMzk0NjQwMlA0NFZDTVk0Tk9LUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) |↑↑ | For assembly of the Z-Stage - mounting worm screws.
[Needle-nose Pliers](https://www.amazon.de/Br%C3%BCder-Mannesmann-Telefonzange-gerade-M10948/dp/B003A63EIG/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=needle+nose+pliers&qid=1575997091&s=diy&sr=1-3) |<img src="./IMAGES/pliers.jpg" width="300"> | Might come handy


## <img src="./IMAGES/E_S.png" height="40"> Done! Great job!
