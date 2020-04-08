# Cube LED Matrix - simple version
([TUT03 of TUTORIALS](../../../TUTORIALS) )  
This is a subsection of the repository for the [Cube LED Matrix](../).

This parts adapt an LED matrix to the UC2 cube. Electric control is done by an ESP32.

The stl-files can be found in the folder [STL](../STL).

<p align="center">
<img src="../IMAGES/Assembly_Cube_LED_Matrix_v0.png" width="600">
</p>

## Purpose
The LED matrix serves as a light source. Using the code you find in [CODE](./CODE) you can change the illumination intensity by simply clicking the button and going through three different brightness level.

## <img src="../IMAGES/D.png" height="40">Parts

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

1. **The Lid** that connect to the magnetic baseplate ([LID](../STL/10_Lid_1x1_el_v2.stl))
2. **The LED-Matrix Adapter** which adapts to the Neopixel LED Matrix display. ([ADAPTER](../STL/20_Cube_insert_LED_holder.stl))


### <img src="../IMAGES/B.png" height="40"> Additional parts
* 4× DIN912 M3×12 screws (galvanized steel) [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* 2× M2 screws with nuts for connecting the LED matrix to the adapter, alternatively use hot glue
* 1× ESP32 [🢂](https://www.amazon.de/AZDelivery-NodeMCU-Development-Nachfolgermodell-ESP8266/dp/B074RGW2VQ/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=esp32&qid=1565008313&s=gateway&sr=8-3)
* 1× LED-Array, AZ Delivery, 8x8 [🢂](https://www.amazon.de/AZDelivery-Matrix-CJMCU-8-Arduino-Raspberry/dp/B078HYP681/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=neopixel+matrix&qid=1565008576&s=gateway&sr=8-2)
* 1× Button [🢂](https://www.az-delivery.de/products/button-modul?_pos=2&_sid=f2080c1b0&_ss=r)
* 5× Female-Female Jumper Wire, 0.14 mm² [🢂](https://www.amazon.de/ZOORE-120pcs-Multicolored-Female-Breadboard/dp/B07P85V1G3/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=jumper+male&qid=1565690543&s=industrial&sr=1-5)
* 1× Power cable for ESP32 - USB-microUSB [🢂](https://www.amazon.de/Gritin-Datenkabel-Geflochtene-Robust-Daten%C3%BCbertragung-Grau/dp/B07CJJHVKX/ref=sr_1_3?keywords=usb+c+kabel&qid=1566029225&s=gateway&sr=8-3)

## <img src="../IMAGES/A.png" height="40"> Assembly


## <img src="../IMAGES/L.png" height="40">Electronics
Careful - open electronic contact can cause shortcuts!

Don't have much experience with electronics? It's actually really simple:

* When using jumper wires you can avoid soldering.
* LED array - 3 wires + 2 wires for the button

<p align="center">
<img src="../IMAGES/Electronics_LED_simple.png" width="300">
</p>

### Tutorial with images
      This tutorial needs an update!

1. All parts for this model
<p align="center">
<img src="../IMAGES/CUBE_LED_MATRIX_1.jpg" width="300">
</p>

2. Solder the 3xpinhead to the LED-Matrix
<p align="center">
<img src="../IMAGES/CUBE_LED_MATRIX_2.jpg" width="300">
</p>

3. Add the pinheads to the ESP32
<p align="center">
<img src="../IMAGES/CUBE_LED_MATRIX_3.jpg" width="300">
</p>

4. Solder everything
<p align="center">
<img src="../IMAGES/CUBE_LED_MATRIX_4.jpg" width="300">
</p>

5. Connect 5V, GND and Data from ESP32 to Neopixel Array using Female-Female jumpers
<p align="center">
<img src="../IMAGES/CUBE_LED_MATRIX_5.jpg" width="300">
</p>

6. Add Lid and Screws - Done!
<p align="center">
<img src="../IMAGES/CUBE_LED_MATRIX_6.jpg" width="300">
</p>

6. Mount everything
<p align="center">
<img src="../IMAGES/CUBE_LED_MATRIX_7.jpg" width="300">
</p>

## <img src="../IMAGES/W.png" width="40"> Code
In the [CODE](./CODE) folder you find a simple code for the [LED array](./CODE/ESP32_ledarr_simple).

Have a look in the [TUTORIALS](../../../TUTORIALS) for a beginners guide to UC2 hardware controls.

Prerequisities:
* [Arduino IDE](https://www.arduino.cc/en/main/software) installed
* ESP32 libraries - [Installation guide here](https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/)
* [FastLED.h](https://www.arduinolibraries.info/libraries/fast-led) library

**Where next?**  
Find out more about the electronics in the [Electronics section](../../../ELECTRONICS)  
Find out more about the code for this part in our dedicated [UC2-Software-GIT](https://github.com/bionanoimaging/UC2-Software-GIT)   
Or return to the [TUTORIALS](../../../TUTORIALS)

## <img src="../IMAGES/S.png" width="40"> Participate!

Do you want to show your own results? Do you have ideas for improvements? Let us know!
