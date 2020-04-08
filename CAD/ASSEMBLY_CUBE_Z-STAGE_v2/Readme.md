# Z-Stage (Objective) Cube
This is the repository for the Z-Stage (Objective) Cube.

The stl-files can be found in the folder [STL](./STL).

## Purpose
In microscopy one often needs the ability to move the objective along the optical axis in order to refocus a given 3D sample.
In order to automate this, we designed a very simple z-stage itself relying on flexure bearings also known from Bowman's flexurescope.

<p align="center">
<img src="./IMAGES/Assembly_Z_Focus_Linearbearing_v0_with_fluomodule.png" width="300">
</p>

**The mechanism is the following:**

**Course movement:** The objective is mounted on a ring which has a screw on one side and the screw head is inserted in a slot in the focussing insert. The movement range for this is 35 mm - the full length of th slot.
<p align="center">
<img src="./IMAGES/Z-stage_principle_01.jpg" width="300">
<img src="./IMAGES/Z-stage_principle_02.jpg" width="300">
<img src="./IMAGES/Z-stage_principle_03.jpg" width="300">
</p>

**Fine movement:** For fine focussing the linearbearing lever is moved by (in this case) a step-motor. When the screw pushes or pulls the lever, due to a rotation of the motor, the objective mount moves with it.
<p align="center">
<img src="./IMAGES/Z-stage_principle_04.jpg" width="300">
<img src="./IMAGES/Z-stage_principle_05.jpg" width="300">
<img src="./IMAGES/Z-stage_principle_06.jpg" width="300">
</p>

### Properties
* theoretically no play due to the use of flexure bearings
* moving range
	* fine: around +/- 6 mm
	* coarse: around 30 mm (shifting the objective lens inside the slot)
* very low cost by relying on off-the-shelf components

## Parts

### <img src="../IMAGES/P.png" height="40"> 3D printing parts
* No support needed in all designs
* Carefully remove all support structures (if applicable)

The Cube consists of the following components.

