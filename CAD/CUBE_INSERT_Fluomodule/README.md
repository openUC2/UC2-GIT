# Cube Fluomodule

Basically you want to switch on/off an LED which can not be powered through a GPIO from the Arduino/ESP32. Therfore you have to amplify it using a switch. Best practice is to use a transistor which works non-mechanically, therfore allowing methods like PWM (puls width modulation) in order to dim the intensity (at least seen by the eye). 

The Fluorescent Module arranges a set of star power-LEDS in a darkfield cofiguration which gets mounted on the Z-stage: 
<p align="center">
<img src="./IMAGES/Assembly_Cube_2x1_Z-Stage_Sampleholder.png" width="500">
</p>


Here we rely on the power transistor BD809 which is documented in the following [DATASHEET](http://www.datasheetdir.com/ISCSEMI-BD809+Power-Transistors).


## Wiring
The transistor BD809 is a PNP-transistor where the base directly connects to a digital port of the ESP or Arduino. The transistors pins are arranged like the following (1,2,3 => Base, Collector, Emitter):

<p align="center">
<img src="./IMAGES/ISCSEMI-BD809-pinout.jpg" width="200">
</p>

The wiring can be done as follows:
<p align="center">
<img src="./IMAGES/ESP_LED_circuit.png" width="200">
</p>

The Base (**B**) goes to an arbitrary ESP/Arduino GPIO pin. If you follow the *Blink*-tutorial from the Arduino IDE you should connect the base to *Pin 13*. Then the LED is also blinking

**IMPORTANT**: All parts have to have the same **GND**. Please connect them! 
**IMPORTANT 2**: The power-LEDs usually need lot's of power, so support it with a strong (💪)  power supply! 