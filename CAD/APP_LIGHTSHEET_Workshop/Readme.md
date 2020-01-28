# Lightsheet Setup (Workshop)
This is the manual for the Lightsheet Microscope used for the International Day of Light (IDoL) workshop.

The stl-files can be found in the folder [STL](./STL).

### Purpose
Produce 3D images with better sectioning.

![](./IMAGES/Assembly_simple_Lightsheet_v1.png)

## Properties
* design is derived from the base-cube

## Parts

### 3D printing parts
* Please find all parts inside the folder [STL](./STL)
### Additional parts
* Please have a look at the bill of materials  



## Remarks and Tips
### 3D Printing:
* No support required in all designs
* Carefully remove all support structures (if applicable)

## Assembly and Alignment of the optical path
Here we briefly give a step-by-step tutorial on how-to allign the beam-path.

The illumination path is independent from the detection path - the order how you align it is up to you.

A simplified scheme can be found [here](./IMAGES/UC2_fullBOX_lightsheet_EN.pdf).

## Assemble the illumination path (light sheet)
Here we try to form the light sheet.

#### 1. Mount the pre-assembled laser cube
* Make sure the Laser-Cube is mounted in such a way, that the four screws that are used for centering the laser are pointing each through a different side of the cube. In other words, the laser inserts must be rotated by 180° with respect to each other.
* Insert the laser in the cube the way that the end with the light source is not sticking out of the cube. The centering screw from the top should be pressing on the light source end.
* The end with the switch is sticking out of the cube. Make sure you can switch it on with the clamp.
* Switch on the laser with the clamp.
* The laser has a line profile. Rotate it inside the holder until the line is horizontal.
* Center the laser roughly with the four centering screws.
* Place he Laser-Cube on the baseplate as indicated by the Animation below.
* ATTENTION: !Don't hit your or anybody's eyes!
* If you make a break or do something else than aligning at the moment, always switch off the laser to make sure you don't endanger anybody's eyesight!

#### 2. Align the telescope
* Place the pre-assembled telescope on the baseplate right after the laser.
* After the laser, first comes the iPhone lens and that the convex lens, in order to collimate the beam.
* Shift the iPhone lens inside the rail back and forth until a parallel (i.e. collimated) beam is created.
* This can be measured by simply comparing the beam at a distance of 2cm and 20 cm right after the telescope: The diameter should not change.
* The telescope should be in the same height as the laser, hence centered.
* Align the telescope and the laser to the same height - The beam profile must not be visible after collimation. If the height is not correctly aligned, the collimated beam will fade away on one side.
* ATTENTION: !Don't hit your or anybody's eyes!

#### 3. Add the cylindrical lens
* Place the pre-assembled lens-mount on the baseplate right after the telescope.
* The axis of the cylindrical lens must be horizontal.
* The flat side of the lens must face away from the telescope - in the direction of the mirror-Cube.
* Currently, 63 mm cylindrical lenses are used. Slide the lens inside the cube as far as possible from the telescope.
* Observe the line-focus of the collimated beam. The focus line must be vertical.
* ATTENTION: !Don't hit your or anybody's eyes!

#### 4. Add the pre-mounted fold-mirror
* Place the pre-assembled 45° fold kinematic mirror on the baseplate after the cylindrical lens.
* It the beginning, the mirror should fold the beam by roughly 90°.
* ATTENTION: !Now the laser beam is going to a perpendicular direction to the one before. Make sure to block the light with i.e. a cardboard, so it can't leave you setup and hit somebody's eyes!

#### 5. Add the pre-mounted objective lens
* If not done already, remove the covers of the 4× objective - they're in the way of your working distance.
* Place the pre-assembled 4x objective lens on the baseplate perpendicular to the kinematic mirror
* Slide the objective holder inside the cube as far as possible from the mirror.
* Tune the kinematic mirror to get as much light as possible through the objective.
* If the height is too far off, adjust the position of the telescope and centering of the laser.
* Tune the focus of the illumination so that the light sheet is roughly in the center of the following block-position.
* Tuning the objective lens can be done by shifting it back and forth in the spring-loaded spiral bearing.  

#### 6. Add the sample-stage
* Place the pre-assembled sample-stage on the baseplate right after the 4x objective lens
* The motor must be pointing over the side of the baseplate
* The light sheet should be aligned in the center of the sample-stage plate and in mid-height.
* Switch the laser off for now.

## Time for electronics

#### 1. Rasperry Pi
* Plug the camera in the RasPi, if not done already.
* Plug the Raspi into an electrical socket. It will switch on automatically.
* When loaded, open the UC2 GUI by double-clicking the icon on the screen and choosing "Execute in command window". Wait until it loads.

#### 2. Motors
* Plug the USB hub in the RasPi.
* Plug the Z-stage and sample-stage into the USB hub using the two USB-microUSB cables. There should be a light on the ESP, once you plug it in.

