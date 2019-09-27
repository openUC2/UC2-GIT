## Smartphone Microscope

This is the repository for the Smartphone Microscope.

<p align="center">
<img src="./IMAGES/Assembly_smartphone_microscope_2.png" width="500">
</p>

It's based on a compound microscope which itself relies on finite corrected objective lenses. The Smartphone reimages the image of the ocular onto the camera sensor. This means that the cellphone's camera lens acts like the eye. Proper imaging is achieved if the exit pupil of the eyepiece is matching well with the entrance pupil of the smartphone camera.

Further details can also be found in the *cell-scope* publication by Professor Fletcher at Berkeley. It can also be found on  [their website](https://cellscope.berkeley.edu/).

<p align="center">
<img src="./IMAGES/Assembly_smartphone_microscope.png" width="500">
</p>

The optical path is relying on the finite corrected objective (MO) lens which produces an intermediate image in its tube-length. This image is propagated to infinty by the eyepiece (EP). The smartphone (CAM) expects this image to form an image on the cellphone's camera-sensor. The mirrors (M) are basically just folding the beam, the LED-Array (LA) is giving the opportunity to have different imaging modalities like Dark-, Brightfield or (quantitative) Differential Phase Contrast.

<p align="center">
<img src="./IMAGES/UC2_OpticalPath_Smartphonemicroscope.png" width="300">
</p>

The files contain a fluorescent module which works in darkfield configuration.

## Device's features:

* Z-Focus
* Upright Microscope
* High resoltion
* Open-Source
* Compatible with Educational/Professional fields
* Compatible with almost any smartphone
* Different imaging modalities
* Different illumination modes
* Fluorescent Module enables "true" fluorescent imaging
* The electronics can be operated via WiFi

## 3D printing

Parts to print:

* 1× [Base-plate 4×4](./STL/Assembly_base_4x4.stl)
* 6× [Cube base 1×1](./STL/10_Cube_1x1_v2.stl)
* 7x [Cube lid 1×1](./STL/10_Lid_1x1_v2.stl)
* 1× [Cube base 2×1](./STL/10_Cube_2x1_v2.stl)
* 1× [Cube lid 2×1](./STL/10_Lid_el_2x1_v2.stl)
* 1× [LED Array Holder](./STL/30_Cube_LED_Array_v0.stl)
* 1× [Cube Insert for Eyepiece](./STL/20_Cube_Insert_Holder-okular_v2.stl)
* 1× [Smartphone Holder](./STL/30_Smartphone_Holder.stl)
* 2× [Cube Insert for Mirror - 45°](./STL/20_Cube_Insert_Mirror_Holder_30x30Mirror_v2.stl)
* 1× [Cube Insert for Z-stage](./STL/20_focus_inlet_triangle_spiral_v6_5.stl)
* 1× [Coupling Screw M4](./STL/30_Coupling_Screw_28BYJ_M4.stl)
* Optional: 1× [Z-stage Fluomodule](./STL/30_Z_Stage_Fluomodule_12.stl)
* Optional: 1× [Z-stage Adapterplate](./STL/30_Z_Stage_Adapterplate_11.stl)
* Optional: 1× [Z-stage Clamp for Slides](./STL/40_XY_Stage_Clamp_Slide_9.stl)- current design is for 4 mm magnets!
* Optional: 1× [Generic Clamp for Slides](./STL/30_Sampleclamp_generic.stl)- current design is for 6 mm magnets!

In the end it should look like this:

<p align="center">
<img src="./IMAGES/UC2_Printed_Smartphonemicroscope.jpg" width="300">
<img src="./IMAGES/IMG_20190913_111607.jpg" width="300">
<img src="./IMAGES/IMG_20190913_111620.jpg" width="300">
<br> * Here UC2_v0 parts were used.
</p>

## Additional components
* 1× Smartphone
* 1× LED-Array, Neopixel, 8x8 [🢂](https://www.amazon.de/AZDelivery-Matrix-CJMCU-8-Arduino-Raspberry/dp/B078HYP681/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=neopixel+matrix&qid=1565008576&s=gateway&sr=8-2)
*  32× - 68× 5mm Ball magnets [🢂](https://www.magnetmax.de/Neodym-Kugelmagnete/Magnetkugel-Kugelmagnet-O-5-0-mm-Neodym-vernickelt-N40-haelt-400-g::158.html)
* 32× - 40× Screws DIN912 ISO 4762 M3×12 mm [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* 3× Screws DIN912 ISO 4762 M3×18 mm [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X18/00843%20%2018.sku/de/DE/EUR/)
* 1× Objective Lens (e.g. 10×, NA 0.3) [🢂](https://de.aliexpress.com/item/32947647522.html?spm=a2g0x.search0104.3.54.6cf57a4c3DwsTO&transAbTest=ae803_3&ws_ab_test=searchweb0_0%2Csearchweb201602_6_10065_10130_10068_10890_10547_319_10546_317_10548_10545_10696_10084_453_454_10083_10618_10307_537_536_10902_10059_10884_10887_321_322_10103%2Csearchweb201603_6%2CppcSwitch_0&algo_pvid=06d972be-b176-4446-8665-56d9e61a8d2c&algo_expid=06d972be-b176-4446-8665-56d9e61a8d2c-7)
* 1× Eyepiece (e.g. 20×) [🢂](https://de.aliexpress.com/item/32965050204.html?spm=a2g0o.productlist.0.0.7aa657eeefLUfu&algo_pvid=cd60fca0-3fa5-4191-9ce9-303815e2afa7&algo_expid=cd60fca0-3fa5-4191-9ce9-303815e2afa7-1&btsid=76036b58-6717-4d1f-a4a0-c3d4bacd0450&ws_ab_test=searchweb0_0,searchweb201602_2,searchweb201603_52)
* 2× Mirrors (e.g. 30×30 mm² Toymirrors) [🢂](https://www.amazon.de/Rayher-14548606-Spiegelmosaik-selbstklebend-SB-Btl/dp/B008KJ8438/ref=pd_bxgy_201_img_3/258-8761405-4543762?_encoding=UTF8&pd_rd_i=B008KJ8438&pd_rd_r=80fd534c-997b-4a19-b91a-9bf38dbf4ade&pd_rd_w=4DEXV&pd_rd_wg=7SLRE&pf_rd_p=98c98f04-e797-4e4b-a352-48f7266a41af&pf_rd_r=N95R9S45MNSYNQX2BAJE&psc=1&refRID=N95R9S45MNSYNQX2BAJE)
* 2× ESP32 [🢂](https://www.amazon.de/AZDelivery-NodeMCU-Development-Nachfolgermodell-ESP8266/dp/B074RGW2VQ/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=esp32&qid=1565008313&s=gateway&sr=8-3)
* 1× Cheap Stepper Motor and 1× Controller [🢂](https://www.amazon.de/Elegoo-Stepper-Schrittmotor-28BYJ-48-Treiberplatine/dp/B01MEGIHLF/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=stepper+arduino&qid=1565008205&s=gateway&sr=8-1-spons&psc=1)
* Optional: 2× Star-LEDs blue (high power 1-3 Watt) [🢂](https://www.ebay.de/itm/Hi-Power-LED-1W-3W-UV-STAR-Ultraviolet-/131326525056?var=)
* Optional: 1x MOS-FET/Power PNP Transistor [🢂](https://www.ebay.de/itm/BD809-Transistor-npn-80V-10A-90W-TO220/360661360188?hash=item53f9179e3c:g:ssEAAOSw-fNaqt1l)
* 9× Female-Female Jumper Wire, 0.14 mm² [🢂](https://www.amazon.de/ZOORE-120pcs-Multicolored-Female-Breadboard/dp/B07P85V1G3/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=jumper+male&qid=1565690543&s=industrial&sr=1-5)
* 2× Power cables for ESP32 - USB-microUSB [🢂](https://www.amazon.de/Gritin-Datenkabel-Geflochtene-Robust-Daten%C3%BCbertragung-Grau/dp/B07CJJHVKX/ref=sr_1_3?keywords=usb+c+kabel&qid=1566029225&s=gateway&sr=8-3)

## Assembly

* [Baseplate ](../ASSEMBLY_Baseplate_v2/)
* [Z-stage ](../ASSEMBLY_CUBE_Z-STAGE_v2/)
* 2× [Mirror Cube ](../ASSEMBLY_CUBE_Mirror_45_v2/)
* [Eyepiece Cube ](../ASSEMBLY_CUBE_Eyepiece_v2/)
* [Smartphone holder Cube ](../ASSEMBLY_CUBE_Cellphonemount/)
* [LED array ](../ASSEMBLY_CUBE_LED_Matrix_v2/)
* 2× Additional empty cube

## Electronics (for dummies)

Don't have much experience with electronics? It's actually really simple:

* When using jumper wires you can avoid most of the soldering.
* LED array - 3 wires

<p align="center">
<img src="./IMAGES/Electronics_LED.png" width="300">
</p>
<p align="center">
<img src="./IMAGES/IMG_20190925_163200.jpg" width="300">
</p>

* Z-stage - 6 wires + motor connection

<p align="center">
<img src="./IMAGES/Electronics_Z-stage.png" width="300">
</p>
<p align="center">
<img src="./IMAGES/IMG_20190925_162651.jpg" width="300">
<img src="./IMAGES/IMG_20190925_162730.jpg" width="300">
<img src="./IMAGES/IMG_20190925_162700.jpg" width="300">
</p>

* Power the ESP32 simply with microUSB cables.
* And it works just like that ;-)

## Results
This is a quick result we shot with an Xperia Z5 of potatoe starch cells:
<p align="center">
<img src="./IMAGES/UC2_Result_Potatoe_Smartphonemicroscope.jpeg" width="300">
</p>

## Participate!

Do you want to show your own results? Do you have ideas for improvements? Let us know!
