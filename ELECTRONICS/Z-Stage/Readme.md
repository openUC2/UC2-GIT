# Code for the XY-STAGE

The electronics part of this project is quiete simple. We only need two motors which drive the Z-stages for the microscope objective lens and the sample stage. We rely on the well-known 28BYJ-48 Stepper motor which operates at 5V and has up to 4096 steps per revolution. It comes with a motor driver ([TI ULN2003](http://www.ti.com/lit/ds/symlink/uln2003a.pdf)) which converts a 4-wire input signal into the 5-wire output signal necessary for the bipolar stepper motor. Further resources can be found [here](http://www.hobby-werkstatt-blog.de/arduino/357-schrittmotor-28byj48-am-arduino.php). 

In order to let the motor spin in both directions with different speed, we need to generate a signal which has a specific order of high/low pulses for each channel. Therefore we use a microcontroller (ESP32 DEV) which can conveniently be programmed in the Arduino IDE (see programming section).


## Wiring
The wiring of the electronic setup is fairly simple. We just need to connect each input-channel of the motor-controller board to an output of the ESP microcontroller. Additionally we need to connect the power of both  controllers (i.e. +5V, GND). In general we could use any of the output-pins of the ESP32, but here we use the following:


```
Motor 1 = 13,12,14,27
Motor 2 = 26,25,23,32
```
	
They connect to the IN1, IN2, IN3, IN4 of the motor controller as indicated below:

![xypins](./IMAGES/Z_Stage_ESP_v0_Schaltplan.png)

## Soldering

The process of connecting the motors to the ESP is again a relatively easy job. One only need to solder a set of wires from the output-pins of the ESP to the input pins of the ULN2003 motor controller. Therefore one should follow these steps:

* Taking 10 wires and cut them to around 100 mm
* Remove the isolation of each wire at both sides
* Add some lead to both sides using the solder iron
* Solder the wires to the electronic parts 

If everything went correct, the entire circuit should look like the lower photograph. 

Step 1: Remove the isolation of the wires
![xypins](./IMAGES/UC2_Soldering_stage_1.jpg)

Step 2: Add some lead to the tips of the short wires and solder them to both sides of the ESP and ULN2003. 
![xypins](./IMAGES/UC2_Soldering_stage_2.jpg)

Stept 3: Finish the setup using and flash the example program to the ESP so that both motors move back-and-forth
![xypins](./IMAGES/UC2_Soldering_stage_3.jpg)


	
## Code 
The code can also be found in the folder [code](./CODE).

The code need to flashed using the Arduino IDE using the ESP32 library. Further information can be found in this handy tutorial for integrating the ESP in the Arduino environment: [Arduino ESP Tutorial](https://randomnerdtutorials.com/getting-started-with-esp32/)

## NOTES
Make sure you're releasing the Motor after usage, otherwise it can get quiet hot!

 