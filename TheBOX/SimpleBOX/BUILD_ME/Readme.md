# Building The MiniBOX and SimpleBOX

This is a guide for building the [SimpleBOX and MiniBOX](../SimpleBOX). If you were looking for another BOX version, [click here](../../).

* Total price: under 150 € for SimpleBOX, around 80 € for MiniBOX
* Printing time including preparation: under 4 days for SimpleBOX, under 2 days for MiniBOX
* Assembly time: under 1 day

### Content
1. [Shopping](#-shopping)
1. [3D printing](#-3d-printing)
1. [Tools](#-which-tools-to-use)
1. [Assembly](#-assembly)

## <a href="#icon01" name="icon01"><img src="./IMAGES/B.png" height="40"></a> Shopping
### What to buy
Check out the [RESOURCES](../../../TUTORIALS/RESOURCES) for more information! The parts here are the cheapest or easily accessible for universities, but almost everything has an alternative in Amazon!

Link - name of part             |  Amount |  Comment | Price
  :-------------------------:|:----------------------------:|:-------------------------:|:-------------------------:
  3D printing material|~260 g| Choose material that works with your 3D printer. If unsure, have a look at the guide in [3D printing section](#-3d-printing)|8 €
  [Microscope objective 4×](https://de.aliexpress.com/item/32947647522.html?spm=a2g0x.search0104.3.54.6cf57a4c3DwsTO&transAbTest=ae803_3&ws_ab_test=searchweb0_0%2Csearchweb201602_6_10065_10130_10068_10890_10547_319_10546_317_10548_10545_10696_10084_453_454_10083_10618_10307_537_536_10902_10059_10884_10887_321_322_10103%2Csearchweb201603_6%2CppcSwitch_0&algo_pvid=06d972be-b176-4446-8665-56d9e61a8d2c&algo_expid=06d972be-b176-4446-8665-56d9e61a8d2c-7)  |  1 piece | It is possible to use 10× objective as well, but we recommend 4× for this setup.| 11 €
  [Lens 100 mm](https://optikbaukasten.de/)  |  1 piece |Artikel 2004|6 €
  [Lens 40 mm](https://optikbaukasten.de/)  |  2 pieces |Artikel 2120|12 €
  [Lens -50 mm](https://www.thorlabs.com/thorproduct.cfm?partnumber=LC1259)  |  1 piece |LC1259|19 €
  [Mirror](https://www.rayher.com/de/spiegelmosaik-selbstklebend-14548606)  |  2 pieces | 45 pieces package, only 2 pieces needed.|0,50 €
  [Magnets](https://www.magnetladen.de/kugelmagnet-5-mm-n42-nickel/)  |  48 pieces | Ball magnets, diameter 5 mm.|total 12 €
  [Screws](https://eshop.wuerth.de) |   ~40 pieces | (Art.-Nr. 00843  12) M3×12, galvanized steel - ~32  pieces; (Art.-Nr. 00843  8) M3×8, galvanized steel - ~3 pieces (32 pieces extra for putting screws to all sides of all cubes); (Art.-Nr. 00943  30) M3×30, not magnetic - 1 piece; (Art.-Nr. 03223) M3 nut | total ~3 €
  [Chocolate](https://prod-cd-origin.milka.de/produkte/milka-weisse-schokolade)|1 bar| Use it as a reward when you're done.

Notes on screws: In order to have the screws on both sides of the cubes, you will need extra 32 pieces M3×8 screws (or M3×12).

### Extra parts for SimpleBOX
Link - name of part             |  Amount |  Comment | Price
  :-------------------------:|:----------------------------:|:-------------------------:|:-------------------------:
  3D printing material|some more| |2-5 €
  [Eyepiece 10×](https://de.aliexpress.com/item/32897739739.html?spm=a2g0s.9042311.0.0.466f4c4dehniSH)  |  1 piece | The holder is designed for an eyepiece of this diameter. Sold in pairs.|11 €
  [Lens 100 mm](https://optikbaukasten.de/)  |  1 piece |Artikel 2004|6 €
  [Flashlight](https://www.pollin.de/p/led-taschenlampe-alu-5-w-cree-led-3xmicro-schwarz-b-ware-535448)  |  1 piece | Light source for the projector and microscope.|7 €
  [Screws](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/) |   ~20 pieces | M3×12, galvanized steel - ~16  pieces; (M3×8, galvanized steel - 16 pieces extra for putting screws to all sides of all cubes); | total ~2 €
  [Chocolate](https://prod-cd-origin.milka.de/produkte/milka-weisse-schokolade)|1 bar| One more won't kill you if you already ate the previous one ;-)


## <a href="#icon02" name="icon02"><img src="./IMAGES/P.png" height="40"></a> 3D Printing:

Completely new to 3D printing? Have a look into this [beginner's guide](https://www.makeuseof.com/tag/beginners-guide-3d-printing/)!

Our quick printing tutorial can be found here:
[![UC2 YouSeeToo - How to print the base-cube?](./IMAGES/CURA_1.png)](https://www.youtube.com/watch?v=SblqYJYXe4k&feature=youtu.be)

We have a good experience with this printer and settings:
* Prusa i3/MK3S
  * For MiniBOX: Prusament PLA 1,75 mm, for one Box: 0,26 g = 88 m = 38 hours = 8 €
  * For SimpleBOX in total: Prusament PLA 1,75 mm, for one Box: 0,455 kg = 152,53 m = 69 hours = 13 €
  * Profile Optimal 0,15 mm, infill 20%, no support, 215/60°C


### <a href="#icon03" name="icon03"><img src="./IMAGES/D.png" height="40"></a>  Housing
Name of part - Link to STL file             |  Amount
:-------------------------:|:----------------------------:
[(01) Basic Cube 1×1](./STL/01_10_Cube_1x1_v2.stl)  |  8 pieces
[(02) Basic Lid 1×1](./STL/02_10_Lid_1x1_v2.stl)  |  8 pieces
[(03) Baseplate 4×1](./STL/03_Assembly_base_4x1.stl)  |  2 pieces
[(04) Baseplate 4×4](./STL/04_Assembly_base_4x2.stl)  |  1 piece

Note on the baseplates: As mentioned before, the MiniBOX was developed with the idea of injection molding produced cubes in mind. To perform the experiment conveniently with 3D printed baseplates, we suggest as optimal one Baseplate 4×4 and two Baseplates 4×1.

### <a href="#icon05" name="icon05"><img src="./IMAGES/D.png" height="40"></a> Inserts

Name of part - Link to STL file            |  Amount |  Comment
:-------------------------:|:-------------------------:|:-------------------------:
[(05) Z-Stage Focusing Insert and Objective Mount](./STL/05_20_focus_inlet_linearflexure_stage_objectivemount.stl)  |  1 piece  | The insert and the objective mount for RMS thread print together.
[(06) Z-Stage Gear](./STL/06_20_gear.stl) |  1 piece   | With hexagonal hole for the nut.
[(08) Mirror Holder 45° 30×30mm²](./STL/08_20_Cube_Insert_Mirror_Holder_30x30Mirror_v2.stl)  |  2 pieces | Size fits for the listed mirrors.
[(09) Generic Sample Holder](./STL/09_20_Cube_insert_Sample_holder.stl)  |  1 piece | In the SimpleBOX, it is used to hold the object in the projector setup.
[(10) Generic Sample Holder Clamp](./STL/10_20_Cube_Insert_Sample_clamp.stl)  |  1 piece | To fix the sample.
[(12) Lens Holder](./STL/12_UC2_Lens_insert_v2_40mm.stl)  |  1 piece | For the 40 mm lens from the shopping list.
[(13) Lens Holder](./STL/13_UC2_Lens_insert_v2_-50mm.stl)  |  1 piece | For the 100 mm lens from the shopping list.
[(14) Lens Holder](./STL/14_UC2_Lens_insert_v2_100mm.stl)  |  1 piece | For the -50 mm lens from the shopping list.


### Extra parts for SimpleBOX
### <a href="#icon03" name="icon03"><img src="./IMAGES/D.png" height="40"></a>  Housing
Name of part - Link to STL file             |  Amount
:-------------------------:|:----------------------------:
[(01) Basic Cube 1×1](./STL/01_10_Cube_1x1_v2.stl)  |  3 pieces
[(02) Basic Lid 1×1](./STL/02_10_Lid_1x1_v2.stl)  |  3 pieces

### <a href="#icon04" name="icon04"><img src="./IMAGES/D.png" height="40"></a> Inserts

Name of part - Link to STL file            |  Amount |  Comment
:-------------------------:|:-------------------------:|:-------------------------:
[(07) Eyepiece/flashlight mount](./STL/07_20_Cube_Insert_Holder_flashlight_eyepiece_v2.stl)  |  2 pieces | Diameter fits for the listed eyepiece and flashlight.
[(11) Smartphone Holder](./STL/11_30_Smartphone_Holder.stl)  |  1 piece | Which belongs together with the eyepiece cube.
[(13) Lens Holder](./STL/13_UC2_Lens_insert_v2_-50mm.stl)  |  1 piece | For the 100 mm lens from the shopping list.

## <a href="#icon05" name="icon05"><img src="./IMAGES/A.png" height="40"></a> Which tools to use
Tool             |  Image|  Comment
:-------------------------:|:----------------------------:|:-------------------------:
[Electric screw driver with 2,5 mm hex bit](https://www.amazon.de/Bosch-Akkuschrauber-Generation-Bits-Ladeger%C3%A4t/dp/B00TTZU566/ref=asc_df_B00TTZU566/?tag=googshopde-21&linkCode=df0&hvadid=255989693737&hvpos=1o1&hvnetw=g&hvrand=6125749874385941808&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9042960&hvtargid=pla-421346020200&psc=1&th=1&psc=1) |[<img src="./IMAGES/screwdriver.jpg" width="300">](https://www.amazon.de/Bosch-Akkuschrauber-Generation-Bits-Ladeger%C3%A4t/dp/B00TTZU566/ref=asc_df_B00TTZU566/?tag=googshopde-21&linkCode=df0&hvadid=255989693737&hvpos=1o1&hvnetw=g&hvrand=6125749874385941808&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9042960&hvtargid=pla-421346020200&psc=1&th=1&psc=1) | For putting the cubes together using M3×12 and M3×8 screws.
[2,5 mm hex key](https://www.amazon.de/Presch-Innensechskant-Satz-Kugelkopf-Innensechskantschl%C3%BCssel/dp/B079V335CR/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2K89GU3MY8P26&keywords=hex+key+set&qid=1575997133&s=diy&sprefix=hex+%2Cdiy%2C160&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRENMU0hKWkJRR0FEJmVuY3J5cHRlZElkPUEwMDIzMjIyMzFBWVIyOEpORU1FSCZlbmNyeXB0ZWRBZElkPUEwMzk0NjQwMlA0NFZDTVk0Tk9LUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) | [<img src="./IMAGES/hex-keys.jpg" width="300">](https://www.amazon.de/Presch-Innensechskant-Satz-Kugelkopf-Innensechskantschl%C3%BCssel/dp/B079V335CR/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2K89GU3MY8P26&keywords=hex+key+set&qid=1575997133&s=diy&sprefix=hex+%2Cdiy%2C160&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRENMU0hKWkJRR0FEJmVuY3J5cHRlZElkPUEwMDIzMjIyMzFBWVIyOEpORU1FSCZlbmNyeXB0ZWRBZElkPUEwMzk0NjQwMlA0NFZDTVk0Tk9LUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)| For fine adjustment of all the M3 screws if needed. The middle one in the picture.
[Needle-nose Pliers](https://www.amazon.de/Br%C3%BCder-Mannesmann-Telefonzange-gerade-M10948/dp/B003A63EIG/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=needle+nose+pliers&qid=1575997091&s=diy&sr=1-3) |<img src="./IMAGES/pliers.jpg" width="300"> | Might come handy

## <a href="#icon06" name="icon06"><img src="./IMAGES/A.png" height="40"></a>  Assembly
Part - link             |  Result|  Comment
:-------------------------:|:----------------------------:|:-------------------------:
[Baseplates](../../../CAD/ASSEMBLY_Baseplate_v2)|[<img src="./IMAGES/baseplates.jpg" width="300">](../../../CAD/ASSEMBLY_Baseplate_v2)|1× "big" baseplate (4×2), 3× "small" baseplate (4×1)
[Lens Cubes](../../../CAD/ASSEMBLY_CUBE_Lens_v2)|[<img src="./IMAGES/lens.jpg" width="300">](../../../CAD/ASSEMBLY_CUBE_Lens_v2)| 5× Lens Cube; Write the focal lenghts of the lenses on the holders, so you can always easily find the right one when building different setups.
[Mirror Cubes](../../../CAD/ASSEMBLY_CUBE_Mirror_45_v2)|[<img src="./IMAGES/mirror.jpg" width="300">](../../../CAD/ASSEMBLY_CUBE_Mirror_45_v2)| 2× Mirror Cube
[Sample Cube](../../../CAD/ASSEMBLY_CUBE_Sample_Holder_v2)|[<img src="./IMAGES/sample.jpg" width="300">](../../../CAD/ASSEMBLY_CUBE_Sample_Holder_v2)|1× Sample Holder Cube
[Z-Stage Cube](../../../CAD/ASSEMBLY_CUBE_Z-STAGE_mechanical_v2)|[<img src="./IMAGES/z-stage.jpg" width="300">](../../../CAD/ASSEMBLY_CUBE_Z-STAGE_mechanical_v2)|1× mechanical Z-Stage with Sample Clamp
[Flashlight Cube](../../../CAD/ASSEMBLY_Lens_v2)|[<img src="./IMAGES/flashlight.jpg" width="300">](../../../CAD/ASSEMBLY_Lens_v2)| 1× Flashlight Cube
[Eyepiece and Smartphone Cube](../../../CAD/ASSEMBLY_CUBE_Eyepiece_v2)|[<img src="./IMAGES/smartphone.jpg" width="300">](../../../CAD/ASSEMBLY_CUBE_Eyepiece_v2)|1× Eyepiece Cube with Smartphone Holder mounted on it


## <a href="#icon07" name="icon07"><img src="./IMAGES/E_S.png" height="40"></a> Done! Great job! Explore the experiments with our [work sheets](../DOCUMENT/UC2_simpleBOX.pdf) now.
