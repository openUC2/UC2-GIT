# Electronics (for dummies)

Don't have much experience with electronics? It's actually really simple!

## <a href="#icon01" name="icon01"><img src="./IMAGES/B.png" width="40"></a> Components
* LED-Array, Neopixel, 8x8 [🢂](https://www.amazon.de/AZDelivery-Matrix-CJMCU-8-Arduino-Raspberry/dp/B078HYP681/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=neopixel+matrix&qid=1565008576&s=gateway&sr=8-2)
* ESP32 [🢂](https://www.amazon.de/AZDelivery-NodeMCU-Development-Nachfolgermodell-ESP8266/dp/B074RGW2VQ/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=esp32&qid=1565008313&s=gateway&sr=8-3)
* Stepper Motor and Driver Board [🢂](https://www.amazon.de/Elegoo-Stepper-Schrittmotor-28BYJ-48-Treiberplatine/dp/B01MEGIHLF/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=stepper+arduino&qid=1565008205&s=gateway&sr=8-1-spons&psc=1)
* Female-Female Jumper Wire, 0.14 mm² [🢂](https://www.amazon.de/ZOORE-120pcs-Multicolored-Female-Breadboard/dp/B07P85V1G3/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=jumper+male&qid=1565690543&s=industrial&sr=1-5)
* Power cables for ESP32 - USB-microUSB [🢂](https://www.amazon.de/dp/B0778FV6K4/ref=sr_1_2?dchild=1&fst=as%3Aoff&qid=1586361990&refinements=p_89%3AGritin&rnid=669059031&s=computers&sr=1-2)

## <a href="#icon02" name="icon02"><img src="./IMAGES/A.png" width="40"></a> Connecting the electronics

* When using [jumper wires](http://blog.sparkfuneducation.com/what-is-jumper-wire) you can avoid most of the soldering.

#### **LED array** - 3 wires

<p align="center">
<img src="./IMAGES/Electronics_LED.png" width="300">
</p>

Connect everything - mind the right pins!

* The wires connect to the little trident which goes into the LED array
* Their other ends connect to the ESP32 according to the scheme above

<p align="center">
<img src="./IMAGES/LED01.jpg" width="300">
<img src="./IMAGES/LED02.jpg" width="300">
<img src="./IMAGES/LED03.jpg" width="300">
<img src="./IMAGES/LED04.jpg" width="300">
<img src="./IMAGES/LED05.jpg" width="300">
</p>

#### **Z-stage** or **Sample-stage** - 6 wires + motor connection
* Sample stage is the very same as the Z-stage - you just mount it on different 3Dprinted parts.

<p align="center">
<img src="./IMAGES/Electronics_Z-stage.png" width="300">
</p>

Connect everything - mind the right pins!

* Connect the motor to the driver board
* Two of the wires are for the (+) and (-)
* Four of the wires are for the IN1 - IN4 (inputs)
* Their other ends connect to the ESP32 according to the scheme above

<p align="center">
<img src="./IMAGES/Stage01.jpg" width="300">
<img src="./IMAGES/Stage02.jpg" width="300">
<img src="./IMAGES/Stage03.jpg" width="300">
<img src="./IMAGES/Stage04.jpg" width="300">
<img src="./IMAGES/Stage05.jpg" width="300">
<img src="./IMAGES/Stage06.jpg" width="300">
</p>

* Flash them with the right software from our [Software-GIT](https://github.com/bionanoimaging/UC2-Software-GIT).
* Power the ESP32 simply with microUSB cables.
* And it works just like that ;-)

## Electronics for the SIMPLE smartphone microscope
No control via WiFi - just buttons. The Simple Smartphone Microscope is found [here](../../APPLICATIONS/APP_SIMPLE-Smartphone_Microscope/electronic)

* When using jumper wires you can avoid soldering.
* LED array - 3 wires + 2 wires for the button

<p align="center">
<img src="./IMAGES/Electronics_LED_simple.png" width="300">
</p>

* Z-stage - 6 wires + motor connection + 2×2 wires for two buttons

<p align="center">
<img src="./IMAGES/Electronics_Z-stage_simple.png" width="300">
</p>

* The buttons are simply an add-on to the Electronics - connect to wires to each button and to the correct pins of the ESP32
<p align="center">
<img src="./IMAGES/Stage07.jpg" width="300">
<img src="./IMAGES/Stage08.jpg" width="300">
<img src="./IMAGES/Stage09.jpg" width="300">
<img src="./IMAGES/Stage10.jpg" width="300">
</p>


* Power the ESP32 simply with microUSB cables.
* And it works just like that ;-)

Further advice:  
[But I don't have such wires...](https://www.youtube.com/watch?v=VB1CrqY_jMg)  
[But how to connect two wires to the same pin?](https://www.youtube.com/watch?v=8W-zdo1AVns)
