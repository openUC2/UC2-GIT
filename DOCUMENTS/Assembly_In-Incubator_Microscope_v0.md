(Assembly) Manual for In-Incubator Microscope v1

Step by step guide for using the raspberry pi with the microscope

V0, 31.8.20180

B. Diederich

Introduction
============

This is a rough set of instructions to start building your own
in-incubator microscope. It comes with the files in our repository
<https://github.com/bionanoimaging/UC2-git> .

It guides you through the major steps which are

1.  Buying parts

2.  3D printing components

3.  Assembling sub-parts

4.  Soldering parts

5.  Flashing parts

6.  Assembling Microscope

7.  Quick-Start

It should serve as a growing manual rather then being a complete list
with detailed trouble-shooting solutions. If you find any error or
unclear sections; Feel free to contribute or report any erros. Thanks!

Buying parts
============

A detailed list with all parts necessary for the microscope can be found
under /Documents/. It’s not mandatory to get exactly the components
you’ll find in the list-. The suppliers and prices may vary. If you have
the abilities to order parts overseas everything gets much cheaper!
Major components are the Raspi+Camera, Arduinos and Light sources.

The magnetic – snap-fit system which allows a very convenient connection
between parts can be replaced by a soldered/wired connection which
reduces the price and availability enormously.

3D printing components 
=======================

In the folder CAD/In\_Incubator\_Microscope/STL you’ll find a list of
exported CAD files. Those are ready to print:

  Filename                                                                   Function                                               \#
  -------------------------------------------------------------------------- ------------------------------------------------------ ----
  IN-INCUBATOR\_MICROSCOPE\_Assembly\_base\_4x2.stl                          Base, holds Magnets, Cubes and electronic connectors   1
  IN-INCUBATOR\_MICROSCOPE\_v0\_05\_\_RMS\_Adapter\_29.stl                   Adapter for RMS-threaded Objective lenses              1
  IN-INCUBATOR\_MICROSCOPE\_v0\_10\_Cube\_LED\_Array\_10.stl                 Cube-Adapter for LED-Matrix                            1
  IN-INCUBATOR\_MICROSCOPE\_v0\_10\_Cube\_v0\_18.stl                         Cube                                                   2
  IN-INCUBATOR\_MICROSCOPE\_v0\_10\_Lid\_el\_v0\_19.stl                      Lid for cube which holds electronics                   3
  IN-INCUBATOR\_MICROSCOPE\_v0\_11\_BS\_1inch\_Mirror\_Thorlabs\_20.stl      Cube-Adapter for 1inch mirrors                         1
  IN-INCUBATOR\_MICROSCOPE\_v0\_11\_Mirror\_Adapter\_for\_RaspiCam\_16.stl   Cube-Adapter for Raspberry Pi Camera                   1

We printed the parts using an Ultimaker 2+ with ABS material. We won’t
give a detailed set of instructions on how-to-print components here, but
you can find nice explanations in several printing-wikis like this one:
<https://www.3dhubs.com/knowledge-base> .

Parameters of CURA-Software are as follows:

-   Infill-Density: 50 % (especially the cubes should have &gt;40%
    infill due to stability)

-   Layer height: .1 mm works fine

-   Printing support: only the Z-focus needs some support to work
    properly, everything else is designed the way that it works
    out-of-the-box

-   BRIM, etc.: You’re better of if you don’t use any BRIM

Assembling the cubes 
=====================

Putting together a cube and the Base-plate follows the IKEA-principle.
Grab the stuff and tools, get angry, then it works. Below you’ll find a
basic cube without any inlets. What you need are 4 cylinder-head (ISO
912, M3, 18mm long) screws which hold the Lid (turkis) in place of the
cube (Green). The orientation of the Lid advices the position of the
magnetic-fit connector which comes into the hole (if necessary). For a
detailed descritption please have a look in the guide on how a basic
design for cubes have to look like.

