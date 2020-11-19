# Michelson Interferometer

We built our Michelson interferometer using 3D printed, low-cost UC2 cube blocks and optical components. In the next chapters, you will find basic information about Michelson Interferometer, setup diagram, necessary UC2 modules, printing details, additional components, assembling contents and final results of our UC2- Michelson Interferometer setup.



_Michelson Interferometer_ is an optical interferometer which measures some factors of light beams such as length, surface irregularities, and refraction index. It is used for testing lenses or prisms, measuring refraction index or minute details of surfaces in optical industry.

<p align="center">
<img src=".\IMAGES\UC2_Setups_8_michelson.png"
width="450">
</p>

The basic mechanism is that Beam-splitter module divides an incoming light beam into two beams, one is transmitted to a fixed mirror and the other is reflected to a movable mirror. Then two beams are reflected by these mirrors (M1 and M2) and interfere with each other with adding or subtracting in Beam-splitter cube.This interference generates a pattern which includes interference fringes of light and dark lines.
Moving screws of the Diagonal Kinematic Mirror Holder cube provides flexibility to interfere two reflected beams in the beam-splitter easily.
In the Results section, interference pattern image of the test setup can be seen.  



<p align="center">
<img src=".\IMAGES\Application_Michelson-Interferometer_v2.png"
width="450">
</p>

### 3D-printed components
### Modules for this setup

|  Name | Properties  |  Price | Link  | # |
|---|---|---|---|---|
|  4×4 Baseplate | - | 5€  | [Base-plate](../../CAD/ASSEMBLY_Baseplate_v2/)  | 1|
|  Module: Laser | - | 18,40 €  | [LASER](../../CAD/ASSEMBLY_CUBE_Laser_v2)  | 1|
|  Module: Beam Expander | It expands incoming laser beam  | 12,10 €  | [Beam Expander](../../CAD/ASSEMBLY_CUBE_Beamexpander_v2)  | 1|
|  Module: Beam Splitter | It splits incoming light beam into two beams and reunites reflected two beams. | 29,20 €  | [Beam Splitter](../../CAD/ASSEMBLY_CUBE_Beamsplitter_v2)  | 1|
|  Module: Kinematic Mirror Holder Cube - Diagonal | For better interference of reflected beams in the Beam-splitter cube. | 4,71 €  | [ Kinematic Mirror 45](../../CAD/ASSEMBLY_CUBE_Mirror_Kinematic_45_v2)  | 1|
|  Module: Kinematic Mirror | - | 9,22 €  | [ Kinematic Mirror](../../CAD/ASSEMBLY_CUBE_Mirror_Kinematic_v2)  | 2|
|  Module: Raspberry Camera  | - | 33,70 €  | [RasPi Camera](../../CAD/ASSEMBLY_CUBE_RaspiCam_v2)  | 1|
|  Module: Empty Cube  | For stability of the setup, it is better to fill the empty positions under other cubes. | 4,40 €  | [Cube](../../CAD/ASSEMBLY_CUBE_Base_v2)  | 2|


### <img src="./IMAGES/P.png" width="40">Parts to print

* 1× [Base-plate 4×4](./STL/Assembly_base_4x4.stl)
* 8× [Cube base 1×1](./STL/10_Cube_1x1_v2.stl)
* 8x [Cube lid 1×1](./STL/10_Lid_1x1_v2.stl)
* 2x [Laser Holder](./STL/20_Cube_Insert_Laser_Mount.stl)
* 1x [Laser Holder Clamp](./STL/00_Laser_Clamp_OnOffSwitch.stl)
* 1× [Lens Adapter for Beam Expander](./STL/30_Lens_Adapter_Beamexpander.stl)
* 1× [Beam Splitter](./STL/20_Cube_Insert_Beamsplitter.stl)
* 1× [RasPi Camera](./STL/20_Cube_Insert_RaspiCam.stl)
* 1× [Cube Insert for Mirror - 45°](./STL/20_Cube_Insert_Kinematic_Mirrormount_45_base.stl)
* 2× [Cube Insert for Kinematic Mirror](./STL/20_Cube_Insert_Kinematic_Mirrormount_base.stl)

At the end it will look like this:

<p align="center">
<img src=".\IMAGES\Application_Michelson-Interferometer_v2_2.png"
width="450">
</p>


