# Z-Stage (Objective) Cube
This is the repository for the Z-Stage (Objective) Cube.

The stl-files can be found in the folder [STL](./STL).


### Purpose
In microscopy one often needs the ability to move the objective along the optical axis in order to refocus a given 3D sample.
In order to automate this, we designed a very simple z-stage itself reyling on flexure bearings also knwon from Bowman's flexurescope. The main difference here is, that we rely on a spiral-design which avoids the parallel-shift of the objective lens and makes the entire design very robust.

<p align="center">
<img src="./IMAGES/Assembly_Z_Focus_Spiralbearing_v3.png" width="1000">
</p>

***The mechanism is as follows***: A stepper motor (28-BYJ) drives a small gearbox which rotates a screw. On the screw, there is a nut which acts as a worm-drive. The conversion of the rotational into linear movement pushes/pulls a small level-arm which is connected to the spiral spring-like linear actuator. It can thus move up-and down around the resting position.
Another spiral-like spring can hold an objective lens with varying sizes. It also allows coarse z-focussing.  

<p align="center">
<img src="./IMAGES/Assembly_Z_Focus_Spiralbearing_v3_2.png" width="600">
</p>

## Properties
* theoretically no play due to the use of flexure berings
* moving range
	* fine: around +/- 8mm
	* coarse: around +/- 20 mm (shifting the objective lens inside the spiral-like spring
* very low cost by relying on off-the-shelf components

## Parts

### 3D printing parts
The Part consists of the following components.

* **The Lid (2x1)** where the Arduino + Electronics finds its place ([LID](./STL/10_Lid_el_2x1_v2.stl))
* **The Cube (2x1)** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/10_Cube_2x1_v2.stl))
* **The Z-Stage and Motor Holder** which moves the objective and holds the stepper motor ([INSERT](./STL/20_focus_inlet_triangle_spiral_v6.stl))
* **The M4 to Motor Adapter (mech. Coupling)** which connects the Motor directly to an M4 screw which acts as a wormdrive ([SCREW](./STL/30_Coupling_Screw_28BYJ_M4.stl))
* **The Objective Lens Thread Fixer** Kind of a retain ring which pushes the spiral arms closer to the objective lens ([FIXER](./STL/30_focus_inlet_triangle_spiral_fixingring.stl))

For Fluomodule:
* **The Fluomodule** where the LEDs finds their place ([FLUOMODULE](./STL/30_Z_Stage_Fluomodule_12.stl))
* **The Adapterplate** which goes on top and where the slides are placed ([ADAPTERPLATE](./STL/30_Z_Stage_Adapterplate_11.stl))
* **The Clamp for microscope slides** which can fix the slide ([CLAMP](./STL/40_XY_Stage_Clamp_Slide_9.stl))

### Additional parts
* 16x DIN912 M3*12 screws (non stainless steel)
* 1x M4 Nut
* 1x M4 Screw, Hex Head, 26mm
* 1x 28-BYJ stepper motor
* 1x Driving electronic
* 1x ESP32 for controlling the motor
* cables to connect everything


## Remarks and Tips
### 3D Printing:
* No support required in all designs except the sprial focussing mechanism (use sparse support!)
* Carefully remove all support structures (if applicable)

## Assembly
* Detailed description coming soon
* Add motor and small gear, fix it with M4 screw
* Add the M4 nut in the dedicted hole close to the moving stage
* Add M4x26mm screw with mounted large gear at one end and insert it into the hole.
* rotate the M4x26 screw so that it pushes the moving z-stage
* Wire the motor, test it
* Done!


### Tutorial with images (Z-Stage)
This is the assembly guide for the Z-Stage.

1. All parts for this model
<p align="center">
<img src="./IMAGES/Z_STAGE_0.jpg" width="300">
</p>

2. Use pliers to put the M4 nut in the place. Be careful, easy to break here!
<p align="center">
<img src="./IMAGES/Z_STAGE_1.jpg" width="300">
</p>

3. Fix the nut using two M3 worm screws (This can also be done later, in case the nut becomes too wobbly.)
<p align="center">
<img src="./IMAGES/Z_STAGE_3.jpg" width="300">
</p>

4.  Put one end of the M4 screw inside the motor coupling thing- use pliers
<p align="center">
<img src="./IMAGES/Z_STAGE_4.jpg" width="300">
</p>

5.  It should look like this
<p align="center">
<img src="./IMAGES/Z_STAGE_5.jpg" width="300">
</p>

7. Add the other side of the coupling thing to the motor
<p align="center">
<img src="./IMAGES/Z_STAGE_6.jpg" width="300">
</p>

8. Mount the motor to the Z-Stage after putting the M4 screw through the nut (rotate it)
<p align="center">
<img src="./IMAGES/Z_STAGE_7.jpg" width="300">
</p>

9. Fix the Z-Stage within the 2x1 cube using headless M3 screws
<p align="center">
<img src="./IMAGES/Z_STAGE_8.jpg" width="300">
</p>

10. Mount the lid
<p align="center">
<img src="./IMAGES/Z_STAGE_9.jpg" width="300">
</p>

11. Start adding the wires
<p align="center">
<img src="./IMAGES/Z_STAGE_10.jpg" width="300">
</p>

12. Mount the control electronics of the Motor to the Z-stage module
<p align="center">
<img src="./IMAGES/Z_STAGE_11.jpg" width="300">
</p>

13. Screw the lid
<p align="center">
<img src="./IMAGES/Z_STAGE_12.jpg" width="300">
</p>

14. Add the objective lens - optional: Add the ring to fix it permanently
<p align="center">
<img src="./IMAGES/Z_STAGE_13.jpg" width="300">
</p>

15. Add as many screws as possible - Done!
<p align="center">
<img src="./IMAGES/Z_STAGE_14.jpg" width="300">
</p>

### Tutorial with images (Fluomodule+Sample Insert)
This is the assembly guide for the Fluomodule+Sample Insert.
It's tought to work as a darkfield illumination. This reduces any scattering light (e.g. 0th order of the illumination).

1. All parts for this model
<p align="center">
<img src="./IMAGES/Z_STAGE_FLUOMODULE_0.jpg" width="300">
</p>

2. Solder the LEDs to the Transistor; The base of the transistor goes to the ouput of the ESP32, the 5V and GND as well; LEDs are connected in parallel; No resistor necessary. BD809 is connected to the LED in series
<p align="center">
<img src="./IMAGES/Z_STAGE_FLUOMODULE_1.jpg" width="300">
</p>

3. Cut the LEDs and add them to the Fluomodule using either Glue or Blutek
<p align="center">
<img src="./IMAGES/Z_STAGE_FLUOMODULE_2.jpg" width="300">
</p>

4. Sandwich the parts using long M3 screws; Add tape to the Transistor to isolate the wires/open contacts
<p align="center">
<img src="./IMAGES/Z_STAGE_FLUOMODULE_3.jpg" width="300">
</p>

5. Put the Fluomodule to the Z-Stage and cleanup the wires.
<p align="center">
<img src="./IMAGES/Z_STAGE_FLUOMODULE_4.jpg" width="300">
</p>


## Fluorescent Module

The wiring of the fluoresceent module can be found [here](../CUBE_INSERT_Fluomodule). 
## Safety
Be careful!


