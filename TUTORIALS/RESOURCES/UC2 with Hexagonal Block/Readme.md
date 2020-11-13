# UC2 with Hexagonal Unit Block

Unit blocks are the key elements of each setup. All setup parts can be easily moved and aligned thanks to the modular UC2 block design like a piece of LEGO. The fundamental design of the unit block is cubic. But in this section, we used the hexagonal shape for the unit block design of the optical setups.  
The idea behind applying a hexagonal honeycomb shape is that the stability of such an optical setup yields a better result.

__Honeycomb structures__ are inspired by bee honeycombs. The way bees build hives is to provide maximum cell space by using a minimal amount of beeswax, indicating that the hexagonal honeycomb
structure is the most stable for nature. To sum up, application areas of honeycomb structures are architecture, aviation, space, transportation, mechanical engineering, chemical engineering, nanofabrication, and biomedicine such as tissue engineering and regenerative medicine [1].


<p align="center">
<img src="./IMAGES/Hexagon blocks 1 and 2.png" width="400">
</p>


You see two different hexagonal shape design above.   
Three corners of the top and bottom surfaces of the hexagonal block have holes for screws and they are placed in the corner of an equilateral triangle. A three-point connection is used for designing and it gives a better result in hexagonal structure than the cube structure.  
In (a), the distance between two corners is the same as one side length of cube (50 mm) but the total space inside the hexagon is decreased and it caused some problems like unmatched optical components like the Thorlab Eyepiece lens and flashlight lamp.  
In (b), some changes are made on the (a), and previous problems are solved.


Time to make insert designs.There are hexagonal insert designs version 1 below: LED holder (a), sample holder (b),  mirror holder(c), sample holder version 2 (d), Raspberry Pi camera holder (e), and objective lens holder (f).

</p>
<p align="center">
<img src="./IMAGES/Hexagonal block with inserts -v1.png" width="400">
</p>


After ending up the design of hexagon blocks and related inserts, a Simple Microscope setup is built for testing new designs and compared them with original cubic design.  
In a finite correction optical system, the objective lens forms an intermediate image by itself. Light passing through the objective is directed toward the intermediate
image plane and converges at that point, undergoing constructive and destructive interference to produce an image.  
__A simple finite-corrected microscope__ is built with a light source like LED lamp or laser, sample, lens, mirror, and
camera (Raspberry Pi Camera Module v2) as a detector.

Let's build Simple Microscope for Hexagonal block version 1.

*In the world of machines:*

</p>
<p align="center">
<img src="./IMAGES/Assembly_hexagon_SimpleMicroscope_T2_2.png" width="400">
</p>

*And in the world of homo sapience:*

</p>
<p align="center">
<img src="./IMAGES/hexagonal simple microscope setup.jpg" width="400">
</p>

The idea behind applying a hexagonal honeycomb shape is that the stability of optical setup acquired as a better result and six vertical surfaces are used in one setup with a trouble-free harmony.
And this motivation created Hexagonal block unit version 1. After testing version 1, we made some changes on it and solved some of problems.  

And ta-da! *Hexagonal Block version 2* was born.


In this design, six lateral surfaces of a hexagon can be used at the same time. Additionally, design is changed to recover the reduced space of the hexagon inside with hexagon base block with 3 pillars (legs) instead of 6. 6-pillars-base and 3-pillars-base can be used together in one system.  
In the base plate, there are still 6 magnets, but their location is changed.   
In the hexagonal base,there are 6 screws instead of 3 because the block can be spin around with 60-degree steps. Three different connection positions exist for one block on this base plate.  


</p>
<p align="center">
<img src="./IMAGES/hexagonal block version 2.png" width="400">
</p>

Image in the above includes 3 different attached options from different points of view. In the top and middle row, we see that block can be used in one position for two different angles. In the bottom row, the block can attach
to a different location with a half-a-unit shift of 25 mm.   
When 3 base plates are connected, a
new connection option for the hexagon block is obtained on this connection point of base plates.

Time to see version 2 blocks in real world:


</p>
<p align="center">
<img src="./IMAGES/Hexagonal v2 printed parts.png" width="400">
</p>


You can find .stl files of baseplate, cube lid and cube base of hexgaonal unit block version 1 designs [here](./STL/version1) and version 2 [here.](./STL/version2)


### Result

###### Dreams vs. Reality

Our idea behind having a new design for cube block was to obtain a more stable connection between a cube block and a base plate with a triangular connection diagram.  
But in practice, this idea was impractical because;

+ 6 magnets were used instead of 4 magnets for each base plate.
  + It increases the total cost of the setup.
  + When we print 4×1, 4×2, 4×4 base plates, magnets create a problem in the corners where 3 or 4 magnets are located next to each other. Neighbor magnets break the good connection link, while the cube attaches to the plate.

  </p>
  <p align="center">
  <img src="./IMAGES/1-base plat problem.png" width="400">
  </p>


  + It is really hard to insert some of the magnets into its places.

+ In the version 1, some optical components could not fit into the hexagon block like LED light source (flashlight), some objectives, and some Thorlab lenses. Therefore,new designs for unmatched components are made like LED light holder design.
</p>
<p align="center">
<img src="./IMAGES/hexagonal flashlight.JPG" width="400">
</p>

+ In the version 1, the total inside area of the hexagon is smaller than the fundamental cube block. The size of the cube base part for 3 different designs can be seen clearly below. Side length is 50 mm for fundamental cube block (a), the distance between 2 edges is 50 mm but the longest distance is 58 mm for hexagonal block designs version 1 and 2.
</p>
<p align="center">
<img src="./IMAGES/Base plate dimensions.png" width="400">
</p>


+ Hexagonal blocks could be used only on XY-plane horizontally. In the cube block system, cube blocks can be used XY-plane, and Z-plane together. And the same insert element of the block can be used horizontally and vertically.

+ Insert parts can not be moved inside the hexagon block. Because of this unlimited design property, newly designed inserts can be used in the setup. These inserts are used without hexagon block base and lid parts.


### A short Message For the next UC2 Designers
:juggling_person:  
You see the beauty of UC2. We had an idea and tried it and shared our experiences with you.   
UC2 is an open-source and improvable project for everybody. If you have any new idea, let's try and share your experiences with us.  
Keep dreaming and improving UC2 with next versions.  :heart:

### Reference

[1] Honeycomb reference: Zhang, Q., Yang, X., Li, P., Huang, G., Feng, S., Shen, C., Han, B., Zhang, X., Jin, F., Xu, F., & Lu, T. J. (2015). Bioinspired engineering of honeycomb structure – Using nature to inspire human innovation. Progress in Materials Science, 74, 332–400. https://doi.org/10.1016/j.pmatsci.2015.05.001
