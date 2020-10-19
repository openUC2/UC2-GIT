# UC2 with 3-holes-cubes

In UC2, blocks are the key elements of each setup. All setup parts can be easily moved and aligned thanks to the modular UC2 block design like a piece of LEGO. The fundamental design of the unit block is cubic, and it has 4 holes for screws in the top and bottom surfaces. Screws connect two parts of the cube (lid and base) and help the cube to attach to the skeleton of the setup, the baseplate. Classical baseplate design has 4 holes in each corner for ball magnets.

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


+ The location of the screws cannot create a stable connection between cube and plate. Because magnets are located in a triangular shape.  
In practice, magnets generate a gap from the plate through the cube.  In the attachment points, it does not create a problem but in screw-free points, the gap between plate and cube breaks the stability of the system. When we touch the screw-free corners, the cube moves up and down.

+ To connect lid and base we must use an additional two setscrews. Otherwise, they will not attach properly.

+ 6 magnets were used instead of 4 magnets for each base plate.
  + It increases the total cost of the setup.
  + When we print more than 1 base plate like 2, 3, or more, magnets can be a problem in the corners where 3 or 4 magnets are located next to each other. Neighbor magnets break the good connection link, while the cube attaches to the plate.

### A short Message For the next UC2 Designers
You see the beauty of UC2. We had an idea and tried it and shared our experiences with you.   
UC2 is an open-source and improvable project for everybody. If you have any new idea, let's try and share your experiences with us.  
Keep dreaming and improving UC2 with next versions.
