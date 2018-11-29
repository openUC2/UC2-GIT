## Magnetic Connectors 

The following part is only for the pupose of convenience. A few components, such as the xyz stage or the illumination have inbuilt electronics. Control is achieved through a 4-wired IC2 BUS. In order to make it work, the electronical components have to be connected to 5V, Gnd, CLK and DATA. 

This can be done be a simple wired connection or alternatively with a set of magnetic connectors to be in-line with the general system design. The CAD files are based on parts which can - so far - only be ordered overseas. 

## Link to order the components
You can find the parts [here](https://www.alibaba.com/product-detail/Hytepro-usb-panel-mount-magnetic-pogo_60802915253.html?spm=a2700.7724857.normalList.2.78171d18RHvp0G&s=p). 
They come in pairs.

## POGO Pins (male/female)
Some images from their website:
![Schematics](./images/PogoPins_1.png)

## Setup
The Pogo pins go inside the 3D printed parts. One for the back-plate, one for the cube's lid. There are dedicated holes which makes the process of assembly quiet easy (No possibility to put it in the wrong place). 

Additionally, the back-plate holds the "female" version of these magnetic adapters, which don't have the spring loaded contacts. The "male" version goes inside the cube.

## Wiring 
If you hold the cube right in front of you and you're facing the bare metal contacts (spring loaded pins), then the left one holds 5V, right one stands for GND. The back-plate goes the same way, so that correct wiring is assured.

```
This is a cube from the back side
-----------------------
|					  |
|					  |
|					  |
|					  |
|					  |
|					  |
|5V - Clk - Data - Gnd|
-----------------------
```

## Soldering
The soldering is quiet easy. Simply put some wires to the end of the Pogo-Pin connectors like that:

![Schematics](./images/PogoPins_2.png)

## Properties
	- 4 pins
	- magnetic (600g)
	
	
## NOTES
Make sure you're releasing the Motor after usage, otherwise it can get quiet hot!

