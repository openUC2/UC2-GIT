# Cube LED Matrix
This parts adapt a LED matrix to the UC2 cubes. Electric control is done by an ESP32.

<p align="center">
<img src="./IMAGES/Assembly_Cube_LED_Matrix_v0.png" width="600">
</p>

## Purpose
It can be used for Fourier Ptychographic Microscopy (FPM, Horstmeyer 2014), quantitative differential phase-contrast (qDPC, Tian&Waller 2015) or oblique illumination, etc.



## Properties
The basic properties/features of the assembly go here.

## Parts

### 3D printing parts
Here we list the 3D printed components from the ./STL folder

The Part consists of the following components.

1. **The Lid** which holds the ESP32 and the screws which connect to the base-plate (optional: wires can be connected to the screws)
2. **The LED-Matrix Adapter** which adapts to the Neopixel LED Matrix display.


### Additional parts
Here we list all parts which need to be bought from different sources.

|  Name | Properties  |  Price | Link  | # |
|---|---|---|---|---|
|  ESP32 | Microcontroller | 5€  | [ESP](http://esp32.net/)  | 1|
|  DIN912 M3x18 | Screws | 1€  | [Wpürth](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X18/00843%20%2018.sku/de/DE/EUR/)  | 6|
|  Adafruit Neopixel 8x8 | LED Matrix (RGB) | 25€  | [Neopixel](https://www.amazon.de/Adafruit-NeoPixel-NeoMatrix-8x8-64-Matrix/dp/B00FA9JDEU)  | 1|
|  Adafruit Neopixel 8x8 | LED Matrix (RGB) | 25€  | [Neopixel](https://www.amazon.de/Adafruit-NeoPixel-NeoMatrix-8x8-64-Matrix/dp/B00FA9JDEU)  | 1|



## Remarks and Tips

### 3D Printing
Print as is without support. Infill can be around 30%.

### Tricks
You can connect the supply-voltage wires to the screws (5V, Gnd) which can connect to the baseplates' magnets which can eventually also hold power. This makes additional wires obsolete.

### Electronics
Please follow the tutorial of how to handle the LED Matrix in the Adafruit Post [here](https://learn.adafruit.com/adafruit-neopixel-uberguide/neomatrix-library). We connect the LED-array to ```pin 9```.

## Assembly
The assembly of this part is straight forward. Just screw all the parts together to end up here:

<p align="center">
<img src="./IMAGES/step1.jpg" width="600">
</p>

<p align="center">
<img src="./IMAGES/step2.jpg" width="600">
</p>

The ```DIN```, ```5V``` and ```Gnd```-Pin have to be connected to the ESP32. The ESP32 connects to the supply voltage (5V).

## Safety
Take care in case you're dealing with lasers. Don't burn yourself if you solder the part! 
