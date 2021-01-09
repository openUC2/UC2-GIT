## Electronics

### Wiring of the Raspberry Pi + DMD Module

In order to control the ***DMD DLP2000EVM*** with the Raspberry Pi we followed the nicely written Blog post here: [http://frederickvandenbosch.be/?p=2948](http://frederickvandenbosch.be/?p=2948).
We decided to have a stable wired version using a customized PCB. The wiring follows this chart:

<p align="center">
<img src="./IMAGES/UC2_wiring_DMD.png" width="500">
</p>

We created a PCB design which can directly be used with a Raspberry Pi and the DMD2000EVM module. All EAGLE-files can be found in the folder [ELECTRONICS](.\ELECTRONICS\Piprojector).


The resulting two-sided PCB appears to look like that:

<p align="center">
<img src="./IMAGES/PiProjector_brd_all.png" width="500">
</p>

It can conveniently be ordered through online resources. Ours came from [aisler](https://aisler.net/) and cost 9€:

<p align="center">
<img src="./IMAGES/UC2_pcb_aisler.png" width="500">
</p>




### Assemble the DMD Module

The SIM-setup uses the bare DMD to display images into the sample-plane. This means, that we need to get rid of the LED illumination. Unfortunately the module stops working once the LED is put away from the electronics. Therefore we need to cover it with dark tape.

***1.) Take the DMD Module***
<p align="center">
<img src="./IMAGES/UC2_DMD_1.jpg" width="300">
</p>

***2.) Remove all screws you can find***
<p align="center">
<img src="./IMAGES/UC2_DMD_2.jpg" width="300">
</p>

***3.) Remove the connection flat-band cable***
<p align="center">
<img src="./IMAGES/UC2_DMD_3.jpg" width="300">
</p>

***4.) Disassemble the DMD module***
<p align="center">
<img src="./IMAGES/UC2_DMD_4.jpg" width="300">
</p>

***5.) Mount the DMD module on the 3D printed module and add the cables***
<p align="center">
<img src="./IMAGES/UC2_DMD_5.jpg" width="300">
</p>

***6.) Connnect raspberry pi with DMD platine***
<p align="center">
<img src="./IMAGES/DMDMontage.jpg" width="300">
</p>


