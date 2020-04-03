# BASE CUBE
This is the repository for the base-cube design. The design-files can be found in the folder [INVENTOR](./INVENTOR).

The basic building unit consists of 3 components.

1. **The Base** which serves as the skeleton of all setups and where the ball magnets will be fed in [More about baseplates.](../ASSEMBLY_Baseplate_v2/)
2. **The Lid** that closes the cube. It is attached by four screws
3. **The Cube Body** where all the functions (i.e. Mirrors, LED's etc.) find their place - insert that define the function of the cube are placed in the body before closing the lid

<p align="center">
<img src="./IMAGES/BASE_CUBE_v2_1.png" width="400">
</p>

The function which fits into the cube is not necessarily bound to optics. It can be anything!
The function is defined by the insert and all our insert are in the respective module folder in [CAD](../)

<p align="center">
<img src="./IMAGES/BASE_CUBE_v2_2.png" width="400">
</p>

### <img src="./IMAGES/F.png" width="40">Devices features:

* Click-Mount via Ball-Magnets/Screws
* Possible electric connection
* Fill in whatever function you want
* Modularized design
* Low-cost production
* Very precise
* Open-Source
* Mount it in all possible directions

## [<img src="./IMAGES/P.png" width="40">3D Printing](./STL)

### <img src="./IMAGES/A.png" width="40">Assembly Video Tutorial

[![UC2 YouSeeToo - How to assemble the base-cube?](./IMAGES/UC2_Assembly_BaseCube.png)](https://www.youtube.com/watch?v=zAMedY0mWKA)

## <img src="./IMAGES/A.png" width="40">Assembly Tutorial with images
([TUT02 of TUTORIALS](../TUTORIALS))
### OLD VERSION!!! Assembly Tutorial with images (Cube v0)
      This section needs a update!

1. All parts for this model
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount1.jpg" width="300">
</p>

2. Widen the holes to <~5.9mm with a drillin-tool
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount2.jpg" width="300">
</p>

3. Insert the lens inside the part (don't touch it!)
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount3.jpg" width="300">
</p>

4. Add the fixation ring
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount5.jpg" width="300">
</p>

5. Fix the ring so that the lens is not loose - don't touch the lens!
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount6.jpg" width="300">
</p>

6. Insert rods inside the cube
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount8.jpg" width="300">
</p>

7. Mount the lens on the rods
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount9.jpg" width="300">
</p>

8. Fasten the rods
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount10.jpg" width="300">
</p>

9. Add the lid to the cube and screw it
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount11.jpg" width="300">
</p>

10. Check if it's tilting - if so: Align screws!
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount12.jpg" width="300">
</p>

11. Done!
<p align="center">
<img src="./IMAGES/UC2_Tut_Lensmount13.jpg" width="300">
</p>

## <img src="./IMAGES/L.png" width="40">Electronics
The Arduino/ESP32 can be introduced with hot-glue or a rubber band, for parts with motors or LEDs.

## CAD Design
Please also see the Module developer kit ([MDK](../../MDK)) for further design instructions on how you sould adapt to the UC2 cubes.

## OpenSCAD files
Open-Souce also means, that one should be able to modify the files with open-source software. Therefore we provide the basic cube as an ```.scad``` file in the [OPENSCAD](./OPENSCAD) folder.  The Inventor files will follow soon!

## Tutorial on how to design an insert in Inventor
Find the tutorial in the [INVENTOR](./INVENTOR) folder.

## Participation
We are eager to see your results! Feel free to file a pull-request or share it via mail or [@openUC2 on Twitter](https://twitter.com/openUC2) .
