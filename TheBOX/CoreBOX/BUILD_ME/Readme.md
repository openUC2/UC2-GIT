# Building The CoreBOX

This is a guide for building the [CoreBOX](../CoreBOX). If you were looking for another BOX version, [click here](../../).

* Total price: 230 €
* Printing time including preparation: 5 days
* Assembly time: 1 day

### Content
1. Shopping
1. 3D printing
1. Tools
1. Assembly

## <img src="./IMAGES/B.png" height="40"> Shopping
### What to buy

Link - name of part             |  Amount |  Comment | Price per amount used
  :-------------------------:|:----------------------------:|:-------------------------:|:-------------------------:
  3D printing material|~620 g| Choose material that works with your 3D printer. If unsure, have a look at the guide in [3D printing section](#3d-printing)|20 €
  [Microscope objective 4×](https://de.aliexpress.com/item/32947647522.html?spm=a2g0x.search0104.3.54.6cf57a4c3DwsTO&transAbTest=ae803_3&ws_ab_test=searchweb0_0%2Csearchweb201602_6_10065_10130_10068_10890_10547_319_10546_317_10548_10545_10696_10084_453_454_10083_10618_10307_537_536_10902_10059_10884_10887_321_322_10103%2Csearchweb201603_6%2CppcSwitch_0&algo_pvid=06d972be-b176-4446-8665-56d9e61a8d2c&algo_expid=06d972be-b176-4446-8665-56d9e61a8d2c-7)  |  1 piece | | 10 €
  [Lens 35 mm](https://www.thorlabs.com/thorproduct.cfm?partnumber=LA1027)  |  1 piece |We did the alignment with lenses of these focal lengths, but other combination are also possible. The alignment principle stays the same, but the positions of the element will be different. |22 €
  [Lens 40 mm](https://www.thorlabs.com/thorproduct.cfm?partnumber=LA1422)  |  2 pieces ||44 €
  [Lens 50 mm](https://www.thorlabs.com/thorproduct.cfm?partnumber=LA1131)  |  1 piece ||21 €
  [Lens 75 mm](https://www.thorlabs.com/thorproduct.cfm?partnumber=LA1608)  |  1 piece ||20 €
  [Lens 100 mm](https://www.thorlabs.com/thorproduct.cfm?partnumber=LA1509)  |  1 piece ||20 €
  [Flashlight](https://www.pollin.de/p/led-taschenlampe-alu-5-w-cree-led-3xmicro-schwarz-b-ware-535448)  |  1 piece | Light source for the projector and microscope.|7 €
  [Magnets](https://www.magnetladen.de/kugelmagnet-5-mm-n42-nickel/)  |  128 pieces | Ball magnets, diameter 5 mm.|30 €
  [Screws](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/) |   ~120 pieces | M3×12, galvanized steel - ~90  pieces; M3×8, galvanized steel - ~90 pieces; M3×18, galvanized steel - 2 pieces; M3×30, not magnetic - 1 piece; M3 nut | ~15 €
  [Chocolate](https://www.milka.de/produkte/milka-standard-tafeln/milka-wei%c3%9fe-schokolade?p=137&provider={D193998A-4A6D-4EA5-BAA8-209357B27A09}&categoryId=1395)|1 bar| Use it as a reward when you're done.

## <img src="./IMAGES/P.png" height="40"> 3D Printing:

Completely new to 3D printing? Have a look into this [beginner's guide](https://www.makeuseof.com/tag/beginners-guide-3d-printing/)!

Our quick printing tutorial can be found here:
[![UC2 YouSeeToo - How to print the base-cube?](./IMAGES/UC2_TutorialPrintYoutube.PNG)](https://www.youtube.com/watch?v=JswW8BexnC4&feature=youtu.be)

We have a good experience with this printer and settings:
* Prusa i3/MK3S
  * PLA 1,75 mm, for one Box: 0,6 kg = 235 m = 105 hours = 20 €
  * Profile Optimal 0,15 mm, infill 20%, no support, 215/60°C
  * [Hint](./IMAGES/prusa_printing_coreBOX.pdf)

### <img src="./IMAGES/D.png" height="40">  Housing
Name of part - Link to STL file             |  Amount
:-------------------------:|:----------------------------:
[(01) Basic Cube 2×1](./STL/01_10_Cube_2x1_v2.stl)  |  1 piece
[(02) Basic Lid 2×1](./STL/02_10_Lid_el_2x1_v2.stl)  |  1 piece
[(03) Basic Cube 1×1](./STL/03_10_Cube_1x1_v2.stl)  |  20 pieces
[(04) Basic Lid 1×1](./STL/04_10_Lid_1x1_v2.stl)  |  20 pieces
[(05) Baseplate 4×1](./STL/05_Assembly_base_4x1.stl)  |  4 pieces
[(06) Baseplate 4×2](./STL/06_Assembly_base_4x2.stl)  |  1 piece
[(07) Baseplate 1×1](./STL/07_10_Base_v2.stl)  |  1 piece
[(08) Baseplate Connector 1×1](./STL/08_Baseplate_Connector_v2.stl)  |  1 piece

### <img src="./IMAGES/D.png" height="40"> Inserts

Name of part - Link to STL file            |  Amount |  Comment
:-------------------------:|:-------------------------:|:-------------------------:
[(09) Z-Stage Focusing Insert](./STL/09_20_focus_inlet_linearflexure_v0_1.stl)  |  1 piece  | Rotate the part in your slicer before printing. Always print it laying on the flat side.
[(10) Z-Stage Objective Mount](./STL/10_30_focus_inlet_objective_mount_v7_7.stl) |  1 piece   | For mounting the objective lens (RMS thread).
[(11a) Z-Stage Bottom Plate](./STL/11a_20_focus_inlet_plate_bottom_2.stl) |  1 piece   | The plate holds the gear and screw in position, allowing the only to rotate but not to wobble.
[(11b) Z-Stage Top Plate](./STL/11b_20_focus_inlet_plate_top_3.stl) |  1 piece   | The plate holds the gear and screw in position, allowing the only to rotate but not to wobble.
[(12) Z-Stage Gear](./STL/12_20_focus_inlet_gear.stl) |  1 piece   | Kindly borrowed from [openflexure](https://openflexure.org).
[(13) Lens Holder](./STL/13_1inch_Assembly_Insert_Lens_mount_fixed_20_Lens_holder.stl)  |  6 pieces | Diameter fits for the listed lenses (25 mm).
[(14) Lens Holder Clamp](./STL/14_1inch_Assembly_Insert_Lens_mount_fixed_20_Lens_holder_clamp.stl)  |  6 pieces | Diameter fits for the listed lenses (25 mm).
[(15) Cylindrical Lens Holder](./STL/15_20_Cube_Insert_Lens_Cylindrical.stl)  |  1 piece | Diameter fits for the listed lenses (25 mm).
[(16) Generic Sample Holder](./STL/16_20_Cube_insert_Sample_holder.stl)  |  5 pieces | In the SimpleBOX, it is used to hold the object in the projector setup.
[(17) Generic Sample Holder Clamp](./STL/17_20_Cube_Insert_Sample_clamp.stl)  |  5 pieces | To fix the sample.
[(18) Mirror Holder 45° 30×30mm²](./STL/18_20_Cube_Insert_Mirror_Holder_30x30Mirror_v2.stl)  |  1 piece | Size fits for the listed mirrors.
[(19) Flashlight Holder](./STL/19_20_Cube_Insert_Flashlight_Holder.stl)  |  2 pieces |
[(20) Circular Aperture Guide](./STL/20_20_Cube_Insert_CirAp_Guide.stl)  |  2 pieces |
[(21) Circular Aperture Wheel](./STL/21_20_Cube_Insert_CirAp_Wheel.stl)  |  2 pieces |
[(22) Circular Aperture Lid](./STL/22_20_Cube_Insert_CirAp_Lid.stl)  |  2 pieces |
[(23) Circular Aperture Leaf](./STL/23_20_Cube_Insert_CirAp_Leaf1.stl)  |  14 pieces |
[(24) Laser Holder](./STL/24_20_Cube_Insert_Laser_Mount.stl)  |  2 pieces |
[(25) Laser Clamp](./STL/25_00_Laser_Clamp_OnOffSwitch.stl)  |  1 piece |
[(26) Beam Expander Insert](./STL/26_20_Cube_Insert_Beamexpander.stl)  |  1 piece |
[(27) Beam Expander Lens Adapter](./STL/27_30_Lens_Adapter_Beamexpander.stl)  |  1 piece |
[(28) Beamsplitter Insert](./STL/28_20_Cube_Insert_Beamsplitter.stl)  |  1 piece |

## <img src="./IMAGES/A.png" height="40"> Which tools to use
Tool             |  Image|  Comment
:-------------------------:|:----------------------------:|:-------------------------:
[Electric screw driver with 2,5 mm hex bit](https://www.amazon.de/Bosch-Akkuschrauber-Generation-Bits-Ladeger%C3%A4t/dp/B00TTZU566/ref=asc_df_B00TTZU566/?tag=googshopde-21&linkCode=df0&hvadid=255989693737&hvpos=1o1&hvnetw=g&hvrand=6125749874385941808&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9042960&hvtargid=pla-421346020200&psc=1&th=1&psc=1) |<img src="./IMAGES/screwdriver.jpg" width="300"> | For putting the cubes together using M3×12 and M3×8 screws.
[2,5 mm hex key](https://www.amazon.de/Presch-Innensechskant-Satz-Kugelkopf-Innensechskantschl%C3%BCssel/dp/B079V335CR/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2K89GU3MY8P26&keywords=hex+key+set&qid=1575997133&s=diy&sprefix=hex+%2Cdiy%2C160&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRENMU0hKWkJRR0FEJmVuY3J5cHRlZElkPUEwMDIzMjIyMzFBWVIyOEpORU1FSCZlbmNyeXB0ZWRBZElkPUEwMzk0NjQwMlA0NFZDTVk0Tk9LUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) | <img src="./IMAGES/hex-keys.jpg" width="300">| For fine adjustment of all the M3 screws if needed.
[3 mm hex key](https://www.amazon.de/Presch-Innensechskant-Satz-Kugelkopf-Innensechskantschl%C3%BCssel/dp/B079V335CR/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2K89GU3MY8P26&keywords=hex+key+set&qid=1575997133&s=diy&sprefix=hex+%2Cdiy%2C160&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRENMU0hKWkJRR0FEJmVuY3J5cHRlZElkPUEwMDIzMjIyMzFBWVIyOEpORU1FSCZlbmNyeXB0ZWRBZElkPUEwMzk0NjQwMlA0NFZDTVk0Tk9LUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) |↑ | For assembly of the Z-Stage - mounting the gear to the M4 screw.
[1,5 mm hex key](https://www.amazon.de/Presch-Innensechskant-Satz-Kugelkopf-Innensechskantschl%C3%BCssel/dp/B079V335CR/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2K89GU3MY8P26&keywords=hex+key+set&qid=1575997133&s=diy&sprefix=hex+%2Cdiy%2C160&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRENMU0hKWkJRR0FEJmVuY3J5cHRlZElkPUEwMDIzMjIyMzFBWVIyOEpORU1FSCZlbmNyeXB0ZWRBZElkPUEwMzk0NjQwMlA0NFZDTVk0Tk9LUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) |↑↑ | For assembly of the Z-Stage - mounting worm screws.
[Needle-nose Pliers](https://www.amazon.de/Br%C3%BCder-Mannesmann-Telefonzange-gerade-M10948/dp/B003A63EIG/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=needle+nose+pliers&qid=1575997091&s=diy&sr=1-3) |<img src="./IMAGES/pliers.jpg" width="300"> | For assembly of the Z-Stage - inserting the M4 nut.

## <img src="./IMAGES/A.png" height="40">  Assembly
Part - link             |  Result|  Comment
:-------------------------:|:----------------------------:|:-------------------------:
[Baseplates](../../../CAD/ASSEMBLY_Baseplate_v2)|<img src="./IMAGES/baseplates.jpg" width="300">|1× "big" baseplate (4×2), 4× "small" baseplate (4×1), 1× "unit" baseplate (1×1), 1× "unit" baseplate connector (1×1)
[Z-Stage Cube](../../../CAD/ASSEMBLY_CUBE_Z-STAGE_mechanical_v2)|<img src="./IMAGES/z-stage.jpg" width="300">|1× mechanical Z-Stage, Sample Clamp not necessary
[Lens Cubes](../../../CAD/ASSEMBLY_CUBE_Lens_v2)|<img src="./IMAGES/lens.jpg" width="300">| 6× Lens Cube; Write the focal lenghts of the lenses on the holders, so you can always easily find the right one when building the setups.
[Cylindrical Lens Cube](../../../CAD/ASSEMBLY_CUBE_Lens_CYLINDRICAL_v2)|<img src="./IMAGES/CUBE_LENS_CYLINDRICAL_1.jpg" width="300">| 1× Cylindrical Lens Cube
[Sample Cubes](../../../CAD/ASSEMBLY_CUBE_Sample_Holder_v2)|<img src="./IMAGES/sample.jpg" width="300">|5× Sample Holder Cube
[Mirror Cube](../../../CAD/ASSEMBLY_CUBE_Mirror_45_v2)|<img src="./IMAGES/mirror.jpg" width="300">| 1× Mirror Cube
[Flashlight Cube](../../../CAD/ASSEMBLY_Lens_v2)|<img src="./IMAGES/flashlight.jpg" width="300">| 1× Flashlight Cube
[Circular Aperture Cube](../../../CAD/ASSEMBLY_CUBE_Aperture_Circular_v2)|<img src="./IMAGES/CirAp11.jpg" width="300">|2× Circular Aperture Cube
[Laser Cube](../../../CAD/ASSEMBLY_CUBE_Laser_v2)|<img src="./IMAGES/laser.jpg" width="300">|1× Laser Holder Cube and Laser Clamp
[Beam Expander Cube](../../../CAD/ASSEMBLY_CUBE_Beamexpander_v2)|<img src="./IMAGES/beamexpander.jpg" width="300">|1× Beam Expander Cube
[Beamsplitter Cube](../../../CAD/ASSEMBLY_CUBE_Beamsplitter_v2)|<img src="./IMAGES/beamsplitter.jpg" width="300">|1× Beam Expander Cube

## <img src="./IMAGES/E_S.png" height="40"> Done! Great job!
