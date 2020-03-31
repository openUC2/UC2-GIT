# LED Matrix

The following gives you a very brief introduction of the workin principle of the low-cost, but versatile LED Matrix. In our version we used the Neopixel Matrix, others might work also.

It can be controlled with an ESP32 or Arduino. The code relies on the Neopixle library, provided by Adafruit Arduion IDE - further information available [here](https://learn.adafruit.com/adafruit-neopixel-uberguide/neomatrix-library).

## LED Matrix (Arduino Nano; I2C)

### Properties
* 8x8 RGB LEDs
* 5V Control Voltage
* WS2812 LED controllers

### Connection Diagram
<p align="center">
<img src="./IMAGES/LED_Matrix_v0_Schaltplan.png" width=500>
</p>

### Schematics
<p align="center">
<img src="./IMAGES/LED_Matrix_v0_Schaltplan2.png" width=500>
</p>

### Wiring
This is how it looks like in a cube
<p align="center">
<img src="./IMAGES/Wiring1.JPG" width=400>
<img src="./IMAGES/Wiring2.JPG" width=400>
</p>

## LED Matrix (ESP32; MQTT)

### Conection pins
```
GND == GND
5V == 5V
DIN == 26
```

## <img src="./IMAGES/W.png" width=40>Code
The code can be found in the [Software GIT](https://github.com/bionanoimaging/UC2-Software-GIT).

## <img src="./IMAGES/Y.png" width=40>Safety
Unplug the power supply when you're not using the LED Matrix!
