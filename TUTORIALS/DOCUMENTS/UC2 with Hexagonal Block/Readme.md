# UC2 with Hexagonal Unit Block

Unit blocks are the key elements of each setup. All setup parts can be easily moved and aligned thanks to the modular UC2 block design like a piece of LEGO. The fundamental design of the unit block is cubic. But in this section, we used the hexagonal shape for the unit block design of the optical setups.  
The idea behind applying a hexagonal honeycomb shape is that the stability of such an optical setup yields a better result.

__Honeycomb structures__ are inspired by bee honeycombs. The way bees build hives is to provide maximum cell space by using a minimal amount of beeswax, indicating that the hexagonal honeycomb
structure is the most stable for nature. To sum up, application areas of honeycomb structures are architecture, aviation, space, transportation, mechanical engineering, chemical engineering, nanofabrication, and biomedicine such as tissue engineering and regenerative medicine [1].

Three corners of the top and bottom surfaces of the hexagonal block have holes for screws and they are placed in the corner of an equilateral triangle. A three-point connection is used for designing and it gives a better result in hexagonal structure than the cube structure.

<p align="center">
<img src="./IMAGES/" width="400">
</p>

You see two different hexagonal shape design above. In (a), the distance between two corners is the same as one side length of cube (50 mm) but the total space inside the hexagon is decreased and it caused some problems like unmatched optical components like the Thorlab Eyepiece lens and flashlight lamp.  
In (b), some changes are made on the (a), and problems are solved.


You see hexagonal insert designs below: LED holder (a), sample holder (b),  mirror holder(c), sample holder (d) version 2, Raspberry Pi camera holder (e), and objective lens holder (f).

<p align="center">
<img src="./IMAGES/Hexagonal block with inserts -v1.png" width="400">
</p>




# *continue editing*

In Figure 8, inserts are assembled with the hexagon base, hexagon lid, and hexagon base plate.
Cubes represent LED holder (a), sample holder (b), mirror holder (c), sample holder-version 2
(d), Raspberry Pi camera holder (e), an objective lens (f), respectively.

<p align="center">
<img src="./IMAGES/Hexagonal block with inserts -v1.png" width="400">
</p>



After ending up the design of hexagon blocks and related inserts, a Simple Microscope setup is built for testing new designs and compared them with original cubic design.

*add simple microscope setup rendered and real *



Let's try alternative unit block designs and try to improve stability problems of 4-holes-cube design.  

<p align="left">
<img src="./IMAGES/3-holes-cube and 4-holes-cube.png" width="400">
</p>

In this new block designs, 3 screw holes are used in the top and bottom surfaces of the cube instead of 4 screws holes and two additional magnet holes are added to the base plate.  
In (a), you see fundamental design of UC2 cube block and in (b), new designed cube block with less screw holes and more magnet holes.

Luckily, we can use already printed inserts from 4-holes-cube setups. They have same dimensions and can be usable for our new cube design.

<p align="left">
<img src="./IMAGES/3-holes-cube with inserts.png" width="400">
</p>

__*add stl files of the new designed cubes*__

You can find .stl files of baseplate, cube lid and cube base of 3-holes-cube block [here.](./DESIGNS)

We designed new cube blocks. Let's build a simple microscope setup and see the differences between 3-holes-cube and classical UC2 4-holes-cube design.  
In a finite correction optical system, the objective lens forms an intermediate image by itself. Light passing through the objective is directed toward the intermediate
image plane and converges at that point, undergoing constructive and destructive interference to produce an image.
A simple finite-corrected microscope is built with a light source like LED lamp or laser, sample, lens, mirror, and
camera (Raspberry Pi Camera Module v2) as a detector.

You can see simple microscope setup in Inventor as rendered image.

<p align="left">
<img src="./IMAGES/Assembly_SimpleMicroscope_T1_full_2.png" width="400">
</p>

And let's build a real Setup!

<p align="left">
<img src="./IMAGES/Simple Microscope experiment with 3-holes-cube.JPG" width="400">
</p>


### Result

###### Dreams vs. Reality

Our idea behind having a new design for cube block was to obtain a more stable connection between a cube block and a base plate with a triangular connection diagram.  
But in practice, this idea was impractical because;

+ 6 magnets were used instead of 4 magnets for each base plate.
  + It increases the total cost of the setup.
  + When I printed more than 1 base plate like 2, 3, or more, magnets can be a problem in the corners where 3 or 4 magnets are located next to each other. Neighbor magnets break the good connection link, while the cube attaches to the plate.

+ In the 2nd task, some optical components could not fit into the hexagon block like LED light source (flashlight), some objectives, and some Thorlab lenses. Therefore, I made new designs for unmatched components in Task 2. The LED light holder design.
+ In the 2nd task, the total area of the inside of the hexagon is smaller than the cube block. The size of the cube base part for 4 different tasks can be seen clearly in Figure 14. Side length
is 50 mm for Task 1, the distance between 2 edges is 50 mm but the longest distance is 58 mm for Tasks 2 and 3.

+ In the 2nd and 3rd tasks, hexagonal blocks could be used only on XY-plane horizontally. In the cube block system (1st task), cube blocks can be used XY- plane, and Z-plane together. And the same insert element of the block can be used horizontally and vertically.

+ In the 2nd and 3rd tasks, insert parts can not be moved inside the hexagon block. Because of this unlimited design property, newly designed inserts can be used in the setup. These inserts
are used without hexagon block base and lid parts.


### A short Message For the next UC2 Designers
You see the beauty of UC2. We had an idea and tried it and shared our experiences with you.   
UC2 is an open-source and improvable project for everybody. If you have any new idea, let's try and share your experiences with us.  
Keep dreaming and improving UC2 with next versions.

### Reference

[1] Honeycomb reference: Zhang, Q., Yang, X., Li, P., Huang, G., Feng, S., Shen, C., Han, B., Zhang, X., Jin, F., Xu, F., & Lu, T. J. (2015). Bioinspired engineering of honeycomb structure – Using nature to inspire human innovation. Progress in Materials Science, 74, 332–400. https://doi.org/10.1016/j.pmatsci.2015.05.001