* **The Lid (2x1)** where the Arduino + Electronics finds its place ([LID](./STL/10_Lid_el_2x1_v2.stl))
* **The Cube (2x1)** which will be screwed to the Lid. Here all the functions (i.e. Mirrors, LED's etc.) find their place ([BASE](./STL/10_Cube_2x1_v2.stl))
* **The Z-Stage and Motor Holder** which moves the objective and holds the stepper motor ([INSERT](./STL/20_focus_inlet_linearflexure_v0.stl))
* **The M3 to Motor Adapter (mech. Coupling)** which connects the Motor directly to an M3 screw which acts as a wormdrive ([SCREW](./STL/30_Coupling_Screw_28BYJ_M3.stl))
* **The Objective Lens Mount** which holds the objective and allows for coarse movement ([OBJECTIVE MOUNT](./STL/30_focus_inlet_objective_mount_v7.stl))

For Fluomodule:
* **The Fluomodule** where the LEDs finds their place ([FLUOMODULE](./STL/30_Z_Stage_Fluomodule_12.stl))
* **The Adapterplate** which goes on top and where the slides are placed ([ADAPTERPLATE](./STL/30_Z_Stage_Adapterplate_11.stl))
* **The Clamp for microscope slides** which can fix the slide ([CLAMP](./STL/40_XY_Stage_Clamp_Slide_9.stl))

### <img src="./IMAGES/B.png" height="40"> Additional parts
* 10× - 20× DIN912 M3×12 screws (galvanized steel) [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)
* 2× DIN912 M3×8 screws (galvanized steel)
* 2× DIN912 M3×18 screws (galvanized steel)
* 1× M3 Nut
* 1× M3 Screw, 30 mm or longer (non-magnetic)
* 1× 28-BYJ stepper motor with 1x Driving electronic [🢂](https://www.amazon.de/Elegoo-Stepper-Schrittmotor-28BYJ-48-Treiberplatine/dp/B01MEGIHLF/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=stepper+arduino&qid=1565008205&s=gateway&sr=8-1-spons&psc=1)
* 1× ESP32 for controlling the motor [🢂](https://www.amazon.de/AZDelivery-NodeMCU-Development-Nachfolgermodell-ESP8266/dp/B074RGW2VQ/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=esp32&qid=1565008313&s=gateway&sr=8-3)
* wires to connect everything; for example: 6× Female-Female Jumper Wire, 0.14 mm² [🢂](https://www.amazon.de/ZOORE-120pcs-Multicolored-Female-Breadboard/dp/B07P85V1G3/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=jumper+male&qid=1565690543&s=industrial&sr=1-5)
* 1× USB Micro Cable [🢂](https://www.amazon.de/Gritin-Datenkabel-Geflochtene-Robust-Daten%C3%BCbertragung-Grau/dp/B07CJJHVKX/ref=sr_1_3?keywords=usb+c+kabel&qid=1566029225&s=gateway&sr=8-3)

For fluomodule:
* 2× LED
* PNP-transistor BD809
* 4× DIN912 M3×18 screws (non stainless steel)
* 4× ballmagnets, 5 mm diameter
* wires to connect everything


## <img src="./IMAGES/A.png" height="40"> Assembly

### Tutorial with images (Z-Stage)
This is the assembly guide for the Z-Stage.

1. All parts for this model. The electronics comes later.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_01.jpg" width="300">
</p>

1. Insert the motor into the motor-screw-coupling adapter.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_02.jpg" width="300">
</p>

1. Insert the head of the M3×20 screw into the motor-screw-coupling adapter. Use pliers to press the screw inside.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_03.jpg" width="300">
</p>

1.  Fix the head of the M3 screw inside the adapter using two M3 worm screws (This can also be done later, in case the screw becomes too wobbly.) You may fix the motor-end the same way, if needed.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_04.jpg" width="300">
</p>

1.  The M3 nut goes into the level of the Z-stage.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_05.jpg" width="300">
</p>

1. We will fix the nut inside the lever using two M3×8 screw. Firstly, insert one screw but only enough to not fall out for now. Use a hex key through the hole in the side of the Z-stage to tighten this screw.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_06.jpg" width="300">
</p>

1. Add the screw to the opposite side. The screws must not hold the nut inside yet! Make sure the screws are tight enough not to fall out and then remove the nut.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_07.jpg" width="300">
</p>

1. Screw the M3 nut on the M3×20 screw, which is attached to the motor. The optimal position for the nut is roughly one third of the length of the screw from the couling adapter.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_08.jpg" width="300">
</p>

1. Insert the nut back to the lever, using the motor with the screwto hold it easily. The wire end of the motor is pointing away from the objective side of the Z-stage. Tighten the two M3×8 screw to fix the nut - the nut must not be able to rotate.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_09.jpg" width="300">
</p>

1. This is how it should look like. The M3×8 screw should be tightened equally. Do not overtighten the screws - you might break the part.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_10.jpg" width="300">
</p>

1. Using two M3×8 screws, fix the motor to the Z-stage.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_11.jpg" width="300">
</p>

1. This is how it should look like now.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_12.jpg" width="300">
</p>

1. Insert a M3×8 screw in the objective mount as shown in the picture. Don't screw it all the way in but leave roughly 1 mm between the head of the screw and the flat side of the objective mount.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_13.jpg" width="300">
</p>

1. Insert the objective lens into its mount.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_14.jpg" width="300">
</p>

1. Insert the objective mount into the focussing insert. The head of the M3×8 screw goes into the slot in the insert. In case the screw is too tigten to the objective mount, it won't go into the slot - loosen the screw a little. In case the head of the screw is too far from the objective mount, it won't hold in the slot but fall through - tigten the screw a little.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_15.jpg" width="300">
</p>

1. The optimal case: the objective mount holds the objective in any position within the slot. You should be able to shift the objective but it shouldn not move on its own. Adjust the screw of the objective mount if necessary. The assembled insert looks like this:
<p align="center">
<img src="./IMAGES/Z_stage_assembly_16.jpg" width="300">
</p>

1. Place the insert inside the cube. For optimal use, the lid of the cube should be sideways from the insert, as shown in the picture. Close the cube using four M3×12 screws.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_17.jpg" width="300">
</p>

1. Add as many M3×8 screws as possible to both the lid and the bottom of the cube-body.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_18.jpg" width="300">
</p>

1. Time for the electronics: You will need the parts shown in this picture.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_19.jpg" width="300">
</p>

1. Connect all cables to the ESP32 following the [instructions](../../ELECTRONICS) in the Electronics section. The ESP32 will go on the side of the Z-stage and all the cables will go through the cube.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_20.jpg" width="300">
</p>

1. Place the ESP32 in the cube as shown in the picture. It needs to be on this side with respect to the objective and motor - this way the power cable won't be in the way in any of the setups where you might use the Z-stage.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_21.jpg" width="300">
</p>

1. Gently pull all the cables - both from ESP32 and stepper motor - through the cube and out on the side opposite to where the objective is looking.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_22.jpg" width="300">
</p>

1. Place the driver board of the motor on the objective side of the cube.  
<p align="center">
<img src="./IMAGES/Z_stage_assembly_23.jpg" width="300">
</p>

1. Gently glue or screw the driver board to the insert.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_24.jpg" width="300">
</p>

1. Connect all the cables of the ESP and the motor to the driver board ([Instructions](../../ELECTRONICS)).
<p align="center">
<img src="./IMAGES/Z_stage_assembly_25.jpg" width="300">
</p>

1. Gently fix the ESP32 to the cube - Done!
<p align="center">
<img src="./IMAGES/Z_stage_assembly_26.jpg" width="300">
</p>

1. This is the correct mutual position of the Z-stage insert, objective, motor, ESP32, motor controller and all the wires.
<p align="center">
<img src="./IMAGES/Z_stage_assembly_27.jpg" width="300">
<img src="./IMAGES/Z_stage_assembly_28.jpg" width="300">
<img src="./IMAGES/Z_stage_assembly_29.jpg" width="300">
<img src="./IMAGES/Z_stage_assembly_30.jpg" width="300">
</p>

1. Where next? [🢂 Software!](https://github.com/bionanoimaging/UC2-Software-GIT) No not plug anything in the power supply, unless you are sure everything is correctly connected.

### Tutorial with images (Fluomodule+Sample Insert)
This is the assembly guide for the Fluomodule+Sample Insert.
It's tought to work as a darkfield illumination. This reduces any scattering light (e.g. 0th order of the illumination).

1. All parts for this model
<p align="center">
<img src="./IMAGES/Z_STAGE_FLUOMODULE_0.jpg" width="300">
</p>

2. Solder the LEDs to the Transistor; The base of the transistor goes to the output of the ESP32, the 5V and GND as well; LEDs are connected in parallel; No resistor necessary. BD809 is connected to the LED in series
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