If a firror should go into the cube, you have to slide it in before –
please wit care; 3D printed material might break. Once done, you can get
the ball-magnets (6mm) ready and put them onto the screws. Place the
Cube with the screws heading the 4 holes in the base on it. Apply some
force, so that the balls snap into the 3D printed holes.

Done! Repeat it for the other components. It’s always the same
mechanism.

![](./2/media/image1.png){width="3.00042104111986in"
height="3.0897779965004375in"}

Soldering 
==========

Soldering of the parts is very simple. You only need to make sure that
all parts receive 5V and GND from a power-supply which has &gt; 2A of
“power”. The SCL and CLK coming from te Raspberry have to be attached to
all Arduinos.

Specific functions like driving a stepper is explained in a dedicated
folder “/Electronics”

Each electronic component works independent. If you’ve connected the
IC2-able devices to the Raspi the first time (make sure that GND is the
same everywhere) you can look for connected devices using the command

*IC2-detect -y -all*

Hints: It is possible to get the +5V/Gnd signal also from the raspberry
pi. These pins are not fused, thus if there is a shortcut it can break!

Parts – Checklist 
==================

If everything’s done, you should find the following parts. We have
already renewed the Z-stage. Below you’ll find the “older version” of
Richard Bowman’s design.

![](./2/media/image2.emf){width="0.2831856955380577in"
height="0.38053040244969377in"}![](./2/media/image3.jpeg){width="6.295833333333333in"
height="3.5416666666666665in"}

1.  Raspberry pi with 7 inch screen

2.  XYZ-stage

3.  Mirror-Block

4.  Cam-Block

5.  Fluorescence Block

6.  LED-Array Block

7.  Backplate

8.  Objective lens

9.  Sample spacer

10. Sample

Step-by-step assembly guide
===========================

1.  Connect wires to magnetic connectors at the backplate

    ![](./2/media/image4.jpeg){width="5.823008530183727in"
    height="3.2756835083114613in"}

2.  Put the microscope objective lens into the holder of the xyz-stage

    ![](./2/media/image5.jpeg){width="5.8217946194225725in"
    height="3.275in"}

3.  Allign the mirror-cube and the camera-cube

    ![](./2/media/image6.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

4.  Attach the mirror- and camera block to the backplate

    ![](./2/media/image7.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

5.  Attach the XYZ-stage to the backplate

    ![](./2/media/image8.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

6.  Put sample-spacer on the XYZ-stage and place sample on it

    ![](./2/media/image9.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

7.  Attach LED-Array to the backplate

    ![](./2/media/image10.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

8.  Connect backplate to the Raspberry-pi

    ![](./2/media/image11.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

Install the firmware of all devices 
====================================

-   Please a

Start the microscope
====================

1.  Plug in the power-supply of the Raspberry-pi

    ![](./2/media/image12.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

2.  Let the Pi boot up

    ![](./2/media/image13.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

3.  Wait about 30 seconds until the experiment scree appears

    ![](./2/media/image14.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

4.  Aliging the smaple while switichg on the preview (Swith on Light,
    control focus and X/Y movement with the
    buttons)![](./2/media/image15.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

    ![](./2/media/image16.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

Start Experiment 
=================

1.  Select “Start
    Experiment![](./2/media/image17.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

2.  First choose Timing (Meas-iter, Total duration) then select
    acquisition method (i.e. Bright-field, qDPC,
    etc.)![](./2/media/image18.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

3.  Choose Start Experiment

4.  ![](./2/media/image19.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

5.  6.  Experiment starts and can be stopped by pressing the
    stop-button![](./2/media/image20.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}![](./2/media/image21.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}![](./2/media/image22.jpeg){width="6.295833333333333in"
    height="3.5416666666666665in"}

Get the data from the device\
=============================

Troubleshooting
===============

If everything fails unplug the device – if it still doesn’t work:

-   Open the TERMINAL

-   Type cd \~/Programming/PPS-app/code/

-   Type python main.py

Copying the images

-   Open the file explorer

-   Plugin the device

-   
