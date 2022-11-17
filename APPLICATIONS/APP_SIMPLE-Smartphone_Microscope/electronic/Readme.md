# Simple Smartphone Microscope - version with electronics

This is the repository for the simple electronic version of the [Smartphone Microscope](../../APP_SMARTPHONE_MICROSCOPE).

This microscope and the code for the ESP32 is a work of students from KL-Gymnasium in Erfurt. It was updated to the v3 version by UC2 core team.

<p align="center">
<img src="../IMAGES/Application_smartphone_microscope_v3.png" width="500">
</p>


## <img src="../IMAGES/F.png" width="40">Devices' features:
* Simple microscope for smartphone imaging
* Manual alignment helps to understand the principle of a microscope
* Teaching the basics of electronics that are needed for more advanced setups

## <img src="../IMAGES/D.png" width="40">Parts
The [Bill of Materials](https://docs.google.com/spreadsheets/d/1U1MndGKRCs0LKE5W8VGreCv9DJbQVQv7O6kgLlB6ZmE/edit?usp=sharing) is always the most up-to-date version!

### Modules for this setup

|  Name | Properties  |  Price | Link  | # |
|---|---|---|---|---|
|  Baseplate puzzle| - | 5€  | [Base-plate](../../../CAD/ASSEMBLY_Baseplate/)  | 8|
|  Module: Z-Stage | -  | ?? €  | [Z-Stage](../../../CAD/ASSEMBLY_CUBE_Z-STAGE_objective)  | 1|
|  Module: Sample holder | -  | 5 €  | [Sample holder](../../../CAD/ASSEMBLY_CUBE_Sample_Holder)  | 1|
|  Module: Mirror 45°  | - | 5€  | [Mirror 45](../../../CAD/ASSEMBLY_CUBE_Mirror_45)  | 2|
|  Module: Eyepiece with Smartphone Holder  | - | ??€  | [Eyepiece + Smartphone](../../../CAD/ASSEMBLY_CUBE_Eyepiece)  | 1|
|  Module: LED array (simple)  | -| ??€  | [LED array](../../../CAD/ASSEMBLY_CUBE_LED_Matrix_simple)  | 1|
|  Module: Empty Cube  | For stability of the setup, it is better to fill the empty positions under other cubes. | 4€  | [Cube](../../../CAD/ASSEMBLY_CUBE_Base)  | 2|


### <img src="../IMAGES/P.png" width="40"> 3D-printing
To acquire the STL-files use the [UC2-Configurator](https://uc2configurator.netlify.app/). The files themselves are in the [RAW](../../../CAD/RAW/STL) folder. The module can be built using injection-moulded (IM) or 3D-printed (3DP) cubes. Choose the APP_Smartphone microscope for this one.

In the end it should look like this (UC2_v2 cubes displayed):

<p align="center">
<img src="../IMAGES/UC2_simple_smartphone_microscope.jpg" width="300">
</p>

## <img src="../IMAGES/B.png" width="40"> Additional components
* Check out the [RESOURCES](../../../TUTORIALS/RESOURCES) for more information!
* 1× Smartphone
* 1× LED-Array, Neopixel, 8x8 [🢂](https://www.amazon.de/AZDelivery-Matrix-CJMCU-8-Arduino-Raspberry/dp/B078HYP681/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=neopixel+matrix&qid=1565008576&s=gateway&sr=8-2)
*  36× - 68× 5mm Ball magnets [🢂](https://www.magnetmax.de/Neodym-Kugelmagnete/Magnetkugel-Kugelmagnet-O-5-0-mm-Neodym-vernickelt-N40-haelt-400-g::158.html)
* 36× - 72× Screws DIN912 ISO 4762 M3×12 mm [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* 1× M3×30 mm and M3 nut - non-magnetic
* 1× Objective Lens (e.g. 10×, NA 0.25) [🢂](https://de.aliexpress.com/item/4000427537503.html?algo_pvid=92c2046d-1afb-4c61-ad4d-c8a3535074dc&algo_exp_id=92c2046d-1afb-4c61-ad4d-c8a3535074dc-0&pdp_ext_f=%7B%22sku_id%22%3A%2210000001769780334%22%7D&pdp_npi=2%40dis%21EUR%2114.77%2110.93%21%21%21%21%21%402100bddb16687215483344070eb889%2110000001769780334%21sea&curPageLogUid=1lQjdJdA4gbN)
* 1× Eyepiece (e.g. 20×) [🢂](https://de.aliexpress.com/item/32897739739.html?spm=a2g0o.productlist.0.0.93247063HYrXWu&algo_pvid=15d023df-ea13-4776-a189-0ea3cfeb68b1&algo_exp_id=15d023df-ea13-4776-a189-0ea3cfeb68b1-0&pdp_ext_f=%7B%22sku_id%22%3A%2266133519978%22%7D&pdp_npi=2%40dis%21EUR%2129.83%2123.27%21%21%21%21%21%402100bddb16687214308061806eb889%2166133519978%21sea&curPageLogUid=4A4h71YgdLsm)
* 2× Mirrors (e.g. 30×30 mm² Toymirrors) [🢂](https://www.amazon.de/Rayher-14548606-Spiegelmosaik-selbstklebend-SB-Btl/dp/B008KJ8438/ref=pd_bxgy_201_img_3/258-8761405-4543762?_encoding=UTF8&pd_rd_i=B008KJ8438&pd_rd_r=80fd534c-997b-4a19-b91a-9bf38dbf4ade&pd_rd_w=4DEXV&pd_rd_wg=7SLRE&pf_rd_p=98c98f04-e797-4e4b-a352-48f7266a41af&pf_rd_r=N95R9S45MNSYNQX2BAJE&psc=1&refRID=N95R9S45MNSYNQX2BAJE)
* 2× ESP32 [🢂](https://www.amazon.de/AZDelivery-NodeMCU-Development-Nachfolgermodell-ESP8266/dp/B074RGW2VQ/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=esp32&qid=1565008313&s=gateway&sr=8-3)
* 1× Stepper Motor and 1× Driver Board [🢂](https://www.amazon.de/Elegoo-Stepper-Schrittmotor-28BYJ-48-Treiberplatine/dp/B01MEGIHLF/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=stepper+arduino&qid=1565008205&s=gateway&sr=8-1-spons&psc=1)
* 3× Button [🢂](https://www.az-delivery.de/products/button-modul?_pos=2&_sid=f2080c1b0&_ss=r)
* 15× Female-Female Jumper Wire, 0.14 mm² [🢂](https://www.amazon.de/ZOORE-120pcs-Multicolored-Female-Breadboard/dp/B07P85V1G3/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=jumper+male&qid=1565690543&s=industrial&sr=1-5)
* 2× Power cables for ESP32 - USB-microUSB [🢂](https://www.amazon.de/dp/B0778FV6K4/ref=sr_1_2?dchild=1&fst=as%3Aoff&qid=1586361990&refinements=p_89%3AGritin&rnid=669059031&s=computers&sr=1-2)


## <img src="../IMAGES/A.png" width="40"> Assembly
For assembly instructions of the respective modules refer to the links in Modules for this setup.

## <img src="../IMAGES/L.png" width="40"> Electronics (for dummies)

Don't have much experience with electronics? It's actually really simple:

* When using jumper wires you can avoid soldering.
* LED array - 3 wires + 2 wires for the button

<p align="center">
<img src="../IMAGES/Electronics_LED_simple.png" width="300">
</p>

* Z-stage - 6 wires + motor connection + 2×2 wires for two buttons

<p align="center">
<img src="../IMAGES/Electronics_Z-stage_simple.png" width="300">
</p>

* Power the ESP32 simply with microUSB cables.
* And it works just like that ;-)

## <img src="../IMAGES/W.png" width="40"> Code
In the [CODE](./CODE) folder you find the code for both the [LED array](./CODE/ESP32_ledarr_simple) and [Z-stage](./CODE/ESP32_z_motor_simple).

Have a look in the [TUTORIALS](../../../TUTORIALS) for a beginners guide to UC2 hardware controls.

Prerequisities:
* [Arduino IDE](https://www.arduino.cc/en/main/software) installed
* ESP32 libraries - [Installation guide here](https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/)
* [FastLED.h](https://www.arduinolibraries.info/libraries/fast-led) library

## <img src="../IMAGES/E.png" width="40"> Results
<p align="center">
<img src="../IMAGES/UC2_simple_smartphone_microscope_class.jpeg" height="250">
<img src="../IMAGES/UC2_simple_smartphone_microscope_results.jpeg" height="250">
<br>
Right: Smartphone microscope during the classroom experiments; left: Red onion cells, the nucleus visible in the center
</p>

**Where next?**  
Find out more about the smartphone microscope in the [SimpleBOX manuals](../../../TheBOX/SimpleBOX/DOCUMENTS)  
Find out more about the electronics in the [Electronics section](../../../ELECTRONICS)  
Find out more about the software for this setup in our dedicated [UC2-Software-GIT](https://github.com/bionanoimaging/UC2-Software-GIT)   

### It seems that you went successfully through all the [TUTORIALS](../../../TUTORIALS). Now you're a skilled UC2 builder!

## <img src="../IMAGES/S.png" width="40"> Participate!

Do you want to show your own results? Do you have ideas for improvements? Let us know!