#### 3. Check if everything works
* Check the camera by clicking on "Camera preview" in the GUI. Let it run.
* Check the Z-stage: Choose Z in the bottom left part on the screen. You can change the step size and move it in either of the directions. Check that the stage really moves in both directions when you press the buttons.
* Check the sample-stage: Choose X in the bottom left part on the screen. You can change the step size and move it in either of the directions. Check that the stage really moves in both directions when you press the buttons.

## Assemble the detection path
Here we try to form the compound microscope.

#### 1. Mount the pre-assembled z-stage
* Make sure the objective is mounted in the Z-stage in such a way that it is "looking out of the cube and to the other side than the motor is mounted".
* Place the Z-stage perpendicular to the illumination light sheet. The objective is now looking roughly on the center of the sample-stage.
* Be careful, do not break any electronics.

#### 2. Place the camera cube
* Place the camera cube behind the Z-stage, with leaving one free position in between them.
* Attach the filter in front of the camera using sticky tape.

#### 3. Find the focus of the detection path
* From now on, the stray light might be a problem. Cover your setup or at least the detection path.
* Take a flashlight and shine through the detection objective on the camera.
* Take a piece of paper and hold it in front of the detection objective. Move it back and forth and observe the image of the RasPi camera. Find the focus of your detection path.
* Move the objective in the Z-stage by hand in order to bring the focus plane of your detection path to the center of the sample-stage.
* The detection objective has to "hang" out of the Z-stage quite a lot in order to allow you to image the center of the sample-stage.  

#### 4. Align the detection path
* Place a sample (ideally a sheet of paper tilted 45° w.r.t. the illumination/detection path).
* Use a lens tissue painted with an yellow highlighter - then you directly use the fluorescence property!
* The paper can be mounted using the magnetic sample mount and fixed with some sticky tape.
* Take a flashlight and shine through the detection objective on the camera.
* Move your sample by hand the see a focused part of the paper on the screen. Tilt your sample with respect to your detection so you'll also see the defocused parts that are closer or further.
* Remove the sample for now.

#### 5. Align the illumination path
* Switch on the laser. Be careful! Do not hit somebody's eyes!
* Firstly, the light sheet should be aligned in height to illuminate the area observed by the detection objective. Adjust the height of the illumination path if necessary (see steps above).
* Align the light sheet roughly in such a way that the waist (the thinnest part of the light sheet) is in front of the detection objective). Trace your light sheet with a piece of paper to find the waist.
* The focus of the 4× objective lens (therefore of the light-sheet) can be varied coarsely by shifting the lens back and forth in the spiral mount.
* Place the sample(the lens tissue) on the sample stage. Bring it to the focus as described in the previous section, using flashlight and focusing in by hand.
* Once you see the structure of the paper, align the light sheet onto the focus plane - tilt the kinematic mirror, adjust the focus of the 4× objective.
* Kinematic mirror: Take a hex key and turn the screw of the mirror - this mirror varies the angle of the light sheet and the position where it hits the back focal plane of the 4x objective lens respectively.

<p align="center">
<img src="./IMAGES/Assembly_simple_Lightsheet_v3.jpg" width="400">
</p>

#### 5. Use of filters
* When using a correct filter between the Z-stage and the camera, it's possible to observe a fluorescent image of the sample.
* Without filters you capture only the scattering image.

## Imaging with the light sheet microscope
* The focus of the detection path can be finely adjusted using the Z-stage motor (GUI - Z).
* Z-series can be acquired by moving the sample (GUI - X) through the focused light sheet plane - Move the sample-stage in both directions, using the lens tissue as a sample, to observe how the camera image changes.
* To acquire an image: Choose "Start experiment" on the right side of the screen, click "Custom" on the top right side and then "Snap" on the bottom right side.

## The result could look like this:

##### Fluorescent Image (*Pollengrain in Agarose*)
<p align="center">
<img src="./IMAGES/Assembly_simple_Lightsheet_v4.png" width="400">
</p>

##### Brightfield Image (*Pollengrain in Agarose*)
<p align="center">
<img src="./IMAGES/Assembly_simple_Lightsheet_v5.png" width="400">
</p>

## Animation
<p align="center">
<img src="./IMAGES/UC2Lightsheet.gif" width="400">
</p>

## Safety
Don't touch the optical surfaces of lenses and objectives!

Attention, don't cut your fingers while removing the lens from the iPhone sensor and the support material from 3D printed parts!

Never (!) look into the laser pointer! It will damage your eye immediately!


* ATTENTION: NEVER LOOK DIRECTLY INTO THE LASER! EYE WILL BE DAMAGED DIRECTLY
* NEVER SWITCH ON THE LASER WITHOUT INTENDED USE
* BEAM HAS TO GO AWAY FROM ONESELF - ALWAYS!