## <img src="./IMAGES/B.png" width="40"> Additional components
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
*  32× - 68× 5mm Ball magnets [🢂](https://www.magnetmax.de/Neodym-Kugelmagnete/Magnetkugel-Kugelmagnet-O-5-0-mm-Neodym-vernickelt-N40-haelt-400-g::158.html)
* 32× - 42× Screws DIN912 ISO 4762 M3×12 mm [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* 1× M3×30 mm and M3 nut - non-magnetic
* 3× Mirrors (e.g. 30×30 mm² Toymirrors) [🢂](https://www.amazon.de/Rayher-14548606-Spiegelmosaik-selbstklebend-SB-Btl/dp/B008KJ8438/ref=pd_bxgy_201_img_3/258-8761405-4543762?_encoding=UTF8&pd_rd_i=B008KJ8438&pd_rd_r=80fd534c-997b-4a19-b91a-9bf38dbf4ade&pd_rd_w=4DEXV&pd_rd_wg=7SLRE&pf_rd_p=98c98f04-e797-4e4b-a352-48f7266a41af&pf_rd_r=N95R9S45MNSYNQX2BAJE&psc=1&refRID=N95R9S45MNSYNQX2BAJE)
* 1x Green Laser [🢂](https://www.laserlands.net/11051047.html)
* 1× RasPi Camera [🢂](https://www.amazon.de/Raspberry-Pi-v2-1-1080P-Kamera-Modul/dp/B01ER2SMHY/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1LUZK9XHFS5CX&keywords=raspberry+pi+camera+v2.1&qid=1565008837&s=gateway&sprefix=raspberry+pi+camera+%2Caps%2C163&sr=8-4)
* 1× RasPi Camera long cable [🢂](https://www.amazon.de/gp/product/B075JN61S7/ref=ox_sc_act_title_2?smid=A1X7QLRQH87QA3&psc=1)
* 2× M2 screw + nut [🢂](https://www.amazon.de/Edelstahl-Sechskopf-Knopf-Schrauben-Unterlegscheiben-Sortiment-Aufbewahrung/dp/B073SS7D8J/ref=sr_1_fkmr0_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=zylinderkopfschrauben+set+galvanisiert&qid=1565007371&s=diy&sr=1-1-fkmr0)
* 1x Iphone Lens [🢂](https://www.ebay.com/c/7029261375)
* 1x Planoconvex Lens f'=26,5mm, 18 mm (551.OAL)[🢂](https://www.pgi-versand.de/?id=47&mode=artdet&artnr=551.OAL)
* 1x Beamsplitter Cube (Art. 2137) [🢂](https://optikbaukasten.de/)


## <img src="./IMAGES/A.png" width="40"> Assembly

* 1x [Baseplate ](../../CAD/ASSEMBLY_Baseplate_v2/)
* 2× [Mirror Cube ](../../CAD/ASSEMBLY_CUBE_Mirror_45_v2/)
* 2× [Additional empty cube](../../CAD/ASSEMBLY_CUBE_Base_v2)
* 1x [LASER cube](../../CAD/ASSEMBLY_CUBE_Laser_v2)
* 1x [Beam-expander cube](../../CAD/ASSEMBLY_CUBE_Beamexpander_v2)
* 1x [Beam-Splitter cube](../../CAD/ASSEMBLY_CUBE_Beamsplitter_v2)
* 1x [Diagonal Kinematic Mirror Holder Cube](../../CAD/ASSEMBLY_CUBE_Mirror_Kinematic_45_v2)
* 2x [Kinematic Mirror Holder Cube ](../../CAD/ASSEMBLY_CUBE_Mirror_Kinematic_v2)
* 1x [RasPi Camera Cube](../../CAD/ASSEMBLY_CUBE_RaspiCam_v2)


## <img src="./IMAGES/E.png" width="40"> Results
We built Michelson Interferometer using injection molding UC2 cubes. Experiment setup looks:
<p align="center">
<img src="./IMAGES/Michelson 2.JPG" width="300">
</p>

<p align="center">
<img src="./IMAGES/Michelson .JPG" width="300">
</p>

Interference pattern looks like:

<p align="center">
<img src="./IMAGES/Michelson 3.jpg" width="300">
</p>

## Suggestions

We are really happy to see you there. If you have any problems or new ideas, please try it or suggest us! We are an open-source project and ready to hear new voices :hugs:
